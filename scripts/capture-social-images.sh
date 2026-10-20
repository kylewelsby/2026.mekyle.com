#!/usr/bin/env bash
# Renders scripts/social-card/card.html as the Open Graph and Twitter cards.
# Each file name carries its hash and the script writes it into templates/base.html,
# because LinkedIn caches a card by its path and ignores a ?v= query.
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
    sips -s format jpeg -s formatOptions 90 "$tmp/$name.png" --out "$tmp/$name.jpg" >/dev/null
    file="$name-$(shasum -a 256 "$tmp/$name.jpg" | cut -c1-8).jpg"
    mv "$tmp/$name.jpg" "$out/$file"
    find "$out" -name "$name-????????.jpg" ! -name "$file" -delete
    sed -E -i '' "s#/images/$name-[0-9a-f]{8}\.jpg#/images/$file#" "$root/templates/base.html"
    grep -q "/images/$file" "$root/templates/base.html" || { echo "templates/base.html has no /images/$name-<hash>.jpg" >&2; exit 1; }
    echo "$out/$file $(sips -g pixelWidth -g pixelHeight "$out/$file" | awk '/pixel/ {printf "%s ", $2}')"
done
