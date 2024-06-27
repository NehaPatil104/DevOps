#!/bin/bash

# Ternary operator => condition && condition2 || condition3

age=18
[[ $age -ge 18 ]] && echo "Adult" || echo "Minor"

