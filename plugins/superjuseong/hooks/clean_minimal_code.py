"""Inject the canonical coding overlay without reading/writing session state."""
import json
from pathlib import Path
import sys

try:
    payload = json.load(sys.stdin)
except (ValueError, OSError):
    sys.exit(0)

event = payload.get('hook_event_name') if isinstance(payload, dict) else None
if event not in ('SessionStart', 'SubagentStart'):
    sys.exit(0)

skill = Path(__file__).resolve().parents[1] / 'skills/clean-minimal-code/SKILL.md'
body = skill.read_text(encoding='utf-8').split('---', 2)[2].strip()
print(json.dumps({'hookSpecificOutput': {'hookEventName': event, 'additionalContext': body}}))
