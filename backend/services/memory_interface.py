"""
Memory Interface

Abstract interface for executive AI memory systems.
Production implementation includes:
- Long-term memory
- Governance rules
- Security constraints
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime


class CIOMemoryInterface(ABC):
    """
    Abstract interface for CIO Memory Vault.
    
    This interface mirrors the production memory system.
    Actual implementation is private and licensed.
    """
    
    @abstractmethod
    async def store(self, record: Dict[str, Any]) -> str:
        """
        Store a memory record.
        
        Args:
            record: Memory data with type, content, priority, etc.
            
        Returns:
            str: Memory ID
        """
        ...
    
    @abstractmethod
    async def retrieve(self, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Retrieve memories matching query.
        
        Args:
            query: Search criteria (type, symbol, priority, date range, etc.)
            
        Returns:
            list: Matching memory records
        """
        ...
    
    @abstractmethod
    async def apply(self, memory_id: str) -> Dict[str, Any]:
        """
        Apply a memory to system parameters.
        
        Args:
            memory_id: ID of memory to apply
            
        Returns:
            dict: Application result with changes made
        """
        ...
    
    @abstractmethod
    async def consolidate(self) -> Dict[str, Any]:
        """
        Consolidate memories (deduplication, pruning, strengthening).
        
        Returns:
            dict: Consolidation results (pruned, merged, strengthened counts)
        """
        ...
