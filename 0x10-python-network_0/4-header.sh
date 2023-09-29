#!/bin/bash
# A Script that takes in a url as an argument, sends a get request to the url
curl -s "$1" -H "X-School-User-Id: 98"
