# Examples

This folder contains example scripts demonstrating civic data analysis using MCP servers and NYC Open Data.

## Scripts

| Script | Description |
|--------|-------------|
| `nyc_311_dashboard.py` | Interactive Streamlit dashboard analyzing NYC 311 service requests with Tufte-style visualizations |
| `mcp_demo.py` | Interactive demo of MCP server queries |
| `real_data_analysis.py` | Sample analysis script for NYC data |
| `analyze_nyc_data.py` | NYC data analysis utilities |
| `create_visualizations.py` | Chart generation examples |
| `create_html_visualizations.py` | HTML-based visualization output |
| `interactive_mcp_example.py` | Interactive MCP query examples |

## Running the 311 Dashboard

```bash
cd examples
streamlit run nyc_311_dashboard.py --server.headless=true
```

The dashboard will be available at http://localhost:8501

## Data Sources

- **NYC 311 Service Requests** (`erm2-nwe9`) - Complaints and service requests
- **Restaurant Inspections** (`43nn-pn8j`) - Health inspection grades
- **Housing Violations** (`wvxf-dwi5`) - HPD violations

## Documentation

See [REAL_DATA_ANALYSIS.md](REAL_DATA_ANALYSIS.md) for sample analysis results and insights.
