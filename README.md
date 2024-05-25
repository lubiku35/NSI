# NSI - Miniprojects

> *Author*: motoslub

The goal of the mini-projects is to create a complex IoT application.

# Mini-Project 05

> *Branch*: mini_project_05

## Overview

This project involves setting up a local MQTT broker, a Raspberry Pi Pico to publish messages to the broker, and a Flask application to read and store the data for further use. The system is designed to enable seamless communication between devices and the web application, facilitating data storage and access through a user-friendly interface.

## Components

### Local MQTT Broker:

A local MQTT broker is set up to facilitate message communication between the Raspberry Pi Pico and the Flask application.
The broker listens on a specified port and handles incoming messages on predefined topics.

### Raspberry Pi Pico:

A script is deployed on the Raspberry Pi Pico to send messages to the local MQTT broker.
The Pico publishes messages to a specific topic (/data) at regular intervals or based on certain conditions.

### MQTT Microservice:

A lightweight Python script acts as an MQTT subscriber microservice.
This script subscribes to the /data topic on the local MQTT broker.
It captures incoming messages and makes them available to the Flask application through a shared variable or function.

## Workflow

### Message Publishing:

The Raspberry Pi Pico, running a custom script, generates data and publishes it to the local MQTT broker on the /data topic.

### Message Subscription:

The MQTT microservice subscribes to the /data topic on the local MQTT broker.
It receives and processes incoming messages, storing the latest message in a shared variable.