#!/usr/bin/env bash
SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

docker build -t bondbidhie2024_algorithm_outcomenet "$SCRIPTPATH"
