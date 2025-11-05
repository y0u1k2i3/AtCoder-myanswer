#!/bin/sh

cd $WORKSPACE_FOLDER/contests

acc new $1

cd $1/a && code -r main.py
