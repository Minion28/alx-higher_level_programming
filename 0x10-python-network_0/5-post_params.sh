#!/bin/bash
# script that takes in URL, sends POST request to the passed URL, and displays body of the response.
curl -sL "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
