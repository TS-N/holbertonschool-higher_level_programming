#!/bin/bash
# Reverse engineering to get "You got me!" in the body of the response
curl 0.0.0.0:5000/catch_me --request PUT -L --data "user_id=98"  --header "Origin: HolbertonSchool"
