#!/bin/sh

FILES_DIR="/home/tbeauman/Documents/42Projects/webserv/_siths/shit_web/shit_files/"

echo "Content-Type: application/json"
echo ""

files=$(ls "$FILES_DIR" 2>/dev/null | while read f; do
    if [ -f "$FILES_DIR$f" ]; then
        echo "\"$f\""
    fi
done | paste -sd ',' -)

echo "[$files]"