#!/bin/sh

gawk  '$2 > 500'  Photometry_V_Band.txt  | gawk '$2 < 1500' | gawk '$3 > 500' | gawk '$3 < 1500' | sort -r -gk 4 > Results.txt

