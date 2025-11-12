#!/usr/bin/env python3
"""
Example Analysis Script - NYC Open Data

This script demonstrates how a civic analysis project uses the
civic-ai-tools infrastructure without directly embedding it.

Directory Structure:
    Code/
    ├── civic-ai-tools/          # Infrastructure (separate repo)
    ├── opengov-mcp-server/      # MCP server (separate repo)
    └── civic-ai-tools-example/  # This project
        └── scripts/
            └── analyze_nyc_data.py  ← YOU ARE HERE

Key Concepts:
    - This project is SEPARATE from civic-ai-tools
    - Infrastructure is referenced via .cursor/mcp.json
    - When using Claude Code, Skills and MCPs are loaded automatically
    - This script can run standalone OR with Claude assistance

Usage:
    # Standalone (shows example query structure)
    python scripts/analyze_nyc_data.py

    # With Claude Code + MCP (interactive analysis)
    Ask Claude: "Using the OpenGov MCP, show me recent 311 complaints in NYC"
"""

import sys
from datetime import datetime, timedelta

def print_header(title):
    """Print a formatted header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def example_query_structure():
    """
    Show what a SoQL query looks like for NYC Open Data

    When using Claude Code with the OpenGov MCP Server configured,
    Claude can generate and execute these queries automatically using
    the OpenGov MCP Companion Skill.
    """
    print_header("Example: NYC 311 Service Requests Analysis")

    print("\nDataset: NYC 311 Service Requests")
    print("Domain: data.cityofnewyork.us")
    print("Dataset ID: erm2-nwe9")

    # Calculate date for last 7 days
    one_week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    print("\n📊 Example SoQL Query (what the MCP would execute):")
    print("-" * 70)
    query = f"""
SELECT
  complaint_type,
  COUNT(*) as count
WHERE
  created_date >= '{one_week_ago}T00:00:00'
GROUP BY
  complaint_type
ORDER BY
  count DESC
LIMIT 10
    """.strip()
    print(query)
    print("-" * 70)

    print("\n💡 With Claude Code + OpenGov MCP, you would ask:")
    print('   "Show me the top 10 complaint types in NYC 311 from the last week"')
    print("\n   Claude would:")
    print("   1. Use the OpenGov MCP Companion Skill for guidance")
    print("   2. Generate the SoQL query above")
    print("   3. Execute it via the OpenGov MCP Server")
    print("   4. Format and present the results")


def show_project_structure():
    """Explain the project structure and benefits"""
    print_header("Understanding the Project Structure")

    print("""
Why Separate Projects?

✓ Clean Separation: Infrastructure vs. Analysis Work
  - civic-ai-tools: Reusable MCP servers and Skills (shared library)
  - This project: Your specific civic analysis work

✓ Version Control: Independent git repositories
  - Commit analysis work without affecting infrastructure
  - Update infrastructure without touching analysis
  - Clear git history for each concern

✓ Scalability: Use civic-ai-tools for multiple projects
  - Clone civic-ai-tools ONCE
  - Create many analysis projects that reference it
  - Share infrastructure across your team

✓ Contribution: Improve shared infrastructure
  - Find a useful pattern? Add it to civic-ai-tools
  - Submit PRs to benefit the whole community
  - Keep project-specific work private

Directory Layout:
""")

    print("""
    /Users/nathanstorey/Code/
    ├── civic-ai-tools/              # Clone once, use everywhere
    │   ├── skills/                  # Shared Skills (OpenGov MCP Companion, etc.)
    │   ├── mcp-servers/             # MCP server implementations
    │   ├── configs/mcp-templates/   # Configuration templates
    │   └── docs/                    # Infrastructure documentation
    │
    ├── opengov-mcp-server/          # Separate MCP server (also shared)
    │   └── dist/index.js
    │
    ├── civic-ai-tools-example/      # Example project (THIS)
    │   ├── .cursor/mcp.json         # References ../civic-ai-tools/
    │   ├── scripts/                 # Project-specific analysis scripts
    │   └── README.md
    │
    ├── nyc-governance-analysis/     # Another project (imaginary)
    │   ├── .cursor/mcp.json         # Also references ../civic-ai-tools/
    │   └── ...
    │
    └── budget-transparency/         # Yet another project (imaginary)
        ├── .cursor/mcp.json         # Also references ../civic-ai-tools/
        └── ...

    Each project has its own git repository, but they all share civic-ai-tools!
    """)


def show_mcp_workflow():
    """Explain how MCPs and Skills work together"""
    print_header("How MCP Servers and Skills Work Together")

    print("""
