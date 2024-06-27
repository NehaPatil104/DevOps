#!/bin/bash

read -p "Enter your marks: " marks

if [[ $marks -gt 40 ]]
then 
	echo "PASS"
else
	echo "FAIL"
fi
