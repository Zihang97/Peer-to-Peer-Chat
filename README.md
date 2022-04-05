# EC530_Peer-to-Peer-Chat

This project implement a Peer-to-Peer command-line chat in python. 

Set up a P2P Chat server and allow multiple clients to connect to it using a client-side script. 
Clients use the socket port to communicate with the server socket. 

## MVP

##### Discovery

You register by making yourself findable by others (as in Telegram or Whatsapp) 

##### Session 

InitiationSend a message to users who you want to connect with

##### Communication and Synchronization

You can live connect with any of your friends who is available now.For users who are not available (offline), you can write messages, which are stored on your own client.The data for offline users will be synchronized when both users are discoverable.

##### Security

All is hashed



## User stories 

- I, the client, should be able to send messages to each other and edit them.
- I, the client, should be able to see contacts and choose one or many to chat with, 
- I, the client, should be able to block other users .
- I, the client, should be able to see the chat history. 
- I, the client, should be able to upload images or files to others.
- I, the client, should be able to read the transcription of the voice messages and should be able to search them.
- I, an AI developer, should be able to access the data anonymized.



## Getting started



```python
p2p.py
server.py
client.py
```



## To do