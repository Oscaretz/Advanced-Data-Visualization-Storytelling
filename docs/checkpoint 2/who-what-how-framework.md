# Who-What-How Framework
## Audience, Action, and Data Strategy

---

## WHO - Target Audience

### Primary Audience
**Investors and Stakeholders**
- **Profile**: Business executives and financial decision-makers evaluating data analysis capabilities
- **Technical Level**: Low to moderate technical understanding
- **Priority**: ROI, strategic insights, business impact
- **Attention Span**: 10-15 minutes presentation time
- **Decision Power**: High - influence funding and resource allocation

### Secondary Audience
**Technical Reviewers**
- **Profile**: Data analysts, data scientists, academic evaluators
- **Technical Level**: High technical proficiency
- **Priority**: Methodological rigor, analytical soundness
- **Decision Power**: Moderate - assess technical competency

### Audience Needs
| Audience Type | Primary Need | Secondary Need | Communication Style |
|--------------|--------------|----------------|-------------------|
| Investors | Business insights | Data credibility | Executive summary, visuals |
| Stakeholders | Strategic value | Implementation feasibility | High-level narrative |
| Technical | Methodological rigor | Reproducibility | Detailed methodology |

---

## WHAT - Core Message and Action

### Primary Objective
**Demonstrate proficiency in hierarchical data visualization techniques and their strategic application to complex, multi-dimensional datasets.**

### Key Messages

#### Message 1: Global Market Insights
**Statement**: Asia dominates global demographics (58.9%) while North America leads in economic productivity (GDP per capita)

**Action**: Inform market entry and expansion strategies based on population-wealth dynamics

**Evidence**:
- Asia: 58.9% population, lower GDP per capita
- North America: 7.6% population, highest GDP per capita
- China + India: 2,849M people (concentrated opportunity)

#### Message 2: Resource Allocation Patterns
**Statement**: Technology companies demonstrate characteristic investment patterns with engineering-heavy budget allocation

**Action**: Benchmark organizational structure and budget distribution against industry standards

**Evidence**:
- Engineering: 50% budget allocation
- Engineering: Only 10.2% workforce
- Technical/Non-technical split: 11.4% / 88.6%

#### Message 3: Visualization Methodology Selection
**Statement**: Different hierarchical visualization techniques serve distinct analytical purposes

**Action**: Select appropriate visualization methods based on data structure and analytical objectives

**Evidence**:
- 4 techniques evaluated (Treemap, Dendrogram, Sunburst, Bar Chart)
- 5 country clusters identified through hierarchical clustering
- Clear use-case mapping established

### Desired Outcomes

**For Investors**:
- ✓ Confidence in analytical capabilities
- ✓ Understanding of data-driven insights
- ✓ Recognition of strategic thinking

**For Stakeholders**:
- ✓ Clarity on methodology selection
- ✓ Appreciation of visualization trade-offs
- ✓ Trust in technical execution

---

## HOW - Data Strategy and Execution

### Data Sources

#### Dataset 1: World Population
- **Source**: UN Data (195 countries)
- **Variables**: Country, Continent, Population (2023), GDP (2023)
- **Purpose**: Demonstrate hierarchical aggregation and comparative analysis
- **Quality**: Official international statistics, high reliability
- **Preprocessing**: GDP per capita calculation, null value handling

#### Dataset 2: Organizational Structure
- **Source**: Synthetic tech company data
- **Variables**: Department, Team, Employee count
- **Purpose**: Illustrate multi-level organizational hierarchies
- **Quality**: Realistic industry patterns
- **Preprocessing**: Hierarchical relationship mapping

#### Dataset 3: Budget Allocation
- **Source**: Synthetic corporate budget data
- **Variables**: Department, Project, Budget amount
- **Purpose**: Show resource distribution patterns
- **Quality**: Representative of tech sector norms
- **Preprocessing**: Aggregation by department and category

### Analytical Approach

