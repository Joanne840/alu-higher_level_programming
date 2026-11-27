#!/bin/bash
# Display the body of a 200 status code GET response after following redirects
code=$(curl -sL -o /tmp/curl_1_body -w "%{http_code}" "$1"); [ "$code" = "200" ] && cat /tmp/curl_1_body; rm -f /tmp/curl_1_body
