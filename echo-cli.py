#!/usr/bin/env python3

import socket
import ssl
import json

HOSTNAME = 'czyz.xyz'
PORT = 63100
CONTEXT = ssl.create_default_context()

def prompt():
        while True:
            try:
                message = input('echo> ')

                # Blank inputs close the connection
                if len(message) == 0:
                    break;
                # Help messages
                elif message == '\\help':
                    print("""\FUNCTION TARGET
                     user:ID,EMAIL,NAME,PASSWORD,PUBLICKEY
                     message:ID,DATA,MEDIATYPE,TIMESTAMP,SIGNATURE,SENDER
                     conversation:ID,NAME
                    """)
                # Inputs that start with \ are commands
                elif message[0] == '\\':
                    parsed = parse_command(message)
                    output = json.dumps(parsed, indent=2)

                ssock.sendall(bytes(output, 'utf-8'))
            except Exception as e:
                print(e)

def parse_command(command):
    # Remove backslash prefix and split on spaces
    command_list = command[1:].split()
    function, target, *args = command_list

    users = []
    messages = []
    conversations = []

    for arg in args:
        target, values = arg.split(':')
        values = values.split(',')

        d = {}

        if target == 'user':
            d['id'], d['email'], d['name'], d['password'], d['publicKey'], *_ = values
            users.append(d)
        elif target == 'message':
            d['id'], d['data'], d['mediaType'], d['timestamp'], d['signature'], d['sender'], *_ = values
            messages.append(d)
        elif target == 'conversation':
            d['id'], d['name'], *_ = values
            conversations.append(d)

    return {
        'function': f'{function} {target}',
        'users': users,
        'messages': messages,
        'conversations': conversations,
    }


with socket.create_connection((HOSTNAME, PORT)) as sock:
    with CONTEXT.wrap_socket(sock, server_hostname=HOSTNAME) as ssock:
        print(ssock.version())
        prompt()

print('Terminating...')
