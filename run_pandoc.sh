#!/bin/bash

# Script for better rendering of pdf from markdown, lots of possibilities


pandoc "$1" \
    -o "$2" \
    -f markdown \
    -V linkcolor:blue \
    -V geometry:a4paper \
    -V geometry:margin=2.3cm \
    -V mainfont="DejaVu Serif" \
    -V monofont="DejaVu Sans Mono" \
    -V mathfont="TeXGyreDejaVuMath-Regular" \
    -V fontsize=12pt \
    -V urlcolor=blue \
    --pdf-engine=xelatex \
    --highlight-style="kate" 
    
