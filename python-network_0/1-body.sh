#!/usr/bin/env bash
# Send a GET request and display body only if HTTP status code is 200
curl -s -L -w "\n%{http_code}" "$1" | awk 'BEGIN{RS="\n"; ORS=""} {lines[NR]=$0} END{if (lines[NR]=="200") {for (i=1; i<NR; i++) {print (i>1?"\n":"") lines[i]}}}'
