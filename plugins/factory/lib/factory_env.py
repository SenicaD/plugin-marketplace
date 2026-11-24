"""Shared setup for the factory scripts.

The scripts ship inside the plugin; all state lives in the project that runs
them. REPO is the project's main checkout, found from the current directory
through git's common dir, so it is the same from the main checkout and from a
job's worktree. config.json in <repo>/factory/ overrides the plugin defaults
key by key.
"""

import json
import subprocess
import sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1]
PLUGIN_BIN = PLUGIN / "bin"


def _repo():
    res = subprocess.run(["git", "rev-parse", "--path-format=absolute", "--git-common-dir"],
                         capture_output=True, text=True)
    if res.returncode != 0:
        print("factory: run this from inside a git repository", file=sys.stderr)
        sys.exit(1)
    return Path(res.stdout.strip()).parent


REPO = _repo()
FACTORY = REPO / "factory"


def _config():
    cfg = json.loads((PLUGIN / "defaults" / "config.json").read_text())
    mine = FACTORY / "config.json"
    if mine.exists():
        cfg.update(json.loads(mine.read_text()))
    return cfg


CONFIG = _config()
