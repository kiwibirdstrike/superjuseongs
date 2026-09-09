# Superjuseong's

A lean personal Agent OS for Codex: eight reusable skills, eight Luna High specialist profiles, and a thin global operating contract.

## Install

Requirements: macOS or Linux, Python 3.11+, and the `codex` CLI.

```bash
git clone git@github.com:kiwibirdstrike/superjuseongs.git ~/superjuseongs
python3 ~/superjuseongs/install.py
```

The installer:

- backs up an existing global `AGENTS.md` and overlapping agent profiles;
- installs the global operating contract and eight agent TOMLs;
- enables native subagents, limits nesting to one level, and disables persistent goals;
- registers this repository as a local plugin marketplace and installs `superjuseong@superjuseongs`.

Start a new Codex thread after installation.

## Contents

- `plugins/superjuseong/`: installable skills-only plugin
- `config/AGENTS.md`: global operating contract
- `config/agents/`: Luna High specialist profiles
- `.agents/plugins/marketplace.json`: local marketplace definition

## Update

```bash
git -C ~/superjuseongs pull
python3 ~/superjuseongs/install.py
```

The installer is intentionally local and personal. Public plugin-directory submission is not included.
