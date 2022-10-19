#!/bin/bash
# POST request to a URL passethe first argument, and displays the body of the response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
