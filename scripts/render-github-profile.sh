#!/usr/bin/env bash
# Renders the GitHub profile images: the README banner and the profile picture.
# They live in the kylewelsby/kylewelsby repository, not on this site.
# Usage: scripts/render-github-profile.sh <output directory>
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
out="${1:?Usage: scripts/render-github-profile.sh <output directory>}"
chrome="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$out"
for file in banner.jpg avatar.jpg; do
    [ ! -d "$out/$file" ] || { echo "$out/$file is a directory" >&2; exit 1; }
done

"$chrome" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=2 \
    --allow-file-access-from-files --virtual-time-budget=4000 --window-size=1280,400 \
    --screenshot="$tmp/banner.png" "file://$root/scripts/social-card/github-banner.html" >/dev/null 2>&1
[ -s "$tmp/banner.png" ] || { echo "Chrome did not render the banner" >&2; exit 1; }
sips -s format jpeg -s formatOptions 88 "$tmp/banner.png" --out "$tmp/banner.jpg" >/dev/null

"$root/scripts/render-favicons.py" --avatar "$tmp/avatar.jpg"

mv "$tmp/banner.jpg" "$tmp/avatar.jpg" "$out/"

for file in banner.jpg avatar.jpg; do
    echo "$out/$file $(sips -g pixelWidth -g pixelHeight "$out/$file" | awk '/pixel/ {printf "%s ", $2}')"
done
