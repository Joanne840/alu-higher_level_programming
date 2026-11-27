#!/bin/bash
# Display all HTTP methods the server will accept
curl -s -i -X OPTIONS "$1" | grep -i '^Allow:' | sed 's/^[Aa][Ll][Ll][Oo][Ww]:[[:space:]]*//' | tr -d '\r'
