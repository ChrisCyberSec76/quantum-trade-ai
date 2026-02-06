# System Architecture

## Overview

Quantum Trade AI is an AI-driven trading platform that orchestrates multiple autonomous agents to analyze markets, make decisions, and execute trades. The system is designed with clear boundaries, single execution authority, and persistent learning capabilities.

---

## Core Principles

### 1. Single Execution Authority

**One trading loop, multiple intelligence sources.**

- All trades execute through a single `SimplifiedTradingLoop`
- Multiple agents provide intelligence and signals
- Clear separation between analysis and execution
- Prevents conflicting orders and ensures consistency

### 2. Tiered Agent Architecture

**Parallel within tiers, sequential across tiers.**

```
TIER 1 (Fast Scan):     SCOUT, NEWS, SENTIMENT, CATALYST
                        ↓ (parallel execution)
TIER 2 (Analysis):      PATTERN, REGIME, EMA, QUANT
                        ↓ (parallel execution)
TIER 3 (Operations):    SCANNER, RISK, COMPLIANCE, REBALANCE
                        ↓ (parallel execution)
TIER 4 (Synthesis):     HARVEY
                        ↓ (sequential)
TIER 5 (Decision):      CIO
```

### 3. Memory-Driven Learning

**Persistent knowledge that improves over time.**

- CIO Memory Vault stores learnings from every trade
- Patterns are recognized and reinforced
- Mistakes are prevented through memory application
- System intelligence score increases with experience

### 4. Interface-Based Design

**Clean contracts between components.**

- Agents communicate through well-defined interfaces
- Services expose clear APIs
- Data flows through standardized schemas
- Easy to test, extend, and maintain

---

## System Components

### Frontend (React/Vite)

- **AI Hub**: Central dashboard for monitoring agents
- **BNAI Strategy**: Real-time scoring and decision visualization
- **AutoTrade Control**: Enable/disable trading loop
- **Cognitive Command Console**: Direct agent interaction

### Backend (FastAPI)

- **Trading Loop**: Single execution authority
- **Agent Orchestration**: Tier-based agent execution
- **Memory System**: Persistent learning and pattern recognition
- **Market Data Service**: Real-time and historical data

### AI Agents (14 Agents)

**Tier 1 - Fast Scanning:**
- SCOUT: Momentum and gap-up detection
- NEWS: Market-moving news analysis
- SENTIMENT: Social media and sentiment tracking
- CATALYST: Event and catalyst detection

**Tier 2 - Analysis:**
- PATTERN: Technical pattern recognition
- REGIME: Market regime identification
- EMA: Trend and momentum analysis
- QUANT: Quantitative factor analysis

**Tier 3 - Operations:**
- SCANNER: Market-wide scanning
- RISK: Risk management and position monitoring
- COMPLIANCE: Regulatory compliance checks
- REBALANCE: Portfolio rebalancing signals

**Tier 4 - Synthesis:**
- HARVEY: Narrative synthesis and high-level analysis

**Tier 5 - Decision:**
- CIO: Final decision-making and coordination

---

## Data Flow

```
Market Data Service
    │
    ├─→ Real-time candles → Strategy Engines
    └─→ Historical data → Backtesting
            │
            ▼
    Simplified Trading Loop
            │
            ├─→ Scanner → Candidates
            ├─→ BNAI Scoring → Eligible Symbols
            ├─→ EMA/VWAP Analysis → Entry Signals
            └─→ Exit Engine → Exit Signals
                    │
                    ▼
            Trade Execution Service
                    │
                    ▼
            Alpaca API (Orders)
```

---

## Key Design Patterns

### 1. Strategy Pattern

Multiple strategy engines (BNAI, EMA/VWAP) provide different perspectives on the same data. The trading loop selects the best signals.

### 2. Observer Pattern

Agents observe market data and emit reports. The CIO synthesizes these reports into decisions.

### 3. Command Pattern

Trading signals are encapsulated as commands that can be queued, validated, and executed.

### 4. Memory Pattern

The Memory Vault acts as a persistent store of learnings, allowing the system to improve over time.

---

## Security & Governance

- **Single Execution Point**: Prevents conflicting orders
- **Risk Checks**: Multiple layers of risk validation
- **Compliance Monitoring**: Regulatory rule enforcement
- **Memory Governance**: Access controls and retention policies

---

## Scalability Considerations

- **Async Processing**: Non-blocking agent execution
- **Caching**: In-memory cache for frequently accessed data
- **Rate Limiting**: API rate limits to prevent overload
- **Horizontal Scaling**: Stateless design allows multiple instances

---

## Production vs Showcase

**Production System:**
- Real market data connections
- Actual order execution
- Proprietary algorithms
- Full security implementation

**Showcase (This Repo):**
- Architecture documentation
- Interface definitions
- Mock implementations
- Design pattern demonstrations

---

## Further Reading

- [DIAGRAMS.md](DIAGRAMS.md) - Visual system flow diagrams
- [AI Board Meetings](AI_BOARD_MEETINGS.md) - How agents collaborate
- [CIO Memory Vault](CIO_MEMORY_VAULT.md) - Persistent learning system
- [Autonomous Agents](AUTONOMOUS_AGENTS.md) - Agent orchestration details
