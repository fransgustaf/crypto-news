#!/bin/sh
googler --json -l en -n 3 -t h1 --site https://news.google.com cryptocurrency|python parse_google_result.py
# ddgr --json -n 3 -t h1 cryptocurrency|python parse_google_result.py
