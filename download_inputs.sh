#!/bin/bash
# This helper script downloads all the files for a year
# It relies on aocd, which you can install with
# uv tool install git+https://github.com/wimglenn/advent-of-code-data.git
#
#  export AOC_SESSION=xyz # (leading space so it's not added to history)
# YEAR=20XX ./download.sh
# 
# To download just today's input:
# DAY=01 aocd ${DAY} > "day${DAY}.txt
set -e

year=${YEAR:-$(date +%Y)}

for day in $(seq -w 1 25); do
  echo "Fetching data for day $day of year $year..."
  aocd ${day} ${year} > "day${day}.txt"
done

echo "Done"
