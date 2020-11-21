#!/usr/bin/expect 
send "!@#$%^&*()_+{}|[]\:\";\'./>?\'\'\"\"aA1/.,?><"
send "\n"
spawn ssh -o StrictHostKeyChecking=no master_vckgzubnpu@161.35.34.26
expect "password"
send "!@#$%^&*()_+{}|[]\:\";\'./>?\'\'\"\"aA1/.,?><"
send "\r"
interact