When you open this project in Claude Code / Cursor:

1. 📄 Loads .cursor/mcp.json
   - Finds MCP server paths: ../../opengov-mcp-server/dist/index.js
   - Finds Skill paths: ../../civic-ai-tools/skills/opengov-mcp-companion

2. 🚀 Starts MCP Servers
   - OpenGov MCP Server: Connects to NYC Open Data (Socrata API)
   - Data Commons MCP: Connects to Google Data Commons

3. 📚 Loads Skills
   - OpenGov MCP Companion: Guides Claude in using OpenGov MCP effectively
   - Provides SoQL query patterns, best practices, error handling

4. 💬 You Ask Questions
   "Show me noise complaints by borough in the last month"

5. 🤖 Claude Responds
   - Uses OpenGov MCP Companion Skill for guidance
   - Generates appropriate SoQL query
   - Executes via OpenGov MCP Server
   - Formats results for you

6. 📊 You Get Results
   - Clean, formatted analysis
   - Source citations (exact queries used)
   - Downloadable data exports
   - Reproducible methodology

All without manually writing SQL or API calls!
    """)


def show_next_steps():
    """Suggest next steps for users"""
    print_header("Next Steps")

    print("""
To Use This Example:

1. ✓ Ensure Prerequisites:
   - civic-ai-tools cloned to: /Users/nathanstorey/Code/civic-ai-tools
   - opengov-mcp-server cloned and built (requires Node.js)
   - Python environment set up: cd civic-ai-tools && uv sync

2. 🔧 Configure MCP:
   - Check .cursor/mcp.json paths are correct
   - Add Socrata app token if you have one (optional, for higher rate limits)

3. 🚀 Start Analyzing:
   - Open this project in Cursor / Claude Code
   - Try example questions:
     "What are the most common 311 complaints in NYC?"
     "Show me restaurant inspection grades by borough"
     "Analyze trends in housing violations over time"

To Create Your Own Project:

1. Create new directory: /Users/nathanstorey/Code/my-civic-project
2. Copy MCP template: cp civic-ai-tools/configs/mcp-templates/*.json .cursor/mcp.json
3. Initialize git: git init (separate repo from civic-ai-tools!)
4. Start analyzing!

Resources:

- Infrastructure Docs: ../civic-ai-tools/CIVIC_AI_TOOLS_SETUP.md
- Configuration Templates: ../civic-ai-tools/configs/mcp-templates/
- Skills Documentation: ../civic-ai-tools/docs/skills-catalog.md
- Validation Script: ../civic-ai-tools/scripts/validate-setup.sh (run to check setup)
    """)


def main():
    """Run the example demonstration"""
    print_header("Civic AI Tools - Example Project")

    print("""
This example demonstrates the PROPER WORKFLOW for civic analysis projects
using the civic-ai-tools infrastructure.

Key Points:
- civic-ai-tools = INFRASTRUCTURE (shared library)
- This project = YOUR ANALYSIS WORK (separate repository)
- MCP servers and Skills are loaded via .cursor/mcp.json
- Keep them separate for clean version control and reusability
""")

    example_query_structure()
    show_project_structure()
    show_mcp_workflow()
    show_next_steps()

    print_header("Example Complete!")
    print("\nReady to start your own civic analysis project!")
    print("Follow the structure shown above to create clean, maintainable projects.\n")


if __name__ == "__main__":
    main()
