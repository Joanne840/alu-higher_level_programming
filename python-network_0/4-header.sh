#!/bin/bash
# Send a GET request with X-HolbertonSchool-User-Id header set to 98
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1"
