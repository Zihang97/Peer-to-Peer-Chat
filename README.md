# EC530_Peer-to-Peer-Chat

This project implements a Peer-to-Peer command-line chat in python. 
We create a P2P Chat server based on the TCP system and allow multiple clients to connect to it using a client-side script. Clients use the socket port to communicate with the server socket. 



## MVP

#### Discovery

Clients register by making themselves findable by others (as in Whatsapp).

#### Session Initiation 

Send a message to users who you want to connect with.

#### Communication and Synchronization

Clients can live-chat with any of their friends who is available now. For users who are not available (offline),  clients can write messages stored on their own ends. The data for offline users will be synchronized when both users are discoverable.

#### Security

All is hashed



## User stories 

- I, the client, should be able to send messages to each other.

- I, the client, should be able to see contacts and choose one or many to chat with. 

- I, the client, should be able to block other users .

- I, the client, should be able to see the chat history. 

- I, the client, should be able to upload images or files to others.

- I, the client, should be able to read the transcription of the voice messages and should be able to search them.

- I, an AI developer, should be able to access the data anonymized.

  


## Achitecture
- TCP Peer to Peer network supports end-to-end communication.

- Local database to store data (e.g.,MySQL).

  

## Feature

##### Multi-Processing

Users can chat with multi-person concurrently by multi-threading. Every user connecting to the server creates a separate thread and communicates with the server on an individual thread based on the socket instance. In each thread, the server awaits a message and sends that message to other users currently on the chat. 

##### Discovery and mute

Users can decide their state of discovery. When a user is discovered, clients can send them any updates or new chats. When a user is not discovered, the messages sent to him are pending, so users are able to block other users.

##### Asynchronous 

Asynchronous messaging allows users to send messages to recipients not currently online but received once online.

##### History

Each user has a local database to store their chat history so that they can display or search chat history.



## Results
The screenshot below shows the concurrent chat from the server's side. 

<img src="pictures/server.png" width=500>



The screenshot below shows how to set up a p2p connection from the client's side.

<img src="pictures/connect.png" width=500>



The screenshot below shows the chat from Client One.

<img src="pictures/client1.png" width=500>



The screenshot below shows the chat from Client Two.

<img src="pictures/client2.png" width=500>



The screenshot below shows the chat from Client Three. 

<img src="pictures/client3.png" width=500>





## Database Schema

Each client of peer-to-peer chat system has a local database belong to him uniquely. ***User*** table is like an address book, which stores his contacts and corresponding ip addresses. ***Receiver*** table stores all the messages received. ***Sender*** table stores all the messages he sent or want to send. Compared to ***Receiver*** table, ***Sender*** table has a unique column `status` with two values `pending` and `sent`. If the client doesn't want to be discovered, he can still send messages but all these messages will be stored with status `pending`. Next time when he wants to be discovered, all pending messages will be sent and then status `pending` will be change to `sent`.

### User table
| Field  | Type   |Null | Key | Default | Extra |
|------  |---------|-----| -----| -----|-----|
|name| varchar(40)   | YES | | NULL| |
|ip|  varchar(40)  | YES | |NULL | |
|port |   varchar(20)     | YES| | NULL| |

### Sender table
| Field  | Type   |Null | Key | Default | Extra |
|------  |---------|-----| -----| -----|-----|
|ip|  varchar(40)  | YES | |NULL | |
|port |   varchar(20)     | YES| | NULL| |
|name| varchar(40)   | YES | | NULL| |
|message| varchar(40)   | YES | | NULL| |
|status| varchar(40)   | YES | | NULL| |
|time| varchar(40)   | YES | | NULL| |

### Receiver table
| Field  | Type   |Null | Key | Default | Extra |
|------  |---------|-----| -----| -----|-----|
|ip|  varchar(40)  | YES | |NULL | |
|port |   varchar(20)     | YES| | NULL| |
|name| varchar(40)   | YES | | NULL| |
|message| varchar(40)   | YES | | NULL| |
|time| varchar(40)   | YES | | NULL| |

