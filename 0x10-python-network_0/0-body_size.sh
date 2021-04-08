#!/bin/bash
# Displays the size of the response only
curl --write-out "%{size_download}\n" --silent --output /dev/null "$1"
