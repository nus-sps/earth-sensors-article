#!/usr/bin/bash
INDEX_FILE=".last_index.txt"
tail -q -n 1 ~/"$INDEX_FILE"
read -s -t 5 -n 1 -p "Press any key to continue ..."
echo
