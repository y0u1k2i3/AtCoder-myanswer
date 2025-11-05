#!/bin/sh

cd $WORKSPACE_FOLDER/practices

acc new $1

cd $1/a && code -r main.py
