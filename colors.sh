#!/bin/bash - 
#===============================================================================
#
#          FILE: colors.sh
# 
#         USAGE: ./colors.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: YOUR NAME (), 
#  ORGANIZATION: 
#       CREATED: 07/13/2015 22:31
#      REVISION:  ---
#===============================================================================

set -o nounset                              # Treat unset variables as an error
#!/bin/bash
 
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.
 
for fgbg in 38 48 ; do #Foreground/Background
	for color in {0..256} ; do #Colors
		#Display the color
		echo -en "\e[${fgbg};5;${color}m ${color}\t\e[0m"
		#Display 10 colors per lines
		if [ $((($color + 1) % 10)) == 0 ] ; then
			echo #New line
		fi
	done
	echo #New line
done
 
exit 0

