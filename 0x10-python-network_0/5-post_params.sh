#!/bin/bash
# Sends a POST requests with custom data/form
curl -s "$1" --data "email=hr@holbertonschool.com&subject=I will always be here for PLD"
