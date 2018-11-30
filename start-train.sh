#!/bin/bash
cd ./local_test/
./build_local.sh
nohup ./train_local.sh > ../resources/log/train.log 2>&1 &