"""
Agent Interface

Abstract interface for autonomous AI agent systems.
Production implementation includes:
- Long-term memory
- Governance rules
- Security constraints
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional


class AgentInterface(ABC):
    """
    Abstract interface for AI trading agents.
    
    This interface mirrors the production AI agent system.
    Actual implementation is private and licensed.
    """
    
    @abstractmethod
    async def analyze(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze market context and produce insights.
        
        Args:
            context: Market data, positions, memory context
            
        Returns:
            dict: Analysis results with confidence scores
        """
        ...
    
    @abstractmethod
    async def decide(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """
        Make trading decision based on analysis.
        
        Args:
            analysis: Results from analyze() method
            
        Returns:
            dict: Decision with action, symbol, confidence, rationale
        """
        ...
    
    @abstractmethod
    async def learn(self, outcome: Dict[str, Any]) -> None:
        """
        Learn from trade outcome and update memory.
        
        Args:
            outcome: Trade result with P&L, exit reason, etc.
        """
        ...


class AgentOrchestratorInterface(ABC):
    """
    Abstract interface for orchestrating multiple agents.
    
    Production implementation includes:
    - Tier-based execution
    - Parallel processing within tiers
    - Sequential coordination across tiers
    - Memory consolidation
    """
    
    @abstractmethod
    async def execute_tier(self, tier: int, agents: List[str]) -> Dict[str, Any]:
        """
        Execute agents in a tier (parallel within tier).
        
        Args:
            tier: Tier number (1-5)
            agents: List of agent IDs in this tier
            
        Returns:
            dict: Results from all agents in tier
        """
        ...
    
    @abstractmethod
    async def synthesize(self, tier_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Synthesize results from multiple tiers.
        
        Args:
            tier_results: Results from all tiers
            
        Returns:
            dict: Final synthesis and decision
        """
        ...
