#!/usr/bin/env python3
"""Hackathon-safe setup.

Adds the workspace contract and installs plugins from this public repository.
Never overwrites existing files and never touches ~/.codex configuration or
agent profiles.

Usage, from the task workspace:
    python3 <repo>/hackathon/setup.py --dry-run
    python3 <repo>/hackathon/setup.py
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
WORKSPACE = Path.cwd()
PLUGINS = (
    "superjuseong@superjuseongs",
    "spec-first@superjuseongs",
    "hackathon@superjuseongs",
)
DRY = "--dry-run" in sys.argv


def say(status: str, message: str) -> None:
    print(f"[{status}] {message}")


def codex(*args: str) -> bool:
    if DRY:
        say("dry", "codex " + " ".join(args))
        return True
    result = subprocess.run(["codex", *args], capture_output=True, text=True)
    if result.returncode != 0:
        say("fail", f"codex {' '.join(args)}: {(result.stderr or result.stdout).strip()[:200]}")
        return False
    return True


def main() -> None:
    # 1. Workspace contract. A task-provided AGENTS.md always wins.
    contract = WORKSPACE / "AGENTS.md"
    if contract.exists():
        say("note", "task already has AGENTS.md; not modified. "
            f"Tell Codex to also follow {HERE / 'AGENTS.md'}.")
    else:
        if not DRY:
            shutil.copy2(HERE / "AGENTS.md", contract)
        say("add", str(contract))

    # 2. Plugins from this public repository.
    if shutil.which("codex") is None and not DRY:
        say("fail", "codex CLI not found; skills not installed. AGENTS.md alone still works.")
        return
    # Fails harmlessly if the marketplace is already registered.
    codex("plugin", "marketplace", "add", str(REPO))
    for plugin in PLUGINS:
        if codex("plugin", "add", plugin):
            say("add", plugin)

    print("\nNext: start a new codex session, check /status and /model, "
          "then run $hk-kickoff.")


if __name__ == "__main__":
    main()
