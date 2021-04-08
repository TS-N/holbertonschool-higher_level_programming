#!/bin/bash
# Send a request with a custom header variable
curl -s "$1" --header "X-HolbertonSchool-User-Id:98"
