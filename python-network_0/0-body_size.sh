#!/usr/bin/env bash
# Display the size of the response body in bytes for a given URL
curl -s -o /dev/null -w '%{size_download}\n' "$1"
