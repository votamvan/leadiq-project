#!/bin/sh
curr_folder=$(pwd)
parentdir="$(dirname "$curr_folder")"
docker run -v $parentdir/resources:/opt/ml --rm test01 train.py