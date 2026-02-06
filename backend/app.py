"""
FastAPI Entry Point - Public Showcase Layer

This interface mirrors the production AI agent system.
Actual implementation is private and licensed.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api import health, system_state, decisions

app = FastAPI(
    title="Quantum Trade AI - Showcase API",
    description="Public-facing interface demonstrating system architecture",
    version="1.0.0-showcase"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Showcase only - production uses specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(health.router, prefix="/api", tags=["Health"])
app.include_router(system_state.router, prefix="/api", tags=["System"])
app.include_router(decisions.router, prefix="/api", tags=["Decisions"])


@app.get("/")
async def root():
    """Root endpoint - API information"""
    return {
        "name": "Quantum Trade AI - Showcase API",
        "description": "Public-facing interface demonstrating system architecture",
        "version": "1.0.0-showcase",
        "note": "This interface mirrors the production AI agent system. Actual implementation is private and licensed.",
        "endpoints": {
            "health": "/api/health",
            "system_state": "/api/system/state",
            "decisions": "/api/decisions"
        }
    }
