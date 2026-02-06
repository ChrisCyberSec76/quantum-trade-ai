"""
Decisions Endpoint - MOCK

This interface mirrors the production AI decision system.
Actual implementation is private and licensed.

NOTE: This endpoint returns MOCK decisions for demonstration purposes only.
"""

from fastapi import APIRouter
from datetime import datetime
from typing import List, Dict, Any
from backend.models.schemas import Decision, DecisionResponse

router = APIRouter()


@router.get("/decisions", response_model=DecisionResponse)
async def get_decisions(limit: int = 10) -> DecisionResponse:
    """
    Get recent AI agent decisions (MOCK).
    
    Production implementation includes:
    - Real-time CIO decisions
    - Agent collaboration results
    - Memory-influenced choices
    - Risk assessments
    
    Args:
        limit: Maximum number of decisions to return
        
    Returns:
        DecisionResponse: Mock decision data
    """
    # Mock decision data for demonstration
    mock_decisions = [
        Decision(
            id=f"decision_{i}",
            timestamp=datetime.utcnow().isoformat(),
            agent="CIO",
            action="BUY",
            symbol="AAPL",
            confidence=85,
            rationale="Mock decision demonstrating decision structure",
            factors={
                "trend_confirmation": True,
                "momentum": True,
                "volume_surge": True
            }
        )
        for i in range(min(limit, 5))
    ]
    
    return DecisionResponse(
        decisions=mock_decisions,
        total=len(mock_decisions),
        note="This is mock data for demonstration. Production system provides real AI decisions."
    )
