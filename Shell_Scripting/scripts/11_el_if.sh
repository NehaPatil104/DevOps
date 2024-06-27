#!/bin/bash
# Else - if
#
read -p "Enter your marks: " marks

if [[ $marks -ge 80 ]]
then
	echo "1st Division"
elif [[ $marks -ge 60 ]]
then 
	echo "2nd Division"
elif [[ $marks -ge 30 ]]
then 
	echo "3rd Division"
else
	echo "Fail !"
fi
