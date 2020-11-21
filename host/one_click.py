#!/usr/bin/env python3

import sys
import json
import struct
import os
import fileinput
import re
import shlex
try:
    # Python 3.x version
    # Read a message from stdin and decode it.
    def getMessage():
        print('Please wait while the program is loading...')
        rawLength = sys.stdin.buffer.read(4)
        if len(rawLength) == 0:
            sys.exit(0)
        messageLength = struct.unpack('@I', rawLength)[0]
        message = sys.stdin.buffer.read(messageLength).decode('utf-8')
        return json.loads(message)

    # Encode a message for transmission,
    # given its content.
    def encodeMessage(messageContent):
        encodedContent = json.dumps(messageContent).encode('utf-8')
        encodedLength = struct.pack('@I', len(encodedContent))
        print('************* Please wait while the program is loading...')
        return {'length': encodedLength, 'content': encodedContent}

    # Send an encoded message to stdout
    def sendMessage(encodedMessage):
        sys.stdout.buffer.write(encodedMessage['length'])
        sys.stdout.buffer.write(encodedMessage['content'])
        sys.stdout.buffer.flush()

    while True:
        receivedMessage = getMessage()
        if receivedMessage["login"] == "login":    
            sendMessage(encodeMessage("pong3 HELLO"))
            #os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
            f = open("auto_ssh.sh", "w")
            ip = receivedMessage["ip"]
            username = receivedMessage["username"]
            password = receivedMessage["password"]
            expect_path = "#!/usr/bin/expect"+"\n"
            ssh_command = "spawn ssh -o StrictHostKeyChecking=no "+username+"@"+ip+"\n";
            ask_pass = "expect \"password\""+"\n"
            line_break = "\nsend "+"\n"
            password=password.replace('\\','\\\\')
            password=password.replace('[','\[')
            password=password.replace(']','\]')
            
           # 
            password=password.replace('\'','\\\'')
            password=password.replace('\"','\\"')
            send_pass = "send \""+password+"\"\n"
            enter = "send "+"\"\\r\""+"\n"
            interact = "interact"
            #f.write(receivedMessage["password"])
            f.writelines([expect_path,ssh_command,ask_pass,send_pass,enter,interact])
            f.close()
            os.system("gnome-terminal -e 'bash -c \"./auto_ssh.sh;\"'")
            #cmd_to_run = "gnome-terminal -e 'sudo apt-get update'"
            #os.system(cmd_to_run)
except AttributeError:
    # Python 2.x version (if sys.stdin.buffer is not defined)
    # Read a message from stdin and decode it.
    def getMessage():
        rawLength = sys.stdin.read(256)
        if len(rawLength) == 0:
            sys.exit(0)
        messageLength = struct.unpack('@I', rawLength)[0]
        message = sys.stdin.read(messageLength)
        return json.loads(message)

    # Encode a message for transmission,
    # given its content.
    def encodeMessage(messageContent):
        encodedContent = json.dumps(messageContent)
        encodedLength = struct.pack('@I', len(encodedContent))
        return {'length': encodedLength, 'content': encodedContent}

    # Send an encoded message to stdout
    def sendMessage(encodedMessage):
        sys.stdout.write(encodedMessage['length'])
        sys.stdout.write(encodedMessage['content'])
        sys.stdout.flush()

    while True:
        receivedMessage = getMessage()
        if receivedMessage == "ping":
            sendMessage(encodeMessage("pong2 HELLO"))
