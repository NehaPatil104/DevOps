#!/bin/bash

# AND Operator

read -p "Enter your age: " age
read -p "Enter your nationality: " nationality
if [[ $age -ge 18 ]] && [[ $nationality == "Indian" ]]
then 
	echo "You can vote"
else
	echo "You can't vote"
fi

