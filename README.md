# Superjuseong's

A lean personal Agent OS for Codex: nine reusable skills, eight Luna High specialist profiles, a thin global operating contract, and a stateless Clean Minimal Code C2 hook.

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

- `plugins/superjuseong/`: installable skills and coding-overlay hooks
- `config/AGENTS.md`: global operating contract
- `config/agents/`: Luna High specialist profiles
- `.agents/plugins/marketplace.json`: local marketplace definition

## Update

```bash
git -C ~/superjuseongs pull
python3 ~/superjuseongs/install.py
```

The installer is intentionally local and personal. Public plugin-directory submission is not included.

## Clean Minimal Code

C2 combines minimal code with explicit data flow for the next agent. Its default
is `middle`; ask for `clean-minimal-code low`, `middle`, `high`, or `off` in the
conversation. Low minimizes the required patch, middle balances simplification
and clarity, and high actively removes proven redundancy in the touched path.
All levels retain readability, validation and proportionate tests. Only middle
has been evaluated in the local comparative experiments.

The SessionStart hook (including compaction) and SubagentStart hook inject the
same canonical skill text. There is no prompt tracker, state file or persistent
loop. Intensity is a conversation instruction, not a globally persisted setting;
pass the chosen level explicitly when delegating without conversation context.
The overlay applies only to coding work, not ordinary conversation.

After install, use `/hooks` to review and trust the two Superjuseong hooks if
Codex requests it, then start a new thread. Disable any other minimal-code
overlay such as Ponytail to avoid conflicting defaults. Hook trust is local to
the installation and is not distributed in this repository.
