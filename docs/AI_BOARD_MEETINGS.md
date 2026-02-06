# AI Board Meetings

## Overview

AI Board Meetings are collaborative sessions where multiple AI agents discuss market conditions, review performance, and make strategic decisions. Think of it as a virtual boardroom where each agent has a voice and contributes their expertise.

---

## Concept

**"Multiple AI agents collaborate like a board of directors, each bringing unique perspectives to trading decisions."**

Unlike single-agent systems, Board Meetings enable:
- **Collaborative Decision-Making**: Multiple agents contribute insights
- **Time-Aware Context**: Different meeting types for different times of day
- **Voice Interaction**: Agents speak their reports (optional)
- **Consensus Building**: Agents debate and reach decisions together

---

## Meeting Types

### 1. Pre-Market Planning (Before 9:30 AM ET)
**Purpose**: Strategy planning for today's session

**Agenda:**
- Review overnight news and catalysts
- Analyze pre-market movers
- Set daily priorities and focus areas
- Review battle plan from Memory Vault

**Participants:**
- CIO (Chair)
- SCOUT (Market opportunities)
- NEWS (Overnight developments)
- CATALYST (Events today)
- HARVEY (Synthesis)

### 2. Live Trading Session (9:30 AM - 4:00 PM ET)
**Purpose**: Real-time performance analysis

**Agenda:**
- Review active positions
- Discuss new opportunities
- Address risk concerns
- Adjust strategy if needed

**Participants:**
- All active agents
- Focus on RISK, COMPLIANCE, REGIME

### 3. Extended Hours Review (4:00 PM - 8:00 PM ET)
**Purpose**: End of day analysis

**Agenda:**
- Review today's performance
- Analyze wins and losses
- Identify learning opportunities
- Prepare for tomorrow

**Participants:**
- CIO (Chair)
- RISK (Position review)
- PATTERN (Pattern analysis)
- HARVEY (Narrative)

### 4. Post-Market Review (After 8:00 PM ET)
**Purpose**: Daily performance review and learning

**Agenda:**
- Calculate win rate and P&L
- Grade the day (A/B/C/D/F)
- Store learnings in Memory Vault
- Generate battle plan for tomorrow

**Participants:**
- All agents
- Focus on learning and improvement

---

## Meeting Flow

### 1. Opening
CIO opens the meeting with a time-appropriate greeting:
- Morning: "Good morning team. Rise and shine, markets open soon."
- Evening: "Good evening team. Markets just closed. Time to review today's performance."

### 2. Agent Reports
Each agent presents their findings:
- **SCOUT**: "Found 3 gap-up candidates: NVDA, AMD, META. All have volume >2x average."
- **NEWS**: "Overnight: Fed minutes released. 2 FDA approvals. Market sentiment bullish."
- **RISK**: "Portfolio stress: max drawdown -2.1%. All positions within limits."
- **PATTERN**: "Closing data: 5 breakouts detected. SPY above 20 EMA."

### 3. Discussion
Agents interact and discuss:
- **CIO**: "SCOUT, what's your confidence on NVDA?"
- **SCOUT**: "High confidence. Gap-up >3%, volume surge, pre-market momentum."
- **RISK**: "CIO, we're already at 80% allocation. Should we wait?"
- **CIO**: "Good point. Let's prioritize top 2 opportunities only."

### 4. Decisions
CIO synthesizes and makes decisions:
- **Decision 1**: "BUY NVDA - High confidence gap-up play"
- **Decision 2**: "HOLD AMD - Monitor for entry"
- **Decision 3**: "EXIT TSLA - Risk limit reached"

### 5. Directives
CIO issues directives for next steps:
- "SCOUT: Continue scanning for momentum plays"
- "RISK: Monitor all positions closely"
- "PATTERN: Watch for breakout confirmations"

### 6. Closing
CIO closes with summary:
- "Good work team. We're up $250 today. Stay disciplined."

---

## Agent Roles

### CIO (Chief Investment Officer)
- **Role**: Chair and final decision maker
- **Responsibilities**: Synthesize inputs, make decisions, coordinate agents
- **Voice**: Authoritative, strategic

### SCOUT
- **Role**: Opportunity finder
- **Responsibilities**: Scan for momentum, gap-ups, volume surges
- **Voice**: Energetic, opportunistic

### NEWS
- **Role**: Information gatherer
- **Responsibilities**: Track market-moving news, SEC filings, events
- **Voice**: Informative, factual

### RISK
- **Role**: Risk manager
- **Responsibilities**: Monitor positions, enforce limits, warn of dangers
- **Voice**: Cautious, protective

### PATTERN
- **Role**: Pattern recognizer
- **Responsibilities**: Identify technical patterns, breakouts, setups
- **Voice**: Analytical, precise

### HARVEY
- **Role**: Synthesizer
- **Responsibilities**: Create narratives, high-level analysis
- **Voice**: Thoughtful, comprehensive

---

## Example Meeting Transcript

```
[9:25 AM ET - Pre-Market Planning]

CIO: "Good morning team. Markets open in 5 minutes. Let's review the plan."

SCOUT: "Pre-market scan complete. Top movers: NVDA +2.5%, AMD +1.8%, META +1.2%. 
        All have volume >2x average. NVDA looks strongest."

NEWS: "Overnight developments: Fed minutes released, dovish tone. 2 biotech FDA 
       approvals. Market sentiment shifted bullish overnight."

CATALYST: "Today's events: NVDA earnings after close. AMD product launch at 11 AM. 
          META has no major catalysts today."

RISK: "Portfolio status: 2 open positions, 60% allocation. Max drawdown -1.2%. 
       We have room for 1-2 more positions."

PATTERN: "Technical analysis: NVDA breaking above resistance. AMD in ascending 
          triangle. META consolidating."

HARVEY: "Synthesis: Strong pre-market setup. NVDA is the clear leader with 
         earnings catalyst. AMD secondary play. META less compelling."

CIO: "Excellent analysis team. Decision: Focus on NVDA as primary opportunity. 
      Monitor AMD for confirmation. Skip META for now. SCOUT, continue scanning. 
      RISK, watch allocation. Let's have a great day."

[Meeting ends]
```

---

## Technical Implementation

### Meeting State
- **Active**: Meeting in progress
- **Phase**: opening, reports, discussion, decisions, closing
- **Transcript**: Full conversation log
- **Decisions**: List of decisions made
- **Directives**: Actions assigned to agents

### Voice Integration
- Each agent has a unique voice (configurable)
- Text-to-speech for agent reports
- Optional voice interaction
- Can be muted for silent mode

### Persistence
- Meeting state persists across navigation
- Transcript saved to session storage
- Decisions stored in Memory Vault
- Can resume interrupted meetings

---

## Benefits

1. **Collaborative Intelligence**: Multiple perspectives improve decisions
2. **Transparency**: Full visibility into decision-making process
3. **Learning**: Meetings generate memories for future reference
4. **Accountability**: Each agent's contribution is recorded
5. **Adaptability**: Different meeting types for different contexts

---

## Interface

See `backend/services/agent_interface.py` for agent interface definitions.

**Key Concepts:**
- Agent collaboration protocols
- Decision synthesis patterns
- Voice interaction design
- State management

---

## Production Implementation

**Production system includes:**
- Real-time agent collaboration
- Voice synthesis and recognition
- Natural language processing
- Decision tracking and validation
- Memory integration

**This showcase demonstrates:**
- Meeting structure and flow
- Agent roles and interactions
- Decision-making patterns
- Time-aware context switching
