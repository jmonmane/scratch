#!/bin/bash
files=$(ls)
select file in $files
until [ -n "$file" ]; do
echo $file
done
