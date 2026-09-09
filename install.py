#!/usr/bin/env python3
"""Install Superjuseong's into the current user's Codex configuration."""

from __future__ import annotations

import re
import shutil
import subprocess
import os
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))


def set_toml_value(text: str, section: str, key: str, value: str) -> str:
    lines = text.splitlines()
    header = f"[{section}]"
    try:
        start = lines.index(header)
    except ValueError:
        suffix = "" if not lines or not lines[-1] else "\n"
        return text.rstrip("\n") + suffix + f"\n{header}\n{key} = {value}\n"

    end = next(
        (index for index in range(start + 1, len(lines)) if lines[index].startswith("[")),
        len(lines),
    )
    pattern = re.compile(rf"^\s*{re.escape(key)}\s*=")
    for index in range(start + 1, end):
        if pattern.match(lines[index]):
            lines[index] = f"{key} = {value}"
            return "\n".join(lines) + "\n"
    lines.insert(end, f"{key} = {value}")
    return "\n".join(lines) + "\n"


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def main() -> None:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = CODEX_HOME / "backups" / f"superjuseongs-{timestamp}"
    agents_dir = CODEX_HOME / "agents"
    CODEX_HOME.mkdir(parents=True, exist_ok=True)
    agents_dir.mkdir(parents=True, exist_ok=True)

    current_agents = [agents_dir / source.name for source in (ROOT / "config/agents").glob("*.toml")]
    if (CODEX_HOME / "AGENTS.md").exists() or any(path.exists() for path in current_agents):
        backup.mkdir(parents=True, exist_ok=True)
        if (CODEX_HOME / "AGENTS.md").exists():
            shutil.copy2(CODEX_HOME / "AGENTS.md", backup / "AGENTS.md")
        backup_agents = backup / "agents"
        for path in current_agents:
            if path.exists():
                backup_agents.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, backup_agents / path.name)

    shutil.copy2(ROOT / "config/AGENTS.md", CODEX_HOME / "AGENTS.md")
    for source in (ROOT / "config/agents").glob("*.toml"):
        shutil.copy2(source, agents_dir / source.name)

    config_path = CODEX_HOME / "config.toml"
    config = config_path.read_text() if config_path.exists() else ""
    for section, key, value in (
        ("features", "multi_agent", "true"),
        ("features", "child_agents_md", "true"),
        ("features", "goals", "false"),
        ("agents", "max_threads", "6"),
        ("agents", "max_depth", "1"),
    ):
        config = set_toml_value(config, section, key, value)
    config_path.write_text(config)

    marketplaces = subprocess.run(
        ["codex", "plugin", "marketplace", "list"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    if not re.search(r"(?m)^superjuseongs(?:\s|$)", marketplaces):
        run("codex", "plugin", "marketplace", "add", str(ROOT))
    run("codex", "plugin", "add", "superjuseong@superjuseongs")

    print("Installed Superjuseong's. Start a new Codex thread to load it.")
    if backup.exists():
        print(f"Backup: {backup}")


if __name__ == "__main__":
    main()
