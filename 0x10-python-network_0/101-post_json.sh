#!/bin/bash
# A Script that delivers a JSON POST request to a url passed as the first argument
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
