#!/usr/bin/expect
spawn ssh -o StrictHostKeyChecking=no master_abeuctztpc@188.166.180.134
expect "password"
send "cS87ynw4"
send "\r"
interact