#!/usr/bin/env bash

./build.sh

docker save bondbidhie2024_algorithm_outcomenet | gzip -c > bondbidhie2024_algorithm_outcomenet.tar.gz
