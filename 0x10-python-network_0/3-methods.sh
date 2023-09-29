#!/bin/bash
# A Script that will take in a URL and displays all http method
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
