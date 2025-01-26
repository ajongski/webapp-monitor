# webapp-monitor
Monitor a webapp and notify admin if down. This is a simple project that illustrates how a webapp's health can be monitored.

## This uses the following:
- Flask for a simple webapp
- Python for the script
- Linux as the base system
- Docker for running the containerized version of the project

## How it works
- The system will check every minute for the health of the webapp
- If the webapp is down, it will send an email notification to the "administrator"
- If the webapp takes longer than **`10 seconds`** to response, it will also send an email notification to the "administrator"

## Pre-requisites:
- Docker and Docker compose installed in local or virtual machine
  - You may visit https://docs.docker.com/manuals/ to install Docker on your machine
- Local or virtual machine may be x86-64 or ARM64 based
- Email account supporting SMTP
  - For testing purposes, you may create an account in https://www.mailslurp.com/ to set up test email accounts (Note: For best results, sender email and recepient email **`MUST`** be in your MailSlurp account)
  - As of January 2025, GMail no longer allows using Less Secure Apps on personal accounts

## To start:
- Clone this repo:
```
git clone https://github.com/ajongski/webapp-monitor.git
```
- Inside the local copy of the repo, create a copy of the **`smtp_email_credentials`** and rename it to **`.env`**
- Provide the necessary credentials for the SMTP email in the .env file
- Assuming Docker and Docker is available on your machine, run in the termin the following command:
```
docker compose up
```
or to run in dettached mode,
```
docker compose up -d
```
- Once up and running, open **`http://localhost:8000`**, to confirm that the webapp is running

## Simulate downtime
- In the terminal, go inside the webapp container
```
docker exec -it webapp-monitoring-1 /bin/sh
```
and kill the Flask process:
```
service flask kill
```
- Wait for a minute or so for the email notification about the health status

## Troubleshooting
- In case there are changes made to any of the files in the local repo, delete first the containers and images created by the running the **`docker compose`** command
It should look like this:
```
docker compose rm webapp-monitoring-1
```
and
```
docker rmi [image ID of the webapp]
```
