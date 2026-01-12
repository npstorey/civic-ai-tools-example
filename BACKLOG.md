# Backlog

Future decisions and potential improvements for this project.

---

## Decision: civic-ai-tools Repository

**Status:** Pending decision

**Context:**
This example project was originally designed to work with a sibling `civic-ai-tools` repository that contained shared infrastructure (Skills, MCP templates, configs). The project has now been refactored to be fully standalone.

**The civic-ai-tools repo contained:**
- OpenGov MCP Companion Skill (now embedded in `docs/opengov-skill.md`)
- MCP configuration templates
- Shared documentation
- Potentially other skills

**Options:**

1. **Archive civic-ai-tools**
   - This example is now standalone and self-sufficient
   - No other projects currently depend on it
   - Reduces maintenance burden

2. **Keep civic-ai-tools as a skill library**
   - Useful if you plan multiple civic data projects
   - Central place to develop and maintain skills
   - Projects can copy skills they need (like this one did)

3. **Merge remaining useful content**
   - Review civic-ai-tools for any other valuable skills or patterns
   - Add them to this repo's `docs/` directory
   - Then archive civic-ai-tools

**To decide:** Review what else exists in civic-ai-tools and whether future projects would benefit from shared infrastructure.

---

## Future Improvements

### Simplify opengov-mcp Installation

**Current state:** Users must clone and build opengov-mcp-server locally via the setup script.

**Goal:** Allow installation via a single command like `npm install -g` or `npx`.

**Options:**

1. **Publish to npm** (recommended)
   - Natural fit since it's a Node.js/TypeScript project
   - Users could run `npx opengov-mcp-server` directly
   - Setup script would simplify significantly
   - Requires: npm account, proper package.json metadata, publish workflow

2. **Rewrite in Python**
   - Would allow `uv tool install` / `pip install` like datacommons-mcp
   - More consistent with Python-based MCP ecosystem
   - Significant effort to rewrite
   - Consider if: Python rewrite offers other benefits (easier contributions, better library ecosystem for civic data)

**Recommendation:** Start with npm publishing. Evaluate Python rewrite only if there's a compelling reason beyond installation convenience.

### Add More Skills
- Consider adding a Data Commons companion skill (`docs/datacommons-skill.md`)
- Document common query patterns for other Socrata portals (Chicago, SF, etc.)

### Codex CLI Support
- Add `~/.codex/config.toml` setup instructions for OpenAI Codex CLI
- Currently only supports Cursor IDE and Claude Code CLI

### Testing
- Add integration tests that verify MCP servers respond correctly
- Could run as part of CI after setup

---

## Notes

- Decision point created: 2026-01-08
- Project converted to standalone: 2026-01-08
