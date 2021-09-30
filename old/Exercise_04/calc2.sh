#!/bin/bash
# usage sum.sh integer1 operation integer2

echo "Which operation?"
read CHOICE

if [ "$CHOICE" == "+" ]; then
  ((result=$1+$2))
elif [ "$CHOICE" == "-" ]; then
  ((result=$1-$2))
elif [ "$CHOICE" == "/" ]; then
  ((result=$1/$2))
elif [ "$CHOICE" == "*" ]; then
   ((result=$1*$2))
elif [ "$CHOICE" == "^" ]; then
   ((result=$1**$2))
fi

echo "Result is $result"