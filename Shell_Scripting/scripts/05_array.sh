#!/bin/bash
#Array

myArray=( Hi 1 2 3.1 "Heyy Buddy" Jeee ) 

echo "${myArray[0]}"
echo "${myArray[3]}"

# Length of array
#
echo "Length: ${#myArray[*]}"

# Slicing
#
echo "Values from index 2 to 3 ${myArray[*]:1:2}"

# Update array

myArray+=( New 30 40 )
echo "${myArray[*]}"
