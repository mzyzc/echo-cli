# echo-cli

`echo-cli` is a bare-bones client made as part of the [Echo secure messenger](https://github.com/mzyzc/echo) project.

It was originally created for debugging purposes so it does not currently include any high-level commands, making it a poor choice for everyday use. If that's what you want, try the [Flutter-based client](https://github.com/mzyzc/echo_client) instead.

## Usage

All commands are prefixed with a backslash (`\`). To check usage when running the program, use the `\help` command.

Commands follow this pattern, where words in ALL CAPS are variable:

```
\FUNCTION TARGET users:ID,EMAIL,NAME,PASSWORD,PUBLIC_KEY
                 messages:ID,DATA,MEDIA_TYPE,TIMESTAMP,SIGNATURE
                 conversations:ID,NAME
```

There are five `FUNCTION`s:

- CREATE
- READ
- UPDATE
- DELETE
- VERIFY

There are three `TARGET`s:

- USERS
- MESSAGES
- CONVERSATIONS

Following these is an arbitrary number of arguments in the format starting with `user`, `message`, or `conversastion` followed by a colon and a specific amount of comma-separated values. Multiple arguments of each type can be specified to represent multiple users, messages, or conversations.

Some values must be Base64-encoded. These are:

- `PUBLIC_KEY` for users
- `DATA` for messages
- `MEDIA_TYPE` for messages
- `TIMESTAMP` for messages
- `SIGNATURE` for messages

Media types follow the [MIME](https://en.wikipedia.org/wiki/Media_type) standard (e.g. `text/plain`) and timestamps follow the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard (e.g. `2014-02-15T08:57:47.812`).

## Typical usage

To register yourself for the first time, run this command (replacing the example values with your own):

Note: `a2V5` is the Base64-encoded value 'key'

`\create users user:,me@example.com,,p@$$w0rd,a2V5`

To log-in with an existing user:

`\verify users user:,me@example.com,,p@$$w0rd,`

To start a conversation with yourself and two other users:

`\create conversations conversation:,ConversationName user:,you@example.com,,, user:,who@example.com,,,`

To list all existing conversations:

`\read conversations`

To send one message in a conversation (more messages can be sent with multiple `message:` arguments):

`\create messages message:,dGhpcyBpcyBhIG1lc3NhZ2U=,dGV4dC9wbGFpbg==,MjAxNC0wMi0xNVQwODo1Nzo0Ny44MTI=,cHJldGVuZCB0aGlzIGlzIGEgdmFsaWQgc2lnbmF0dXJl conversation:1,`

To list all messages in a conversation:

`\read messages conversation:1,`
