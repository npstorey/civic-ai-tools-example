# Setup Guide

This guide walks you through setting up the civic-ai-tools-example project to work with **Cursor IDE** or **Claude Code CLI**.

## Quick Start

```bash
git clone https://github.com/npstorey/civic-ai-tools-example.git
cd civic-ai-tools-example

# Optional: Set up API keys first (for higher rate limits)
cp .env.example .env
# Edit .env with your API keys

# Run setup
./scripts/setup.sh
```

The setup script will:
1. Check prerequisites (Node.js, Python 3.11+, git)
2. Clone and build the OpenGov MCP server into `.mcp-servers/`
3. Install the `datacommons-mcp` Python package via uv
4. **Auto-generate MCP config files** (`.mcp.json` and `.cursor/mcp.json`)
   - Reads API keys from `.env` if present
   - Uses absolute paths for Cursor (required for reliability)

---

## Prerequisites

### Required

| Tool | Version | Purpose |
|------|---------|---------|
| Node.js | 18+ | Runs opengov-mcp-server |
| npm | 8+ | Installs Node dependencies |
| Python | 3.11+ | Required by datacommons-mcp |
| git | any | Clones MCP server |

### Recommended

| Tool | Purpose |
|------|---------|
| [uv](https://github.com/astral-sh/uv) | Fast Python package manager |
| [Data Commons API Key](https://apikeys.datacommons.org/) | Higher rate limits |

Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Project Structure

After running setup:

```
civic-ai-tools-example/
├── .mcp-servers/
│   └── opengov-mcp-server/    # Cloned & built by setup script
├── .mcp.json                   # Claude Code CLI config (auto-generated, gitignored)
├── .mcp.json.example           # Template for Claude Code config
├── .cursor/
│   ├── mcp.json               # Cursor IDE config (auto-generated, gitignored)
│   └── mcp.json.example       # Template for Cursor config
├── .env.example               # API keys template
├── .env                       # Your API keys (gitignored)
├── docs/
│   └── opengov-skill.md       # OpenGov query guidance
├── scripts/
│   ├── setup.sh               # Setup script
│   └── *.py                   # Demo scripts
└── CLAUDE.md                  # Claude Code instructions
```

**Note:** The `.mcp.json`, `.cursor/mcp.json`, and `.env` files are gitignored because they contain API keys and machine-specific paths.

---

## Tool-Specific Setup

### Cursor IDE

1. Run `./scripts/setup.sh` (auto-generates `.cursor/mcp.json` with absolute paths)
2. Open this folder in Cursor
3. MCP servers should load automatically
4. If servers don't appear, fully quit Cursor (Cmd+Q) and reopen
5. Start asking questions about NYC data

### Claude Code CLI

1. Run `./scripts/setup.sh` (auto-generates `.mcp.json`)
2. Start Claude Code:
   ```bash
   claude
   ```
3. On first run, approve the MCP servers when prompted
4. Verify servers are connected:
   ```
   /mcp
   ```

---

## MCP Servers

### OpenGov MCP Server

Provides access to NYC Open Data portal (data.cityofnewyork.us) via Socrata API.

**Capabilities:**
- Query datasets using SoQL
- Dataset discovery and metadata retrieval
- Built-in caching and rate limiting

**Key Datasets:**
| Dataset | ID | Description |
|---------|-----|-------------|
| 311 Service Requests | `erm2-nwe9` | Citywide service complaints |
| Restaurant Inspections | `43nn-pn8j` | Health inspection grades |
| Housing Violations | `wvxf-dwi5` | Building code violations |
| NYC Schools | `s3k6-pzi2` | School directory |
| Traffic Accidents | `h9gi-nx95` | Motor vehicle collisions |

### Data Commons MCP

Provides access to Google Data Commons for statistical data.

**Capabilities:**
- Search geographic entities (cities, states, countries)
- Retrieve statistical data across variables
- Compare data across locations

**Key Entity DCIDs:**
| City | DCID |
|------|------|
| New York City | `geoId/3651000` |
| Los Angeles | `geoId/0644000` |
| Chicago | `geoId/1714000` |

---

## Example Queries

Once set up, try these natural language queries:

### NYC Open Data
- "What are the top 10 complaint types in NYC 311?"
- "Show me restaurant inspection grades by borough"
- "Analyze housing violation trends over the past year"

### Statistical Data
- "What's NYC's population?"
- "Compare median income in NYC, LA, and Chicago"

### Combined Analysis
- "What's the relationship between median income and housing violations?"

---

## Running Demo Scripts

```bash
# Interactive MCP capabilities demo
python scripts/mcp_demo.py

# Real data analysis example
python scripts/real_data_analysis.py
```

---

## API Keys Configuration

API keys are optional but recommended for higher rate limits. Configure them by creating a `.env` file:

```bash
# Copy the example file
cp .env.example .env

# Edit with your API keys
nano .env  # or use your preferred editor
```

### Getting API Keys

| Service | Purpose | Get Key |
|---------|---------|---------|
| NYC Open Data (Socrata) | Higher rate limits for NYC data | [Get Token](https://data.cityofnewyork.us/profile/edit/developer_settings) |
| Google Data Commons | Higher rate limits for statistical data | [Get Key](https://apikeys.datacommons.org/) |

### .env File Format

```bash
# NYC Open Data - increases rate limits significantly
SOCRATA_APP_TOKEN=your_token_here

# Data Commons - recommended for statistical queries
DC_API_KEY=your_key_here
```

The MCP servers will automatically load these from the project root `.env` file.

---

## Troubleshooting

### "MCP server not found" / "Cannot find module"

1. Run the setup script:
   ```bash
   ./scripts/setup.sh
   ```
2. Verify the server exists:
   ```bash
   ls .mcp-servers/opengov-mcp-server/dist/index.js
   ```

### "datacommons-mcp: command not found"

1. Install it:
   ```bash
   uv tool install datacommons-mcp
   ```
2. Add `~/.local/bin` to your PATH if needed
3. Re-run setup to update configs with the correct path:
   ```bash
   rm .mcp.json .cursor/mcp.json
   ./scripts/setup.sh
   ```

### Claude Code doesn't show MCP tools

1. Restart Claude Code session
2. Check `/mcp` for server status
3. Approve project-scoped servers if prompted

### Cursor doesn't load MCP servers

**Common issues and solutions:**

1. **Server shows "connected" but no tools appear:**
   - Fully quit Cursor (Cmd+Q on Mac, not just close window)
   - Reopen Cursor and the project

2. **"Cannot find module" error in logs:**
   - This usually means the path in `.cursor/mcp.json` is incorrect
   - The setup script generates absolute paths which work reliably
   - Re-run setup to regenerate:
     ```bash
     rm .cursor/mcp.json
     ./scripts/setup.sh
     ```

3. **Server connects then immediately disconnects:**
   - Check Cursor's MCP logs: Help → Toggle Developer Tools → Console
   - Look for path-related errors
   - Ensure you're using absolute paths (the setup script does this automatically)

4. **"Request timed out" errors:**
   - Fully quit and restart Cursor
   - If persists, clear Cursor's MCP cache:
     ```bash
     rm -rf ~/Library/Application\ Support/Cursor/User/globalStorage/mcp-*
     ```

**Why Cursor needs absolute paths:**

Unlike Claude Code CLI which runs from the project directory, Cursor's MCP client may resolve relative paths from a different working directory. Using absolute paths in `.cursor/mcp.json` ensures the MCP server is always found correctly. The setup script handles this automatically.

**Manually checking your Cursor config:**

Your `.cursor/mcp.json` should have paths like:
```json
{
  "args": ["/Users/yourname/path/to/civic-ai-tools-example/.mcp-servers/opengov-mcp-server/dist/index.js"]
}
```

NOT relative paths like:
```json
{
  "args": [".mcp-servers/opengov-mcp-server/dist/index.js"]
}
```

---

## Files Reference

| File | Purpose | Generated By |
|------|---------|--------------|
| `.mcp.json.example` | MCP config template for Claude Code CLI | Committed to repo |
| `.mcp.json` | Your MCP config (gitignored) | `setup.sh` auto-generates |
| `.cursor/mcp.json.example` | MCP config template for Cursor IDE | Committed to repo |
| `.cursor/mcp.json` | Your Cursor MCP config with absolute paths (gitignored) | `setup.sh` auto-generates |
| `.env.example` | API keys template | Committed to repo |
| `.env` | Your API keys (gitignored) | Copy from `.env.example` |
| `scripts/setup.sh` | Automated setup script | Committed to repo |
| `docs/opengov-skill.md` | Detailed OpenGov query guidance | Committed to repo |
| `CLAUDE.md` | Instructions for Claude Code | Committed to repo |
