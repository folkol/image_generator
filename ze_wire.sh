#!/bin/sh

inbox=$1

if [ -z "$inbox" ]
then
    echo "Usage: $0 inbox_location"
    exit 1
fi

throttle() {
    while [ $(ls -la $inbox | wc -l) -gt 20 ]
    do
	sleep 1
    done
}

while :
do
    throttle

    name=$(mktemp).jpg
    echo "[$(date)] - Generating: $name"
    python gen_image.py $name
    mv $name ${inbox}
done
