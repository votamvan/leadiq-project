#!/bin/bash
cd ./local_test/
./build_local.sh
rm -f nohup.out
nohup ./serve_local.sh &