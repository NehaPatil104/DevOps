#!/bin/bash

FILEPATH=name.txt

if [[ -f $FILEPATH ]]
then
	echo "File exist"
else
	echo "File not exist"
	exit 1
fi
