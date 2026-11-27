#!/usr/bin/env bash
# Display all HTTP methods the server will accept for a given URL
curl -s -i -X OPTIONS "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
