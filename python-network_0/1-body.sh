#!/usr/bin/env bash
# Send a GET request and display body only if HTTP status code is 200
status=$(curl -s -L -o /tmp/curl_body.txt -w "%{http_code}" "$1")
if [ "$status" -eq 200 ]; then
    cat /tmp/curl_body.txt
fi
rm -f /tmp/curl_body.txt
