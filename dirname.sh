echo "$(dirname "$1")"
echo "$(cd "$(dirname "$1")" && pwd)"
echo $(basename "$1")
