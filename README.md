<p align="center">
  <img src="assets/clueso-logo.png" alt="Clueso" width="88" height="88" />
</p>

# Clueso MCP

> Make videos and docs with ChatGPT, Claude, and Gemini.

Clueso's MCP connects your favorite AI agents to a video creation engine.
Just describe what you need — and every output stays fully editable, by you or AI.

No scripting, no API keys to manage, no terminal commands. This is a remote
(hosted) MCP server: connect to the endpoint, authorize with your Clueso
account, and start creating in about two minutes.

- **Server URL:** `https://connect.clueso.io/mcp`
- **Transport:** Streamable HTTP
- **Auth:** OAuth 2.0 (sign in to Clueso)
- **Registry name:** `io.clueso/video`

## Connect your MCP

Works with **Claude, ChatGPT, Gemini, GitHub Copilot, Cursor — or any MCP client.**

- **Claude / Claude Code:** Settings → Connectors → Add custom connector →
  `https://connect.clueso.io/mcp` → authorize.
- **ChatGPT / Cursor / any other MCP client:** add a custom connector pointing
  at the same URL; your client walks you through the OAuth sign-in.

### GitHub Copilot

Copilot speaks the same Streamable HTTP + OAuth that every other client here
uses, so there is nothing Copilot-specific to install — just point it at the
same URL.

**VS Code** — add `.vscode/mcp.json` to your workspace (or your user config):

```json
{
  "servers": {
    "clueso": {
      "type": "http",
      "url": "https://connect.clueso.io/mcp"
    }
  }
}
```

Or from the terminal, without editing files by hand:

```bash
code --add-mcp '{"name":"clueso","type":"http","url":"https://connect.clueso.io/mcp"}'
```

Then open Copilot Chat in **Agent mode** and pick the `clueso` tools. The first
call opens a browser to sign in to Clueso; after that the session is
remembered.

**Copilot CLI** — add the same server via `/mcp add`, choosing HTTP transport
and the URL above. See
[Adding MCP servers for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers).

> **On Copilot Business / Enterprise plans**, an admin has to enable the
> **"MCP servers in Copilot"** policy for your organization before any MCP
> server — including this one — becomes available. If Copilot never lists the
> `clueso` tools, check that policy first; it is the usual cause.

Full setup guide: https://help.clueso.io/mcp-setup

## What you can make

Create videos through conversation — product walkthroughs, feature
announcements, tutorials, sales demos, training content, and customer
onboarding videos. Your agent applies your brand guidelines automatically,
so everything stays on-brand.

## Edit anything, just by asking

Edit existing videos the same way — swapping assets, updating text, changing
branding, trimming clips, adjusting transitions, and rearranging sections.
Manage your entire library, all through conversation.

## Example workflows

- Read a Linear ticket → produce a release video → post it to Slack
- Turn your top support tickets into explainer videos, auto-published to your help center
- "Localize my entire video library into French and Spanish" — in one instruction
- Turn a meeting recording into a polished recap in minutes

## Links

- Homepage: https://www.clueso.io/mcp
- Setup: https://help.clueso.io/mcp-setup
- Privacy: https://www.clueso.io/legal/privacy
- Terms: https://www.clueso.io/legal/terms

## For maintainers

Public anchor for Clueso's MCP listing across registries. Canonical metadata
lives in [`server.json`](./server.json), published to the
[official MCP Registry](https://registry.modelcontextprotocol.io) as
`io.clueso/video` via DNS-authenticated publishing from the `clueso.io` domain.
