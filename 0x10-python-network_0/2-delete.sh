#!/bin/bash
# A Script that sends a del request to the url passed as the first argument
curl -s "$1" -X DELETE
