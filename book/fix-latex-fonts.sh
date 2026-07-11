#!/bin/bash
# Download and install Source Sans Pro + Source Code Pro for PDF rendering
set -e

FONT_DIR="/usr/share/fonts/truetype/source-sans-pro"
mkdir -p "$FONT_DIR"
cd /tmp

# Source Sans Pro
curl -sL "https://github.com/adobe-fonts/source-sans/releases/download/3.052R/OTF-source-sans-3.052R.zip" -o source-sans.zip
unzip -q -o source-sans.zip -d source-sans 2>/dev/null || true
cp /tmp/source-sans/OTF/*.otf "$FONT_DIR/" 2>/dev/null || true

# Source Code Pro  
curl -sL "https://github.com/adobe-fonts/source-code-pro/releases/download/2.042R-u/1.062R-i/1.026R-vf/TTF-source-code-pro-2.042R-u_1.062R-i_1.026R-vf.zip" -o source-code.zip
unzip -q -o source-code.zip -d source-code 2>/dev/null || true
cp /tmp/source-code/TTF/*.ttf "$FONT_DIR/" 2>/dev/null || true

find "$FONT_DIR" -name "*.otf" -o -name "*.ttf" 2>/dev/null | head -5
fc-cache -f 2>/dev/null || true
echo "Fonts installed"
