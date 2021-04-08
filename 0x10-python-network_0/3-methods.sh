#!/bin/bash
# Displays all HTTP methods the server will accept
curl -s "$1" --request OPTIONS --head | grep  "Allow:" | cut -c 8-
