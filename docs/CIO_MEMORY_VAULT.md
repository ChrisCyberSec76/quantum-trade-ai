# CIO Memory Vault

## Overview

The CIO Memory Vault is a persistent learning system that stores insights, patterns, and learnings from trading activity. It enables the AI system to improve over time by remembering what worked, what didn't, and why.

---

## Core Concept

**"The system learns from every trade and applies that knowledge to future decisions."**

Unlike stateless AI systems, the Memory Vault provides:
- **Persistent Learning**: Knowledge survives across sessions
- **Pattern Recognition**: Identifies successful and failed patterns
- **Adaptive Behavior**: Adjusts parameters based on outcomes
- **Intelligence Growth**: System IQ score increases with experience

---

## Architecture

### Storage Layer

- **Vector Database**: Semantic search and similarity matching
- **Memory Scoring**: Relevance and effectiveness scoring
- **Retention Rules**: Automatic cleanup of old/ineffective memories
- **Agent Governance**: Access controls and usage policies

### Application Layer

- **Memory Application Engine**: Converts memories into active system parameters
- **Confidence Boosts**: Symbol-specific confidence adjustments
- **Agent Trust Recalibration**: Adjusts agent weights based on performance
- **Strategy Adjustments**: Modifies entry/exit rules based on learnings

---

## Memory Types

### 1. BATTLE_PLAN
Daily trading strategies and priorities. Created before market open.

**Example:**
```json
{
  "memory_type": "BATTLE_PLAN",
  "title": "Market Open Battle Plan - 2026-02-06",
  "content": "Focus on gap-up momentum. Watch for NVDA, AMD breakouts.",
  "priority": "HIGH",
  "auto_apply": true
}
```

### 2. LEARNING
General learnings from trades and market observations.

**Example:**
```json
{
  "memory_type": "LEARNING",
  "title": "Gap-up momentum works best before 10 AM",
  "content": "Analysis of 50 trades shows 70% win rate for gap-ups entered before 10 AM ET.",
  "priority": "MEDIUM"
}
```

### 3. ERROR_FIX
Solutions to prevent repeat mistakes.

**Example:**
```json
{
  "memory_type": "ERROR_FIX",
  "title": "Avoid low-volume breakouts",
  "content": "3 losses from low-volume breakouts. Add volume filter: min 1.5x average.",
  "priority": "HIGH",
  "auto_apply": true
}
```

### 4. STRATEGY_ADJUSTMENT
Parameter changes based on performance.

**Example:**
```json
{
  "memory_type": "STRATEGY_ADJUSTMENT",
  "title": "Tighten stop loss after losses",
  "content": "After -$500 day, reduce stop loss from -2% to -1.5%",
  "priority": "HIGH",
  "metrics": {
    "stop_loss_percentage": -1.5
  }
}
```

### 5. RISK_RULE
Risk management rules and alerts.

**Example:**
```json
{
  "memory_type": "RISK_RULE",
  "title": "Reduce exposure after loss",
  "content": "Lost $500 yesterday. Reduce max position size to 50%.",
  "priority": "CRITICAL",
  "auto_apply": true
}
```

### 6. PATTERN_INSIGHT
Successful pattern recognition.

**Example:**
```json
{
  "memory_type": "PATTERN_INSIGHT",
  "title": "NVDA gap-up pattern",
  "content": "NVDA gap-ups >3% with volume >2x average have 80% win rate.",
  "related_symbols": ["NVDA"],
  "effectiveness_score": 85
}
```

### 7. TRADE_OUTCOME
Individual trade results for learning.

**Example:**
```json
{
  "memory_type": "TRADE_OUTCOME",
  "title": "WIN: AAPL +$250",
  "content": "Profitable trade on AAPL. Strategy: MOMENTUM. Entry: $150.",
  "related_symbols": ["AAPL"],
  "metrics": {
    "profit_loss": 250,
    "strategy": "MOMENTUM"
  }
}
```

---

## Memory Lifecycle

### 1. Creation
- Agents create memories after trades, analysis, or errors
- Deduplication checks prevent duplicates
- Auto-assigns validity dates (default: next market open + 24 hours)

### 2. Consolidation
- Memory Consolidator Agent runs periodically
- Deduplicates similar memories
- Prunes expired/ineffective memories
- Strengthens frequently-used memories

### 3. Application
- High-priority memories with `auto_apply: true` are automatically processed
- Memory Application Engine converts memories into system parameters
- Updates confidence thresholds, strategy parameters, agent weights

### 4. Reinforcement
- Successful memories are reinforced when referenced
- Failed memories are deprioritized or removed
- Pattern memories are consolidated when multiple similar patterns exist

---

## Intelligence Score

The Memory Vault calculates an Intelligence Score (0-100) based on:

- **Memory Effectiveness**: How well memories performed when applied
- **Win Rate**: Success rate of trades influenced by memories
- **Pattern Recognition**: Accuracy of pattern memories
- **Learning Velocity**: Rate of new memory creation
- **Memory Reinforcement**: Frequency of successful memory usage

**Score Ranges:**
- 0-40: Learning phase
- 40-60: Building knowledge
- 60-80: Experienced
- 80-100: Expert level

---

## How Memories Affect Trading

### 1. Confidence Boosts
If a memory contains a high `whale_probability` for a symbol, it adds a confidence boost:
- 80% whale probability → +12% confidence boost
- Max boost: +20%

### 2. Strategy Adjustments
Memories can modify:
- Stop loss percentages
- Position sizes
- Entry criteria
- Exit rules

### 3. Agent Trust Recalibration
Memories analyze agent performance and adjust weights:
- Win rate ≥ 70% → 1.4x weight
- Win rate ≥ 60% → 1.2x weight
- Win rate < 40% → 0.6x weight

### 4. Risk Filters
Memories can add filters to avoid repeat mistakes:
- "Avoid low-volume breakouts"
- "Skip symbols with recent losses"
- "Require higher confidence after losses"

---

## Example Flow

1. **Trade Completes**: Loss of $500 on TSLA
2. **Memory Created**:
   ```json
   {
     "memory_type": "RISK_RULE",
     "title": "Risk Alert: TSLA at -2.5%",
     "content": "Position hit -2.5% loss. Tighten entry criteria.",
     "related_symbols": ["TSLA"],
     "auto_apply": true,
     "priority": "HIGH"
   }
   ```
3. **Memory Consolidator Processes**: Validates and stores
4. **Memory Application Engine Applies**:
   - Reduces max position size for TSLA to 50%
   - Adds tighter entry criteria filter
5. **Next TSLA Trade**: Uses adjusted parameters

---

## Key Benefits

1. **Persistent Learning**: Knowledge survives across sessions
2. **Mistake Prevention**: Error fixes auto-apply to prevent repeats
3. **Adaptive Behavior**: System adjusts to market conditions
4. **Symbol Intelligence**: Symbol-specific learnings improve over time
5. **Agent Performance Tracking**: Trust weights based on results

---

## Interface

See `backend/services/memory_interface.py` for the abstract interface definition.

**Key Methods:**
- `store(record)`: Store a memory
- `retrieve(query)`: Search memories
- `apply(memory_id)`: Apply memory to system
- `consolidate()`: Run consolidation process

---

## Production Implementation

**Production system includes:**
- Vector database for semantic search
- Real-time memory scoring and ranking
- Automatic retention and cleanup policies
- Agent access governance
- Security constraints and validation

**This showcase demonstrates:**
- Interface design
- Memory types and structure
- Application patterns
- Intelligence scoring concept
