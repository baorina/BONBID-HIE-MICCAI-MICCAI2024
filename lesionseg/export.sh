#!/usr/bin/env bash

./build.sh

docker save bondbidhie2024_algorithm_segnet | gzip -c > bondbidhie2024_algorithm_segnet.tar.gz
