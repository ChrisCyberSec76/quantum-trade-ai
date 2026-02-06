# System Architecture Diagrams

This document contains visual representations of the Quantum Trade AI system architecture using Mermaid diagrams. These diagrams illustrate system flow, agent orchestration, memory management, and decision-making processes.

---

## 🏗️ Overall System Architecture

```mermaid
graph TB
    subgraph "Frontend Layer"
        UI[AI Hub Dashboard]
        BNAI[BNAI Strategy View]
        CMD[Cognitive Command Console]
    end
    
    subgraph "Backend API Layer"
        API[FastAPI Backend]
        HEALTH[Health Endpoints]
        STATE[System State API]
        DECISIONS[Decisions API]
    end
    
    subgraph "Core Trading System"
        LOOP[Simplified Trading Loop]
        SCANNER[Market Scanner]
        BNAI_ENGINE[BNAI Strategy Engine]
        EXIT[Exit Engine]
    end
    
    subgraph "Agent Orchestration"
        ORCH[Agent Orchestrator]
        TIER1[Tier 1: Fast Scan]
        TIER2[Tier 2: Analysis]
        TIER3[Tier 3: Operations]
        TIER4[Tier 4: Synthesis]
        TIER5[Tier 5: Decision]
    end
    
    subgraph "Memory System"
        VAULT[CIO Memory Vault]
        APP[Memory Application Engine]
        CONSOL[Memory Consolidator]
    end
    
    subgraph "External Services"
        ALPACA[Alpaca API]
        MARKET[Market Data Service]
        BASE44[Base44 AI Platform]
    end
    
    UI --> API
    BNAI --> API
    CMD --> API
    
    API --> HEALTH
    API --> STATE
    API --> DECISIONS
    
    API --> LOOP
    LOOP --> SCANNER
    LOOP --> BNAI_ENGINE
    LOOP --> EXIT
    
    LOOP --> ORCH
    ORCH --> TIER1
    TIER1 --> TIER2
    TIER2 --> TIER3
    TIER3 --> TIER4
    TIER4 --> TIER5
    
    TIER5 --> VAULT
    VAULT --> APP
    VAULT --> CONSOL
    APP --> LOOP
    
    LOOP --> ALPACA
    SCANNER --> MARKET
    BNAI_ENGINE --> MARKET
    ORCH --> BASE44
    
    style LOOP fill:#e1f5ff
    style VAULT fill:#fff4e1
    style TIER5 fill:#ffe1f5
    style ORCH fill:#e1ffe1
```

---

## 🤖 Agent Tier Execution Flow

```mermaid
graph LR
    subgraph "TIER 1: Fast Scan (Parallel)"
        SCOUT[SCOUT<br/>Momentum Detection]
        NEWS[NEWS<br/>News Analysis]
        SENTIMENT[SENTIMENT<br/>Sentiment Tracking]
        CATALYST[CATALYST<br/>Event Detection]
    end
    
    subgraph "TIER 2: Analysis (Parallel)"
        PATTERN[PATTERN<br/>Pattern Recognition]
        REGIME[REGIME<br/>Regime Identification]
        EMA[EMA<br/>Trend Analysis]
        QUANT[QUANT<br/>Quantitative Analysis]
    end
    
    subgraph "TIER 3: Operations (Parallel)"
        SCANNER[SCANNER<br/>Market Scanning]
        RISK[RISK<br/>Risk Management]
        COMPLIANCE[COMPLIANCE<br/>Compliance Checks]
        REBALANCE[REBALANCE<br/>Portfolio Rebalancing]
    end
    
    subgraph "TIER 4: Synthesis (Sequential)"
        HARVEY[HARVEY<br/>Narrative Synthesis]
    end
    
    subgraph "TIER 5: Decision (Sequential)"
        CIO[CIO<br/>Final Decision]
    end
    
    SCOUT --> PATTERN
    NEWS --> PATTERN
    SENTIMENT --> REGIME
    CATALYST --> REGIME
    
    PATTERN --> SCANNER
    REGIME --> RISK
    EMA --> COMPLIANCE
    QUANT --> REBALANCE
    
    SCANNER --> HARVEY
    RISK --> HARVEY
    COMPLIANCE --> HARVEY
    REBALANCE --> HARVEY
    
    HARVEY --> CIO
    
    CIO -->|Decisions| EXEC[Trade Execution]
    CIO -->|Learnings| MEMORY[Memory Vault]
    
    style SCOUT fill:#ffcccc
    style NEWS fill:#ffcccc
    style SENTIMENT fill:#ffcccc
    style CATALYST fill:#ffcccc
    style PATTERN fill:#ccffcc
    style REGIME fill:#ccffcc
    style EMA fill:#ccffcc
    style QUANT fill:#ccffcc
    style SCANNER fill:#ccccff
    style RISK fill:#ccccff
    style COMPLIANCE fill:#ccccff
    style REBALANCE fill:#ccccff
    style HARVEY fill:#ffffcc
    style CIO fill:#ffccff
```

