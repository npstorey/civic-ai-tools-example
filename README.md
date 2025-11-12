# Civic AI Tools - Example Project

This is a demonstration project showing the **proper workflow** for using civic-ai-tools infrastructure.

## 📁 Directory Structure

This example demonstrates the recommended sibling directory approach:

```
/Users/nathanstorey/Code/
├── civic-ai-tools/          # Shared infrastructure (library)
├── opengov-mcp-server/      # OpenGov MCP Server
└── civic-ai-tools-example/  # This example project ← YOU ARE HERE
    ├── .cursor/
    │   └── mcp.json         # References ../civic-ai-tools
    ├── scripts/
    │   └── analyze_nyc_data.py
    └── README.md
```

## 🎯 Purpose

This example shows how to:
- Structure a new civic analysis project
- Reference civic-ai-tools as a sibling directory
- Use MCP servers and Skills from civic-ai-tools
- Keep your project code separate from infrastructure

## 🚀 What This Example Does

The `scripts/analyze_nyc_data.py` script demonstrates:
1. Using the OpenGov MCP Companion Skill (referenced from civic-ai-tools)
2. Querying NYC Open Data via the OpenGov MCP Server
3. Proper project structure for real civic analysis work

## ⚙️ Setup

### Prerequisites

1. **Civic-ai-tools** must be cloned as a sibling:
   ```bash
   cd /Users/nathanstorey/Code
   git clone https://github.com/npstorey/civic-ai-tools.git
   ```

2. **OpenGov MCP Server** must be cloned and built:
   ```bash
   cd /Users/nathanstorey/Code
   git clone https://github.com/npstorey/opengov-mcp-server.git
   cd opengov-mcp-server
   npm install && npm run build
   ```

3. **Node.js** required for OpenGov MCP Server

### Running the Example

```bash
# From the civic-ai-tools-example directory
python scripts/analyze_nyc_data.py
```

Or, when using Claude Code with the MCP configuration:
- Open this project in Cursor/Claude Code
- The `.cursor/mcp.json` file will load the MCP servers and skills
- Ask Claude natural language questions about NYC data

## 📝 MCP Configuration

The `.cursor/mcp.json` file demonstrates:
- How to reference the OpenGov MCP Server (sibling directory)
- How to load Skills from civic-ai-tools (sibling directory)
- Environment variables for configuration

## 🔍 Learning Points

1. **Infrastructure vs. Project Separation**
   - civic-ai-tools = reusable infrastructure
   - This project = your analysis work
   - Keep them separate in git

2. **Path References**
   - Use `../civic-ai-tools/` to reference infrastructure
   - Use `./` for project-local files
   - All paths are relative to this project's root

3. **Skills Usage**
   - Shared skills come from civic-ai-tools
   - Project-specific skills can live in `./skills/`
   - Both can be used together

## 🎓 Creating Your Own Project

To create a new civic analysis project:

```bash
# 1. Create your project directory
cd /Users/nathanstorey/Code
mkdir my-civic-project
cd my-civic-project

# 2. Initialize git (separate from civic-ai-tools)
git init

# 3. Copy an MCP template
cp ../civic-ai-tools/configs/mcp-templates/municipal-research.json .cursor/mcp.json

# 4. Start analyzing!
```

## 📚 Resources

- **Civic-AI-Tools Docs**: `../civic-ai-tools/CIVIC_AI_TOOLS_SETUP.md`
- **Configuration Templates**: `../civic-ai-tools/configs/mcp-templates/`
- **Skills Catalog**: `../civic-ai-tools/docs/skills-catalog.md`

## ⚠️ Common Issues

### "Skill not found" or "MCP server not found"
- Check that civic-ai-tools and opengov-mcp-server are in sibling directories
- Verify paths in `.cursor/mcp.json` are correct
- Run `../civic-ai-tools/scripts/validate-setup.sh` (once we create it!)

### "Module not found"
- Make sure you've set up the Python environment:
  ```bash
  cd ../civic-ai-tools
  uv sync
  ```

---

**This is a template/example project - not meant for production work.**

For real civic analysis, create your own project following this structure!
