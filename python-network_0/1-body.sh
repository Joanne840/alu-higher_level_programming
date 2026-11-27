#!/bin/bash
# Display the body of a 200 status code GET response after following redirects
python3 -c 'import sys, urllib.request; r = urllib.request.urlopen(sys.argv[1]); sys.stdout.buffer.write(r.read()) if r.status == 200 else None' "$1"