#### Phase 1: Exploratory Analysis
1. Data quality assessment (missing values, outliers)
2. Descriptive statistics calculation
3. Initial pattern identification
4. Variable relationship exploration

#### Phase 2: Visualization Implementation
1. **Treemap**: Population and budget proportional representation
2. **Dendrogram**: Country clustering via Ward's method
3. **Sunburst**: Radial organizational hierarchy display
4. **Comparative**: Multiple techniques on same dataset

#### Phase 3: Insight Extraction
1. Quantitative metric calculation
2. Pattern interpretation
3. Cross-technique comparison
4. Business insight formulation

### Technical Execution

#### Tools & Libraries
- **Python 3.x**: Primary analysis environment
- **Pandas**: Data manipulation and aggregation
- **Matplotlib/Seaborn**: Static visualizations
- **Plotly**: Interactive visualizations
- **Squarify**: Treemap implementation
- **SciPy**: Hierarchical clustering algorithms
- **Scikit-learn**: Data standardization

#### Methodological Rigor
- **Standardization**: Z-score normalization for clustering
- **Distance Metric**: Euclidean distance for similarity
- **Linkage Method**: Ward's criterion for cluster formation
- **Validation**: Visual inspection and business logic verification

### Communication Strategy

#### Visual Hierarchy
1. **Executive Summary**: High-level findings (1 page)
2. **Methodology Overview**: Technique explanation (4 pages)
3. **Detailed Results**: Per-technique analysis (1 page each)
4. **Comparative Assessment**: Cross-method evaluation (1 page)
5. **Conclusions**: Strategic recommendations (1 page)

#### Narrative Flow
```
Problem → Methods → Results → Insights → Recommendations
```

**Introduction** (Why this matters)
↓
**Techniques** (How we analyzed)
↓
**Findings** (What we discovered)
↓
**Comparison** (What works best when)
↓
**Conclusions** (What to do with this)

#### Design Principles
- **Clarity**: Avoid technical jargon for non-technical audience
- **Consistency**: Uniform color schemes and formatting
- **Hierarchy**: Clear visual importance indicators
- **Whitespace**: Prevent cognitive overload
- **Accessibility**: High contrast, readable fonts

### Success Metrics

#### Qualitative Indicators
- ✓ Audience engagement during presentation
- ✓ Relevant questions asked
- ✓ Positive feedback on clarity
- ✓ Request for additional details

#### Quantitative Indicators
- ✓ 100% visualization techniques implemented
- ✓ 3 distinct datasets analyzed
- ✓ 5 country clusters identified
- ✓ 4 comparative methods evaluated
- ✓ 9-page comprehensive report delivered

---

## Implementation Timeline

| Phase | Activities | Duration | Deliverables |
|-------|-----------|----------|--------------|
| Data Preparation | Collection, cleaning, validation | 2 days | Clean datasets |
| Analysis | Exploratory analysis, clustering | 3 days | Statistical insights |
| Visualization | Create all 4 visualization types | 3 days | Visual outputs |
| Documentation | Write report, create storyboard | 2 days | Final documents |
| Review | Quality check, refinement | 1 day | Polished deliverables |

**Total**: 11 days

---

## Risk Mitigation

### Potential Challenges

**Challenge 1**: Audience technical literacy variance
- **Mitigation**: Multi-level explanations (executive summary + technical details)
- **Backup Plan**: Supplementary glossary available

**Challenge 2**: Visualization complexity overwhelming viewers
- **Mitigation**: Progressive disclosure, start simple then drill down
- **Backup Plan**: Simplified versions prepared

**Challenge 3**: Data quality issues
- **Mitigation**: Thorough preprocessing and validation
- **Backup Plan**: Document assumptions and limitations

---

## Conclusion

This framework ensures that hierarchical data visualization analysis serves its intended purpose: demonstrating analytical competency while extracting actionable insights for decision-makers. By clearly defining audience needs, core messages, and execution strategy, we maximize communication effectiveness and stakeholder value.