---

## 🧠 Memory Vault Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Creation: Agent Creates Memory
    
    Creation --> Deduplication: Check for Duplicates
    Deduplication --> Stored: Unique Memory
    Deduplication --> Merged: Duplicate Found
    
    Merged --> Stored: Consolidate
    
    Stored --> Active: Auto-Apply Enabled
    Stored --> Archived: Low Priority
    
    Active --> Application: Memory Application Engine
    Application --> Applied: Parameters Updated
    
    Applied --> Reinforcement: Successful Outcome
    Applied --> Deprioritized: Failed Outcome
    
    Reinforcement --> Active: Strengthen Memory
    Deprioritized --> Archived: Reduce Priority
    
    Archived --> Expired: Retention Period Ends
    Expired --> [*]: Cleanup
    
    note right of Creation
        Memory Types:
        - BATTLE_PLAN
        - LEARNING
        - ERROR_FIX
        - STRATEGY_ADJUSTMENT
        - RISK_RULE
        - PATTERN_INSIGHT
        - TRADE_OUTCOME
    end note
    
    note right of Application
        Converts to:
        - Confidence Boosts
        - Strategy Parameters
        - Agent Weights
        - Risk Filters
    end note
```

---

## 👥 AI Board Meeting Flow

```mermaid
sequenceDiagram
    participant CIO as CIO (Chair)
    participant SCOUT as SCOUT
    participant NEWS as NEWS
    participant RISK as RISK
    participant PATTERN as PATTERN
    participant HARVEY as HARVEY
    participant VAULT as Memory Vault
    
    CIO->>VAULT: Retrieve Battle Plan
    VAULT-->>CIO: Today's Strategy
    
    CIO->>SCOUT: Request Market Scan
    CIO->>NEWS: Request News Update
    CIO->>RISK: Request Risk Assessment
    CIO->>PATTERN: Request Pattern Analysis
    
    par Parallel Agent Reports
        SCOUT-->>CIO: Gap-up Candidates: NVDA, AMD
        NEWS-->>CIO: Overnight Developments
        RISK-->>CIO: Portfolio Status: 60% Allocation
        PATTERN-->>CIO: Technical Patterns Detected
    end
    
    CIO->>HARVEY: Request Synthesis
    HARVEY-->>CIO: Comprehensive Market Narrative
    
    CIO->>CIO: Synthesize All Inputs
    CIO->>CIO: Apply Memory Vault Learnings
    
    CIO->>SCOUT: Decision: BUY NVDA
    CIO->>RISK: Decision: HOLD AMD
    CIO->>PATTERN: Directive: Watch Breakouts
    
    CIO->>VAULT: Store Meeting Decisions
    VAULT-->>CIO: Memory Stored
    
    Note over CIO: Meeting Complete
