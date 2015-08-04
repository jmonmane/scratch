#!/bin/bash
sudo cp /var/log/boot.log ~/logs/`date +%F`-boot.log
DIFF=$(diff ~/logs/`date +%F`-boot.log ~/logs/boot.log)
if [ -n $DIFF ]; then
echo $DIFF
else
echo "No Diff"
fi
exit
