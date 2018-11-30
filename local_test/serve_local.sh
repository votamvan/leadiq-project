#!/bin/sh
rm ../resources/output/*
curr_folder=$(pwd)
parentdir="$(dirname "$curr_folder")"
docker run -v $parentdir/resources:/opt/ml -p 8080:8080 --rm test01 serve.py