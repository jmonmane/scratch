#!/bin/bash

options="Done $(ls .)"
printf "\nSelect a file to process:\n"
select option in $options
do
md5sum "$option"
done
