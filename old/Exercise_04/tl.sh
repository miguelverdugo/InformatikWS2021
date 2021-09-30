#!/bin/bash
# usage sum.sh integer1 operation integer2

color="red"

echo "for-loop, n=5"

for i in $(seq 1 5)
do
  if [ "$color" = "red" ]
  then
    echo "$color"
    color="green"
    sleep 10
  elif [ "$color" = "green" ]
  then
    echo "$color"
    color="red"
    sleep 5
  fi
done

echo "While loop, Ctrl c to stop"

while [ true ]
do
  if [ "$color" = "red" ]
  then
    echo "$color"
    color="green"
    sleep 10
  elif [ "$color" = "green" ]
  then
    echo "$color"
    color="red"
    sleep 5
  fi
done
