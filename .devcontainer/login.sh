#!/bin/sh

expect -c "
set timeout 3
spawn acc login
expect \"? username:\"
send \"${ATCODER_USERNAME}\n\"
expect \"? password:\"
send \"${ATCODER_PASSWORD}\n\"
expect \"$\"
exit 0
"
oj login https://atcoder.jp -u $ATCODER_USERNAME -p $ATCODER_PASSWORD

# expect -c "
# set timeout 3
# spawn oj login https://atcoder.jp
# expect \"Username:\"
# send \"${ATCODER_USERNAME}\n\"
# expect \"Password:\"
# send \"${ATCODER_PASSWORD}\n\"
# expect \"$\"
# exit 0
# "
