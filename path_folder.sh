#!/bin/bash

# files = {example01/py_test.py example02/py_test.py}

va=$(python3 path_folder.py $1 $2)

echo $va


# String
text=$1

# Set space as the delimiter
IFS=' '

# Read the split words into an array
# based on space delimiter
read -ra newarr <<< "$text"



# Print each value of the array by using
# the loop
for val in "${newarr[@]}";
do
 echo "$val"
done