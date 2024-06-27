#!/bin/bash

# Switch case

echo "Provide an option"
echo "a : Print date"
echo "b : List Scripts"
echo "c : Current Location"

read choice

case $choice in
	a)date;;
	b)ls;;
	c)pwd;;
	*) echo "Please provide valid option"
esac
