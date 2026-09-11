"""Run with python3 hooks/test_clean_minimal_code.py; no external packages."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'hooks/clean_minimal_code.py'

with tempfile.TemporaryDirectory() as directory:
    for event in ('SessionStart', 'SubagentStart'):
        result = subprocess.run([sys.executable, str(SCRIPT)], input=json.dumps({
            'hook_event_name': event, 'source': 'compact', 'cwd': directory}),
            cwd=directory, capture_output=True, text=True, check=True)
        output = json.loads(result.stdout)
        specific = output['hookSpecificOutput']
        assert specific['hookEventName'] == event
        body = (ROOT/'skills/clean-minimal-code/SKILL.md').read_text().split('---', 2)[2].strip()
        assert specific['additionalContext'] == body
        assert set(output) == {'hookSpecificOutput'}
    for payload in ('not json', '{}', '[]', '{"hook_event_name":"Stop"}'):
        result = subprocess.run([sys.executable, str(SCRIPT)], input=payload,
            cwd=directory, capture_output=True, text=True, check=True)
        assert not result.stdout
    assert not list(Path(directory).iterdir()), 'hook wrote runtime state'
print('PASS: event routing, canonical context, invalid input, no state writes')
