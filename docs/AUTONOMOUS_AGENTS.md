# Autonomous Agents

## Overview

The system orchestrates **14 autonomous AI agents** that work together to analyze markets, identify opportunities, manage risk, and make trading decisions. Each agent has a specific role and expertise, and they collaborate through a tiered architecture.

---

## Agent Architecture

### Tier-Based Execution

Agents are organized into 5 tiers, executed sequentially:

```
TIER 1 (Fast Scan)     →  TIER 2 (Analysis)     →  TIER 3 (Operations)
SCOUT, NEWS,           →  PATTERN, REGIME,      →  SCANNER, RISK,
SENTIMENT, CATALYST    →  EMA, QUANT            →  COMPLIANCE, REBALANCE
     ↓                        ↓                        ↓
     └────────────────────────┴────────────────────────┘
                              ↓
                    TIER 4 (Synthesis)
                              HARVEY
                              ↓
                    TIER 5 (Decision)
                              CIO
```

**Execution Pattern:**
- **Within Tier**: Agents run in parallel
- **Across Tiers**: Sequential (Tier 1 → Tier 2 → Tier 3 → Tier 4 → Tier 5)
- **Timeout**: Each tier has a timeout (Tier 1: 60s, Tier 2: 120s, etc.)

---

## The 14 Agents

### TIER 1: Fast Scanning (Parallel)

#### SCOUT
**Role**: Momentum and gap-up detection  
**Mission**: Find explosive moves before they happen  
**Output**: List of candidates with momentum scores  
**Frequency**: Every 5 minutes during market hours

**Key Functions:**
- Scan Finviz for gap-ups
- Analyze Alpaca most actives
- Check after-hours movers
- Score candidates (0-110)

#### NEWS
**Role**: Market-moving news analysis  
**Mission**: Identify news that will move markets  
**Output**: News alerts with impact scores  
**Frequency**: Every 5 minutes

**Key Functions:**
- Monitor financial news feeds
- Analyze SEC filings
- Track earnings announcements
- Score news impact (0-100)

#### SENTIMENT
**Role**: Social media and sentiment tracking  
**Mission**: Gauge market mood and social buzz  
**Output**: Sentiment scores and trending tickers  
**Frequency**: Every 10 minutes

**Key Functions:**
- Monitor Twitter/X mentions
- Track Reddit discussions
- Analyze Google Trends
- Calculate sentiment scores

#### CATALYST
**Role**: Event and catalyst detection  
**Mission**: Find events that will cause price movement  
**Output**: Catalyst alerts with timing  
**Frequency**: Every 5 minutes

**Key Functions:**
- Track earnings dates
- Monitor FDA decisions
- Watch for product launches
- Identify economic events

---

### TIER 2: Analysis (Parallel)

#### PATTERN
**Role**: Technical pattern recognition  
**Mission**: Identify chart patterns and setups  
**Output**: Pattern signals with confidence  
**Frequency**: Every 15 minutes

**Key Functions:**
- Detect breakouts
- Identify support/resistance
- Recognize chart patterns
- Score pattern strength

#### REGIME
**Role**: Market regime identification  
**Mission**: Determine current market environment  
**Output**: Regime classification (RISK_ON, RISK_OFF, etc.)  
**Frequency**: Every 10 minutes

**Key Functions:**
- Analyze VIX levels
- Measure market breadth
- Track sector rotation
- Classify regime

#### EMA
**Role**: Trend and momentum analysis  
**Mission**: Identify trend direction and strength  
**Output**: EMA signals and trend confirmation  
**Frequency**: Every 10 minutes

**Key Functions:**
- Calculate EMA crossovers
- Measure trend strength
- Identify pullback opportunities
- Score trend quality

#### QUANT
**Role**: Quantitative factor analysis  
**Mission**: Analyze statistical factors and ML signals  
**Output**: Quant scores and factor rankings  
**Frequency**: Every 30 minutes

**Key Functions:**
- Run factor models
- Calculate ML predictions
- Analyze backtest results
- Score quantitative strength

---

### TIER 3: Operations (Parallel)

#### SCANNER
**Role**: Market-wide scanning  
**Mission**: Find opportunities across entire market  
**Output**: Scanned candidates with scores  
**Frequency**: Every 10 minutes

**Key Functions:**
- Scan all liquid stocks
- Filter by criteria
- Rank by opportunity
- Generate watchlist

#### RISK
**Role**: Risk management and position monitoring  
**Mission**: Protect capital and manage exposure  
**Output**: Risk alerts and position recommendations  
**Frequency**: Every 30 minutes

**Key Functions:**
- Monitor open positions
- Calculate portfolio risk
- Check position limits
- Generate exit signals

#### COMPLIANCE
**Role**: Regulatory compliance checks  
**Mission**: Ensure all trades meet regulatory requirements  
**Output**: Compliance status and warnings  
**Frequency**: Every 30 minutes

