# NEONE Server Setup - Notification Handler

The neone-flask repository is an alternative configuration that includes a Flask app to listen to incoming notifications to port 5000 in your server. The Flask app serves as a customizable notification handler. You can adapt it to process incoming notifications from the NEONE server and integrate them with your internal systems

Go to the main [neone repository](https://github.com/astein-iamovers/neone) if you have your own NOTIFICATION_ENDPOINT (ensure it has the "/notification" suffix).

## Notifications

ONE Record requires each server to implement a notifications endpoint to receive notifications from other ONE Record servers. While the NEONE server includes a notifications endpoint, processing and integrating notifications into your systems is beyond the scope of ONE Record. This flexibility allows companies to define their own rules and workflows for handling notifications. The NEONE Server stores notifications as objects and allows you to forward them to your own custom NOTIFICATION_ENDPOINT. In the current version, NEONE expects the notification endpoint to end with "/notifications".

The following setup creates a notification-handler service using Flask to receive these notifications and process them according to your needs.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Git](https://git-scm.com/downloads) installed
- Have your variables handy to update the .env file

## Step by step guide

1) Clone this repository
   ```bash
   git clone https://github.com/astein-iamovers/neone-flask.git
   ```
2) Switch to the directory neone-flask
   ```bash
   cd neone-flask
   ```
3) If you have Mac or Linux, please reset folder permissions to allow cross-container dependencies.
   ```bash
   chmod -R 755 ./
   ```
4) Modify your .env file with the nano editor.
   ```bash
   nano .env
   ```
   Paste your variables
   - BASE_1R_HOST: the URL of your ONE Record Server
   - CLIENT_ID: given by IAM
   - CLIENT_SECRET: given by IAM
   - AUDIENCE: given by IAM

5) Optional: modify the Flask app according to your needs

6) Start all services with [docker compose](https://docs.docker.com/compose/)
   ```bash
   sudo docker compose up -d
   ```
7) Wait until all containers are up and running:
   ```bash
   [+] Running 6/6
    ✔ Network docker-compose_default            Created
    ✔ Container docker-compose-graph-db-1       Healthy
    ✔ Container docker-compose-graph-db-setup-1 Started
    ✔ Container docker-compose-ne-one-server-1  Healthy
    ✔ Container neone-ne-one-play-1             Started
    ✔ Container neone-ne-one-view-1             Started
    ✔ Container notification-handler-1          Started
        
    
   ```
8) Try to access the ONE Record Server by http://{BASE_1R_HOST}:8080 using your favorite browser (replace {BASE_1R_HOST} with your configured host value in the .env file)
   Accessing http://{BASE_1R_HOST}:8080 in your browser should return an HTTP 401 error, indicating the server is running but requires authentication. This confirms the NEONE server is correctly set up.

# Overview of services

| Name | Description | Base URL / Admin UI |
|-|-|-|
| ne-one-server | [ne-one server](https://git.openlogisticsfoundation.org/wg-digitalaircargo/ne-one) | http://{BASE_1R_HOST}:8080 |
| ne-one-view | [ne-one view](https://git.openlogisticsfoundation.org/wg-digitalaircargo/ne-one-view) | http://{BASE_1R_HOST}:3000 |
| ne-one-play | [ne-one play](https://github.com/aloccid-iata/neoneplay) | http://{BASE_1R_HOST}:3001 |
| graphdb | GraphDB database as database backend for ne-one-server-1 repository neone | http://{BASE_1R_HOST}:7200 |
| notification-handler | Flask app listening on port 5000 to process incoming notifications | http://{BASE_1R_HOST}:5000 |

