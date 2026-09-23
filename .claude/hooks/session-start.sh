#!/bin/bash
# Claude Code on the web: install Playwright (Python) at session start.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Pinned to match the Chromium build pre-installed in the web environment
# (/opt/pw-browsers/chromium-1194), so no browser download is needed.
PLAYWRIGHT_VERSION="1.56.0"

if python3 -c "import playwright, importlib.metadata as m; assert m.version('playwright') == '${PLAYWRIGHT_VERSION}'" 2>/dev/null; then
  echo "playwright ${PLAYWRIGHT_VERSION} already installed"
  exit 0
fi

pip install --quiet --root-user-action=ignore "playwright==${PLAYWRIGHT_VERSION}"
