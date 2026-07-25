"""
Root main.py - shim for Nixpacks auto-detect
Nixpacks looks for `main:app` at repo root, so we import the real app
from backend/main.py and re-export it.
"""
import sys
import os

# Ensure backend/ is on Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "backend"))

# Re-export the FastAPI app
from main import app  # noqa: F401, E402