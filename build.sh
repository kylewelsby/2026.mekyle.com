#!/usr/bin/env bash
# Cloudflare Pages build for the Zola site.
#
# Prefers mise (the project's tool manager, see .mise.toml) and falls back to a
# direct binary download when mise is not on the build image. Idempotent: safe
# to re-run on a warm build environment.
#
# HTML and inline scripts are minified by Zola itself (minify_html in
# config.toml); static/js/plausible.js already ships minified, so there is no
# separate JS-minify step to maintain here.
set -euo pipefail

# Single source of truth for the Zola version lives in .mise.toml.
ZOLA_VERSION="$(sed -n 's/^zola[[:space:]]*=[[:space:]]*"\([^"]*\)".*/\1/p' .mise.toml)"

if command -v mise >/dev/null 2>&1; then
  echo "mise detected; installing pinned tools..."
  mise trust --yes >/dev/null 2>&1 || true
  mise install
  ZOLA=(mise exec -- zola)
else
  echo "mise not found; downloading Zola v${ZOLA_VERSION}..."
  curl -sL "https://github.com/getzola/zola/releases/download/v${ZOLA_VERSION}/zola-v${ZOLA_VERSION}-x86_64-unknown-linux-gnu.tar.gz" | tar xz
  chmod +x zola
  ZOLA=(./zola)
fi

# Production (main) excludes drafts; preview and branch deploys include them so
# work in progress is reviewable on *.pages.dev before it ships.
if [ "${CF_PAGES_BRANCH:-}" = "main" ]; then
  echo "Building Zola site (production, drafts excluded)..."
  "${ZOLA[@]}" build
else
  echo "Building Zola site (preview '${CF_PAGES_BRANCH:-local}', drafts included)..."
  "${ZOLA[@]}" build --drafts
fi

echo "Build complete!"
