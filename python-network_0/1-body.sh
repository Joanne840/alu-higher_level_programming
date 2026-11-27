#!/bin/bash
# Display the body of a 200 status code GET response
curl -s -L -w "\n%{http_code}" "$1" | awk 'NR>1{print prev} {prev=$0} END{if ($0=="200") printf "%s", prev}'
