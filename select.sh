#!/bin/bash

PS3='Choose stuff'
LIST="1 2 3 4"
select var in $LIST
do
echo "var"
echo ""
break
done
