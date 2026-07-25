"""
Root main.py - shim for Nixpacks auto-detect.
Nixpacks looks for `main:app` at repo root, so we import the real
FastAPI app from the backend/ package and re-export it as `app`.
"""
import sys
import os

# Make sure backend/ is importable as a package
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the real app from the backend package
from backend.main import app  # noqa: F401, E402