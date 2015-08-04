
# dash - print a line of dashes
# options: # how many (default 72)
#
# -c X use char X instead of dashes
#
function usagexit ( )
{
printf "usage: %s [-c X] [#]\n" $(basename $0)
exit 2
} >&2
LEN=72
CHAR='-'
while (( $# > 0 ))
do
case $1 in
[0-9]*) LEN=$1;;
-c) shift
CHAR=$1;;
*) usagexit;;
esac
shift
done
if (( LEN > 4096 ))
then
echo "too large" >&2
exit
fi
# build the string to the exact length
DASHES=""
for ((i=0; i<LEN; i++))
do
DASHES="${DASHES}${CHAR}"
done
printf "%s\n" "$DASHES"
