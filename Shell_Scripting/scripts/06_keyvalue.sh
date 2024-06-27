#!/bin/bash

# HOw to store key value pair
#
declare -A myArray
myArray=( [name]=Neha [age]=20 )

echo "Name: ${myArray[name]}, Age: ${myArray[age]}"
