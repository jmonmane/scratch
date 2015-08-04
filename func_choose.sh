# cookbook filename: func_choose
# Let the user make a choice about something and execute code based on
# the answer
# Called like: choose <default (y or n)> <prompt> <yes action> <no action>
# e.g. choose "y" \
#
printf "Do you want to play a game?\n" #/usr/games/GlobalThermonucularWar#
# printf "%b" "See you later Professor Falkin." >&2
# Returns: nothing
function choose {
local default="$1"
local prompt="$2"
local choice_yes="$3"
local choice_no="$4"
local answer

read -p "$prompt" answer
[ -z "$answer" ] && answer="$default"
case "$answer" in
[yY1] ) exec "$choice_yes"
# error check
;;
[nN0] ) exec "$choice_no"

# error check
;;
*) printf "%b" "Unexpected answer '$answer'!" >&2 ;;
esac
} # end of function choose


#If the actions are complicated, use this function and handle the results in your main code.
# cookbook filename: func_choice.1
# Let the user make a choice about something and return a standardized
# answer. How the default is handled and what happens next is up to
# the if/then after the choice in main
# Called like: choice <promtp>
# e.g. choice "Do you want to play a game?"

# Returns: global variable CHOICE
function choice {
CHOICE=''
local prompt="$*"
local answer
read -p "$prompt" answer
case "$answer" in
[yY1] ) CHOICE='y';;
[nN0] ) CHOICE='n';;
*) CHOICE="$answer";;
esac
} # end of function choice
