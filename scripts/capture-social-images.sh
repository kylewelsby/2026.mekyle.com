#!/usr/bin/env bash
# Captures the homepage hero as the Open Graph and Twitter cards.
# Run `mise exec -- zola serve` first. Usage: scripts/capture-social-images.sh [url]
set -euo pipefail

url="${1:-http://127.0.0.1:1111/}"
chrome="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
out="$(cd "$(dirname "$0")/.." && pwd)/static/images"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

for card in "og-image 1200 630" "twitter-card 1200 600"; do
    read -r name width height <<<"$card"
    "$chrome" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
        --virtual-time-budget=4000 --window-size="$width,$height" \
        --screenshot="$tmp/$name.png" "$url" >/dev/null 2>&1
    sips -s format jpeg -s formatOptions 88 "$tmp/$name.png" --out "$out/$name.jpg" >/dev/null
    echo "$out/$name.jpg"
done
