"""
Data Schemas

Pydantic models defining API contracts and data structures.
These schemas mirror the production system's data contracts.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional
from datetime import datetime
from enum import Enum


class AgentStatus(str, Enum):
    """Agent execution status"""
    IDLE = "idle"
    ACTIVE = "active"
    READY = "ready"
    ERROR = "error"


class DecisionAction(str, Enum):
    """Trading decision actions"""
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"
    SKIP = "SKIP"


class MemoryType(str, Enum):
    """CIO Memory types"""
    BATTLE_PLAN = "BATTLE_PLAN"
    LEARNING = "LEARNING"
    ERROR_FIX = "ERROR_FIX"
    STRATEGY_ADJUSTMENT = "STRATEGY_ADJUSTMENT"
    RISK_RULE = "RISK_RULE"
    PATTERN_INSIGHT = "PATTERN_INSIGHT"
    TRADE_OUTCOME = "TRADE_OUTCOME"


class Decision(BaseModel):
    """AI agent decision model"""
    id: str
    timestamp: str
    agent: str
    action: DecisionAction
    symbol: str
    confidence: int = Field(ge=0, le=100)
    rationale: str
    factors: Dict[str, Any] = Field(default_factory=dict)


class DecisionResponse(BaseModel):
    """Response containing multiple decisions"""
    decisions: List[Decision]
    total: int
    note: Optional[str] = None


class MemoryRecord(BaseModel):
    """CIO Memory record model"""
    id: str
    memory_type: MemoryType
    title: str
    content: str
    priority: str  # CRITICAL, HIGH, MEDIUM, LOW
    source_agent: str
    created_date: str
    valid_from: Optional[str] = None
    valid_until: Optional[str] = None
    applied: bool = False
    auto_apply: bool = False
    related_symbols: List[str] = Field(default_factory=list)
    effectiveness_score: Optional[int] = Field(None, ge=0, le=100)


class AgentReport(BaseModel):
    """Agent analysis report model"""
    agent_id: str
    timestamp: str
    status: AgentStatus
    findings: Dict[str, Any] = Field(default_factory=dict)
    confidence: int = Field(ge=0, le=100)
    execution_time_ms: Optional[int] = None
