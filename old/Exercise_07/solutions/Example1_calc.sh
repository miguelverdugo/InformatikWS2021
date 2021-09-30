#/usr/bin/bash


# Take user Input 
echo "Enter operation : "
echo "example: 8 + 3 ; 5.5 * 2.4; 7 / 4.2 "
echo  " "
read operation
echo "scale=2; $operation" | bc


