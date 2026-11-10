#!/usr/bin/env python3
"""Install one or both frontend skill families in a target repository, safely."""
import argparse
import hashlib
import os
import shutil
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DEST = {"claude": Path(".claude/skills"), "codex": Path(".agents/skills")}


def fingerprint(folder: Path) -> dict[str, str]:
    """Hash every file, and refuse to follow symlinks within a skill tree."""
    entries = {}
    for path in folder.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Symlink in skill directory: {path}")
        if path.is_file():
            entries[path.relative_to(folder).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return entries


def no_link_ancestors(path: Path, boundary: Path) -> None:
    current = path
    while True:
        if current.is_symlink():
            raise ValueError(f"Refuse symlink target or ancestor: {current}")
        if current == boundary:
            return
        if current == current.parent:
            raise ValueError(f"Destination outside project: {path}")
        current = current.parent


def install(project: Path, host: str = "both", pack: str = "both", dry_run: bool = False, replace: bool = False) -> int:
    project = Path(project).expanduser().resolve()
    if not project.is_dir():
        raise ValueError(f"Project directory does not exist: {project}")
    hosts = list(DEST) if host == "both" else [host]
    if not set(hosts) <= set(DEST):
        raise ValueError(f"Unknown host: {host}")
    if pack not in ("both", "ux-laws", "wcag21"):
        raise ValueError(f"Unknown pack: {pack}")
    folders = sorted(p for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()
                     and (pack == "both" or p.name.startswith("ux-" if pack == "ux-laws" else "wcag21-")))
    if not folders:
        raise ValueError("No source skills found")

    actions, errors = [], []
    for h in hosts:
        for folder in folders:
            dest = project / DEST[h] / folder.name
            try:
                no_link_ancestors(dest, project)
                if dest.exists() and not dest.is_dir():
                    raise ValueError(f"Non-directory destination: {dest}")
                if not dest.exists():
                    action = "install"
                elif fingerprint(dest) == fingerprint(folder):
                    action = "unchanged"
                elif replace:
                    action = "replace"
                else:
                    raise ValueError(f"Existing different skill: {dest}; --replace required after review")
                fingerprint(folder)  # guard against publishing symlinked or compromised source trees
                actions.append((action, folder, dest))
            except ValueError as exc:
                errors.append(str(exc))
    if errors:
        raise ValueError("Preflight failed; no files changed:\n" + "\n".join(errors))
    for action, _, dest in actions:
        print(f"{action:9} {dest}")
    if dry_run:
        print("Dry run; no files changed.")
        return len(actions)

    stages: list[Path] = []
    backups: list[tuple[Path, Path]] = []
    installed: list[Path] = []
    try:
        for action, folder, dest in actions:
            if action == "unchanged":
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            stage = dest.parent / f".{dest.name}.stage-{uuid.uuid4().hex}"
            shutil.copytree(folder, stage)
            stages.append(stage)
        stage_index = 0
        for action, _, dest in actions:
            if action == "unchanged":
                continue
            stage = stages[stage_index]
            stage_index += 1
            if action == "replace":
                backup = dest.parent / f".{dest.name}.backup-{uuid.uuid4().hex}"
                dest.rename(backup)
                backups.append((dest, backup))
            os.replace(stage, dest)
            installed.append(dest)
        for _, backup in backups:
            shutil.rmtree(backup)
    except Exception:
        for dest in reversed(installed):
            if dest.exists():
                shutil.rmtree(dest)
        for dest, backup in reversed(backups):
            if backup.exists():
                backup.rename(dest)
        raise
    finally:
        for stage in stages:
            if stage.exists():
                shutil.rmtree(stage)
    print(f"Checked {len(actions)}; newly installed/replaced {sum(a != 'unchanged' for a, _, _ in actions)}.")
    return len(actions)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True, help="Existing target repository directory")
    parser.add_argument("--host", choices=("claude", "codex", "both"), default="both")
    parser.add_argument("--pack", choices=("ux-laws", "wcag21", "both"), default="both")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--replace", action="store_true", help="Allow replacing same-named skills after review")
    args = parser.parse_args()
    try:
        install(args.project, args.host, args.pack, args.dry_run, args.replace)
    except ValueError as exc:
        parser.error(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
