#!/bin/bash

for option in $(cowsay -l):
cowsay -f $option "echo"