```

---

## 📊 Complete Trading Decision Flow

```mermaid
flowchart TD
    START([Market Data Update]) --> SCAN[Market Scanner]
    
    SCAN --> CANDIDATES{Found<br/>Candidates?}
    CANDIDATES -->|No| WAIT[Wait for Next Update]
    CANDIDATES -->|Yes| BNAI_SCORE[BNAI Scoring Engine]
    
    BNAI_SCORE --> SCORE_CHECK{Score >=<br/>Threshold?}
    SCORE_CHECK -->|No| WAIT
    SCORE_CHECK -->|Yes| ENTRY_CHECK{Entry<br/>Ready?}
    
    ENTRY_CHECK -->|No| WAIT
    ENTRY_CHECK -->|Yes| ORCH[Agent Orchestration]
    
    ORCH --> TIER1_EXEC[Tier 1 Execution]
    TIER1_EXEC --> TIER2_EXEC[Tier 2 Execution]
    TIER2_EXEC --> TIER3_EXEC[Tier 3 Execution]
    TIER3_EXEC --> HARVEY_SYNTH[HARVEY Synthesis]
    HARVEY_SYNTH --> CIO_DECISION[CIO Decision]
    
    CIO_DECISION --> MEMORY_CHECK[Check Memory Vault]
    MEMORY_CHECK --> CONFIDENCE_BOOST{Confidence<br/>Boost?}
    CONFIDENCE_BOOST -->|Yes| ADJUST[Adjust Parameters]
    CONFIDENCE_BOOST -->|No| RISK_CHECK[Risk Validation]
    ADJUST --> RISK_CHECK
    
    RISK_CHECK --> RISK_OK{Risk<br/>OK?}
    RISK_OK -->|No| REJECT[Reject Trade]
    RISK_OK -->|Yes| COMPLIANCE_CHECK[Compliance Check]
    
    COMPLIANCE_CHECK --> COMPLIANCE_OK{Compliant?}
    COMPLIANCE_OK -->|No| REJECT
    COMPLIANCE_OK -->|Yes| EXECUTE[Execute Trade]
    
    EXECUTE --> MONITOR[Monitor Position]
    MONITOR --> EXIT_CHECK{Exit<br/>Signal?}
    EXIT_CHECK -->|No| MONITOR
    EXIT_CHECK -->|Yes| EXIT_TRADE[Exit Trade]
    
    EXIT_TRADE --> OUTCOME[Record Outcome]
    OUTCOME --> MEMORY_STORE[Store in Memory Vault]
    MEMORY_STORE --> WAIT
    
    REJECT --> WAIT
    WAIT --> START
    
    style START fill:#e1f5ff
    style EXECUTE fill:#ccffcc
    style REJECT fill:#ffcccc
    style MEMORY_STORE fill:#fff4e1
    style CIO_DECISION fill:#ffccff
