"""Compatibility loaders — canonical implementations live in simulate.py."""

from .simulate import list_fixture_ids, list_framework_ids, load_fixture, load_framework
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = ROOT / "results"

__all__ = [
    "RESULTS_DIR",
    "list_fixture_ids",
    "list_framework_ids",
    "load_fixture",
    "load_framework",
]
