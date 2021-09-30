#!/bin/sh

echo "Number of objects"
gawk ' sqrt( ($2 - 1000)^2 + ($3 - 1000)^2 ) < 300'  Photometry_V_Band.txt | wc -l 
 
echo "Brightest object":
gawk ' sqrt( ($2 - 1000)^2 + ($3 - 1000)^2 ) < 300'  Photometry_V_Band.txt | sort -gk 4 | tail -1