**Key Functions:**
- Check pattern day trader rules
- Validate position limits
- Monitor trade frequency
- Ensure regulatory compliance

#### REBALANCE
**Role**: Portfolio rebalancing signals  
**Mission**: Optimize portfolio allocation  
**Output**: Rebalancing recommendations  
**Frequency**: Every 30 minutes

**Key Functions:**
- Analyze current allocation
- Calculate target allocation
- Identify rebalancing needs
- Generate rebalance signals

---

### TIER 4: Synthesis (Sequential)

#### HARVEY
**Role**: Narrative synthesis and high-level analysis  
**Mission**: Create comprehensive market narrative  
**Output**: Synthesis report with high-conviction ideas  
**Frequency**: Every hour

**Key Functions:**
- Synthesize all agent inputs
- Create market narrative
- Identify high-conviction opportunities
- Generate execution recommendations

---

### TIER 5: Decision (Sequential)

#### CIO
**Role**: Final decision-making and coordination  
**Mission**: Make final trading decisions based on all inputs  
**Output**: BUY/HOLD/SELL decisions with rationale  
**Frequency**: Every 15 minutes (or on-demand)

**Key Functions:**
- Synthesize all tier results
- Apply Memory Vault learnings
- Make final decisions
- Coordinate agent execution

---

## Agent Communication

### Report Structure

Each agent produces a report with:
```json
{
  "agent_id": "SCOUT",
  "timestamp": "2026-02-06T09:35:00Z",
  "status": "complete",
  "findings": {
    "candidates": ["NVDA", "AMD", "META"],
    "scores": {"NVDA": 85, "AMD": 72, "META": 68}
  },
  "confidence": 88,
  "summary": "Found 3 gap-up candidates. NVDA strongest."
}
```

### Agent Dependencies

Some agents depend on others:
- **CIO** depends on all other agents
- **HARVEY** depends on Tier 1-3 agents
- **RISK** depends on position data
- **PATTERN** depends on market data

### Progress Tracking

Each agent reports progress (0-100%):
- 0%: Not started
- 50%: In progress
- 90%: Almost complete
- 100%: Complete

---

## Orchestration Flow

### 1. Overnight Intelligence (4 PM - 9:30 AM ET)

**Purpose**: Prepare for next trading day

**Flow:**
1. Tier 1 agents scan overnight developments
2. Tier 2 agents analyze patterns and regime
3. Tier 3 agents check risk and compliance
4. HARVEY synthesizes overnight intelligence
5. CIO creates battle plan for market open

### 2. Market Hours (9:30 AM - 4:00 PM ET)

**Purpose**: Active trading and monitoring

**Flow:**
1. All agents run continuously at their intervals
2. SCOUT finds opportunities
3. Other agents validate and analyze
4. CIO makes real-time decisions
5. RISK monitors positions

### 3. Post-Market (After 4 PM ET)

**Purpose**: Review and learning

**Flow:**
1. Agents review day's performance
2. Store learnings in Memory Vault
3. Generate battle plan for tomorrow
4. Consolidate memories

---

## Agent Capabilities

### Individual Agent Skills

Each agent has specialized capabilities:
- **Data Analysis**: Process market data
- **Pattern Recognition**: Identify patterns
- **Risk Assessment**: Evaluate risk
- **Decision Making**: Make recommendations

### Collaborative Intelligence

Agents collaborate to:
- **Validate Signals**: Multiple agents confirm opportunities
- **Cross-Reference**: Agents check each other's findings
- **Synthesize**: Combine multiple perspectives
- **Learn Together**: Share learnings through Memory Vault

---

## Memory Integration

Agents interact with the Memory Vault:

1. **Store Learnings**: Agents create memories after analysis
2. **Retrieve Context**: Agents query memories for relevant context
3. **Apply Learnings**: Agents use memories to improve decisions
4. **Reinforce Patterns**: Successful patterns are reinforced

---

## Interface

See `backend/services/agent_interface.py` for agent interface definitions.

**Key Methods:**
- `analyze(context)`: Analyze market context
- `decide(analysis)`: Make decision based on analysis
- `learn(outcome)`: Learn from trade outcome

---

## Production Implementation

**Production system includes:**
- Real-time agent execution
- Base44 function integration
- Parallel processing within tiers
- Sequential coordination across tiers
- Progress tracking and reporting
- Error handling and recovery

**This showcase demonstrates:**
- Agent architecture and roles
- Tier-based execution pattern
- Agent communication protocols
- Orchestration flow

---

## Benefits

1. **Specialized Expertise**: Each agent focuses on one area
2. **Parallel Processing**: Multiple agents work simultaneously
3. **Collaborative Intelligence**: Agents validate and enhance each other
4. **Scalable Architecture**: Easy to add new agents
5. **Fault Tolerance**: One agent failure doesn't stop the system
