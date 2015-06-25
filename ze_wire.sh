#!/bin/sh

inbox=$1
if test -z "$inbox"
then
    echo "Usage: nohup $0 inbox_location >> /mnt/wire.log &"
    exit 1
fi

while :
do
    name=out_$(date +%s).jpg
    echo "Generating $name"
    python gen_image.py $name
    mv $name $inbox
    sleep 10
done
