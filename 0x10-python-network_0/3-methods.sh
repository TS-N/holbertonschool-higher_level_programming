#!/bin/bash
# Displays all HTTP methods the server will accept
curl -s "$1" --head | grep  "Allow:" | cut -c 8-
