#!/bin/bash
# Sends a JSON POST request
curl -s --header "Content-Type: application/json" --data @"$2" "$1"
