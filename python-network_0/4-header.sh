#!/usr/bin/env bash
# Send a GET request with header X-HolbertonSchool-User-Id: 98 and display body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
