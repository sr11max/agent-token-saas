"""
Vercel entrypoint for token-saas FastAPI
- Vercel serverless wrapper
- All paths (/api/*, /, /health) routed to this handler
- /app serves static frontend via StaticFiles
"""
import sys
import os
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

# Vercel sets the cwd differently
os.chdir(str(Path(__file__).parent.parent / "backend"))

# Import the FastAPI app
from main import app

# Vercel needs the app object as the handler
handler = app