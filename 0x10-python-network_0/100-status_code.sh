#!/bin/bash
# Displays status code only using no pipes redirection ';' nor '&&'
curl -s --write-out %{http_code} -o /dev/nullcurl "$1"
