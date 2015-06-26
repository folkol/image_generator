#!/bin/sh

inbox=$1
if test -z "$inbox"
then
    echo "Usage: $0 inbox_location"
    exit 1
fi

while :
do
    # Throttling
    while test $(ls -la $inbox | wc -l) -gt 20
    do
	sleep 1
    done

    name=$(mktemp).jpg
    echo "[$(date)] - Generating: $name"
    python gen_image.py $name
    mv $name ${inbox}
done
