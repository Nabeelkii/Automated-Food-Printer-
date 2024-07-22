#!/bin/bash

number=$(cat output.txt)
number=$(( (${#number} - 1) * 5 ))
echo "$number"
