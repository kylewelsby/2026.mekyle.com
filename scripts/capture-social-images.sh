#!/usr/bin/env bash
# Renders scripts/social-card/card.html as the Open Graph and Twitter cards.
# Usage: scripts/capture-social-images.sh
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
card="file://$root/scripts/social-card/card.html"
chrome="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
out="$root/static/images"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

for spec in "og-image 630" "twitter-card 600"; do
    read -r name height <<<"$spec"
    "$chrome" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
        --allow-file-access-from-files --virtual-time-budget=4000 --window-size="1200,$height" \
        --screenshot="$tmp/$name.png" "$card?h=$height" >/dev/null 2>&1
    sips -s format jpeg -s formatOptions 90 "$tmp/$name.png" --out "$out/$name.jpg" >/dev/null
    echo "$out/$name.jpg $(sips -g pixelWidth -g pixelHeight "$out/$name.jpg" | awk '/pixel/ {printf "%s ", $2}')"
done
