#!/bin/sh

# Check if tests passed
if test ; then
    source submit.sh
else
    echo "Tests failed. Please fix errors before submitting."
fi
