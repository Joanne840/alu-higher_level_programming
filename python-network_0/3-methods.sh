#!/usr/bin/env bash
# Display all HTTP methods the server will accept for a given URL
curl -s -I -X OPTIONS "$1" | grep -i '^Allow:' | sed 's/^[Aa][Ll][Ll][Oo][Ww]:[[:space:]]*//' | tr -d '\r\n' && echo ""
