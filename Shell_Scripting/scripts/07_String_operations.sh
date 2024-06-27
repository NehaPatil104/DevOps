#!/bin/bash
#
#String Operations
#
myVar="Hey, how are you?"
myVarLength=${#myVar}
echo "String length: ${myVarLength}"

echo "Upper case: ${myVar^^}"
echo "Lower case: ${myVar,,}"

# Replacing a string
newVar=${myVar/Hey/Hello}
echo "${newVar}"

# String slicing

echo "String Slicing: ${myVar:5:10}"
