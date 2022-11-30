#!/bin/env bash

MODULE="$1"

if [[ -z $MODULE ]]
then
    poetry run pytest --cov
else
    poetry run pytest "$MODULE" --cov="$MODULE" --cov-report term-missing
fi
