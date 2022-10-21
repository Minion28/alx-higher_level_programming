#!/bin/bash
# script that takes in a URL as an argument, sends a GET request to it, and displays the body of the response.
curl -s -H "X-HolbertonSchool-User-Id: 98" -X GET "$1"
