#!/bin/bash
# Break

no=6
for i in 1 2 3 5 3 5 9 6 3 
do 
	if [[ $no -eq $i ]]
	then 
		echo "$no is found!!"
		break
	fi
	echo "Number is $i"
done
