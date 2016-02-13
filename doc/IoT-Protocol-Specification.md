# IoT Protocol Specification

> This file acts as a document to IoT Protocol.


## Overall

IoT Protocol is based on the JSON format to follow the idea of RESTful API.

It passes through TCP/UDP/HTTP Protocol.

Here's its detailed format:

```
{
    "proto": "iddp",
    "role": "<rolename>",
    "id": iot_id,
    "data": {<data items}
    <other items>
}

```


## role

> `role` implies which kind of message it is.
> It is be of format **action-content**


### action

* broadcast

Broadcast a message through UDP in LAN

* send

Post a message through TCP

* reply

Reply a message. Reply a broadcast by UDP and others by TCP

* pull

Ask for something from the cloud

* push

Send something to the cloud

* remote

Ask the cloud to deliver a message to the remote device.

### content

* discover

For IoT device discovery in LAN

