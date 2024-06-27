#!/bin/bash
#
#Getting values from a file

FILE="name.txt"

for name in $(cat $FILE)
do
	echo "Name: $name"
done