```

---

## 🔄 Memory Application Engine Flow

```mermaid
graph TD
    MEMORY[Memory Retrieved] --> TYPE_CHECK{Memory<br/>Type?}
    
    TYPE_CHECK -->|STRATEGY_ADJUSTMENT| STRAT[Strategy Parameters]
    TYPE_CHECK -->|PATTERN_INSIGHT| PATTERN[Pattern Recognition]
    TYPE_CHECK -->|RISK_RULE| RISK[Risk Parameters]
    TYPE_CHECK -->|ERROR_FIX| ERROR[Error Prevention]
    TYPE_CHECK -->|LEARNING| LEARN[Learning Application]
    TYPE_CHECK -->|BATTLE_PLAN| PLAN[Battle Plan]
    
    STRAT --> ADJUST_STOP[Adjust Stop Loss]
    STRAT --> ADJUST_SIZE[Adjust Position Size]
    STRAT --> ADJUST_ENTRY[Adjust Entry Criteria]
    
    PATTERN --> BOOST_CONF[Boost Confidence]
    PATTERN --> ADD_FILTER[Add Pattern Filter]
    
    RISK --> REDUCE_SIZE[Reduce Position Size]
    RISK --> TIGHTEN_STOP[Tighten Stop Loss]
    RISK --> ADD_RISK_FILTER[Add Risk Filter]
    
    ERROR --> PREVENT_ERROR[Prevent Error Pattern]
    ERROR --> ADD_VALIDATION[Add Validation Rule]
    
    LEARN --> UPDATE_WEIGHTS[Update Agent Weights]
    LEARN --> REFINE_LOGIC[Refine Trading Logic]
    
    PLAN --> SET_PRIORITIES[Set Daily Priorities]
    PLAN --> FOCUS_SYMBOLS[Focus on Symbols]
    
    ADJUST_STOP --> APPLIED[Parameters Applied]
    ADJUST_SIZE --> APPLIED
    ADJUST_ENTRY --> APPLIED
    BOOST_CONF --> APPLIED
    ADD_FILTER --> APPLIED
    REDUCE_SIZE --> APPLIED
    TIGHTEN_STOP --> APPLIED
    ADD_RISK_FILTER --> APPLIED
    PREVENT_ERROR --> APPLIED
    ADD_VALIDATION --> APPLIED
    UPDATE_WEIGHTS --> APPLIED
    REFINE_LOGIC --> APPLIED
    SET_PRIORITIES --> APPLIED
    FOCUS_SYMBOLS --> APPLIED
    
    APPLIED --> TRADING_LOOP[Trading Loop Uses<br/>Updated Parameters]
    
    style MEMORY fill:#fff4e1
    style APPLIED fill:#ccffcc
    style TRADING_LOOP fill:#e1f5ff
```

---

## ⏰ Time-Aware Agent Execution

```mermaid
gantt
    title Daily Agent Execution Schedule
    dateFormat HH:mm
    axisFormat %H:%M
    
    section Pre-Market
    SCOUT Scan          :09:00, 5m
    NEWS Update         :09:00, 5m
    CATALYST Check      :09:00, 5m
    Board Meeting       :09:25, 5m
    
    section Market Hours
    SCOUT Continuous    :09:30, 6h30m
    NEWS Continuous     :09:30, 6h30m
    PATTERN Analysis    :09:30, 6h30m
    RISK Monitoring     :09:30, 6h30m
    CIO Decisions       :09:30, 6h30m
    
    section Post-Market
    Performance Review  :16:00, 30m
    Memory Consolidation:16:30, 30m
    Battle Plan Creation:17:00, 30m
```

---

## 🎯 Decision Synthesis Process

```mermaid
mindmap
  root((CIO Decision))
    Tier 1 Inputs
      SCOUT Candidates
      NEWS Impact
      SENTIMENT Score
      CATALYST Events
    Tier 2 Analysis
      PATTERN Signals
      REGIME Classification
      EMA Trends
      QUANT Scores
    Tier 3 Operations
      SCANNER Results
      RISK Assessment
      COMPLIANCE Status
      REBALANCE Needs
    Memory Vault
      Battle Plan
      Pattern Insights
      Risk Rules
      Error Fixes
    Synthesis
      HARVEY Narrative
      Confidence Score
      Risk-Adjusted Decision
    Final Decision
      BUY
      HOLD
      SELL
      SKIP
```

---

## 📈 System Data Flow

```mermaid
graph LR
    subgraph "Data Sources"
        ALPACA[Alpaca API]
        NEWS_API[News Feeds]
        SOCIAL[Social Media]
    end
    
    subgraph "Data Processing"
        MARKET_DATA[Market Data Service]
        INDICATORS[Technical Indicators]
        SCORING[BNAI Scoring]
    end
    
    subgraph "Agent Processing"
        AGENTS[14 AI Agents]
        ORCH[Orchestrator]
    end
    
    subgraph "Decision Layer"
        SYNTHESIS[Synthesis Engine]
        MEMORY[Memory Vault]
        DECISION[Decision Engine]
    end
    
    subgraph "Execution"
        VALIDATION[Risk/Compliance]
        EXECUTION[Trade Execution]
        MONITORING[Position Monitoring]
    end
    
    ALPACA --> MARKET_DATA
    NEWS_API --> MARKET_DATA
    SOCIAL --> MARKET_DATA
    
    MARKET_DATA --> INDICATORS
    INDICATORS --> SCORING
    
    SCORING --> AGENTS
    MARKET_DATA --> AGENTS
    
    AGENTS --> ORCH
    ORCH --> SYNTHESIS
    
    SYNTHESIS --> MEMORY
    MEMORY --> DECISION
    
    DECISION --> VALIDATION
    VALIDATION --> EXECUTION
    EXECUTION --> MONITORING
    
    MONITORING --> MEMORY
    
    style MARKET_DATA fill:#e1f5ff
    style MEMORY fill:#fff4e1
    style DECISION fill:#ffccff
    style EXECUTION fill:#ccffcc
