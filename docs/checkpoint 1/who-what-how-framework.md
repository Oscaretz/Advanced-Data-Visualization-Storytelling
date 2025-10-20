# WHO–WHAT–HOW Framework: Audience, Action, and Data Strategy

## 1. Storytelling Framework Overview
This framework defines the **narrative and analytical intent** of the cryptocurrency spatiotemporal project. It bridges the technical results with an audience-centered perspective, clarifying **who** the research is for, **what** action or insight it aims to drive, and **how** the data supports those conclusions.

---

## 2. WHO – Audience

### Primary Audience
**Retail Investors (Ages 25–40)**  
Young professionals with medium technical literacy and growing interest in digital finance. They seek to understand whether cryptocurrencies are viable long-term investments and how market risk behaves over time.  
- **Motivation:** Personal wealth growth, curiosity about decentralized finance.  
- **Challenge:** Limited access to analytical tools for understanding volatility and adoption signals.  
- **Need:** Evidence-based insights on market uncertainty and behavioral indicators.

### Secondary Audience
**Financial Advisors and Market Analysts**  
Professionals seeking to interpret behavioral and financial dynamics for clients or institutional reports.  
- **Motivation:** Data-driven advisory, diversification strategies.  
- **Challenge:** Integrating public attention data (Google Trends) with market indicators.  
- **Need:** Analytical validation that connects social sentiment with price volatility patterns.

---

## 3. WHAT – Desired Action

The goal is to enable both audiences to **make informed decisions about cryptocurrency exposure** in their portfolios and analyses.  

Specifically, the project encourages the following actions:  
1. **Risk Evaluation:** Understand the high volatility and random walk nature of crypto assets.  
2. **Adoption Monitoring:** Track geographic search interest as an indicator of global awareness.  
3. **Signal Detection:** Identify when public attention precedes market movements.  

This empowers investors and analysts to interpret **behavioral signals** as early indicators of market shifts, rather than relying solely on price trends.

---

## 4. HOW – Data as Evidence

The analytical framework relies on quantitative and spatial data to substantiate behavioral and financial insights:

| Evidence Type | Dataset | Analytical Method | Insight |
|----------------|----------|-------------------|----------|
| **Time Series Behavior** | `prices_with_metrics.csv` | ADF tests, ACF/PACF, log returns | Prices behave as random walks — high uncertainty and unpredictability. |
| **Volatility Clustering** | `prices_with_metrics.csv` | Rolling variance, volatility metrics | High-volatility periods persist; risk is cyclical and self-reinforcing. |
| **Geographic Adoption** | `trends_enriched.csv` | Choropleth mapping, regional aggregation | Global interest is increasing but uneven, concentrated in specific regions. |
| **Lead–Lag Dynamics** | `integrated_data.csv` | Cross-correlation (CCF) analysis | In several cases, public attention **precedes** volatility spikes — potential early signal. |

---

## 5. Data Story Synthesis

The findings construct a coherent data story:  
- Cryptocurrencies remain **highly speculative assets**, with unpredictable price trajectories.  
- Yet, **volatility is not random in its intensity** — clusters of risk emerge and persist.  
- Meanwhile, **geographic data reveals uneven adoption**, showing cultural and economic asymmetries.  
- Importantly, **behavioral interest data may anticipate market turbulence**, offering predictive insight for attentive observers.  

This synthesis positions the study as both a **behavioral-financial analysis** and a **strategic tool for market awareness**.

---

## 6. Strategic Implications

For retail investors, the takeaway is **caution with opportunity**: cryptocurrencies offer innovation and growth potential but demand awareness of volatility cycles and behavioral momentum.  

For analysts and advisors, the project highlights the importance of integrating **alternative data sources** (like Google Trends) to enhance forecasting and market interpretation models.

---

**Members of the Team Project:**
David
Oscar
Moi
Braulio
Gerardo
Luis 

**Last Updated:** October 2025   
