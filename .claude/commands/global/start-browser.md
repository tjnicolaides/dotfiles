---
description: Start web browser for automation and testing
---

Before using browser related tools (Chrome Devtools MCP, or Playwright MCP), ensure Chrome is running with debugging port:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 &
```

This starts Chrome with debugging on port 9222.

Target: $ARGUMENTS

If a URL is provided in arguments, navigate there after confirming Chrome is running.