```

---

## 🔐 Security & Governance Flow

```mermaid
graph TD
    TRADE[Trade Signal] --> SINGLE_AUTH{Single Execution<br/>Authority Check}
    
    SINGLE_AUTH -->|Pass| RISK_LAYER1[Risk Layer 1:<br/>Position Limits]
    SINGLE_AUTH -->|Fail| REJECT1[Reject: Multiple<br/>Execution Points]
    
    RISK_LAYER1 --> RISK_CHECK1{Within<br/>Limits?}
    RISK_CHECK1 -->|No| REJECT2[Reject: Exceeds<br/>Position Limit]
    RISK_CHECK1 -->|Yes| RISK_LAYER2[Risk Layer 2:<br/>Portfolio Risk]
    
    RISK_LAYER2 --> RISK_CHECK2{Portfolio<br/>Risk OK?}
    RISK_CHECK2 -->|No| REJECT3[Reject: Portfolio<br/>Risk Too High]
    RISK_CHECK2 -->|Yes| COMPLIANCE_LAYER[Compliance Layer:<br/>Regulatory Checks]
    
    COMPLIANCE_LAYER --> COMPLIANCE_CHECK{Compliant?}
    COMPLIANCE_CHECK -->|No| REJECT4[Reject: Compliance<br/>Violation]
    COMPLIANCE_CHECK -->|Yes| MEMORY_GOV[Memory Governance:<br/>Access Control]
    
    MEMORY_GOV --> MEMORY_CHECK{Memory<br/>Access OK?}
    MEMORY_CHECK -->|No| REJECT5[Reject: Memory<br/>Access Denied]
    MEMORY_CHECK -->|Yes| EXECUTE[Execute Trade]
    
    EXECUTE --> AUDIT[Audit Log]
    AUDIT --> MONITOR[Monitor Position]
    
    style SINGLE_AUTH fill:#ffe1f5
    style RISK_LAYER1 fill:#fff4e1
    style RISK_LAYER2 fill:#fff4e1
    style COMPLIANCE_LAYER fill:#e1f5ff
    style MEMORY_GOV fill:#e1ffe1
    style EXECUTE fill:#ccffcc
    style REJECT1 fill:#ffcccc
    style REJECT2 fill:#ffcccc
    style REJECT3 fill:#ffcccc
    style REJECT4 fill:#ffcccc
    style REJECT5 fill:#ffcccc
```

---

## 📝 Notes

- All diagrams use Mermaid syntax and render automatically on GitHub
- Diagrams illustrate the showcase architecture, not production implementation details
- Flow directions indicate data and control flow
- Color coding helps distinguish different system components
- These diagrams complement the written documentation in other files

---

## 🔗 Related Documentation

- [ARCHITECTURE.md](ARCHITECTURE.md) - Detailed system architecture
- [AUTONOMOUS_AGENTS.md](AUTONOMOUS_AGENTS.md) - Agent details and roles
- [CIO_MEMORY_VAULT.md](CIO_MEMORY_VAULT.md) - Memory system documentation
- [AI_BOARD_MEETINGS.md](AI_BOARD_MEETINGS.md) - Board meeting documentation
