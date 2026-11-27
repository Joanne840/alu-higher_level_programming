#!/usr/bin/env bash
# Send a DELETE request to the URL passed as the first argument and display body
curl -s -X DELETE "$1"
