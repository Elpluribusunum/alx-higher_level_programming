#!/bin/bash 
# A Script that sends a request to a url passed as an argument, display
curl -s -L -X HEAD -w "%{http_code}" "$1"
