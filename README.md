# hidonash website
[![tests](https://github.com/SimonZimmer/hidonash-website/actions/workflows/main.yml/badge.svg)](https://github.com/SimonZimmer/hidonash-website/actions/workflows/main.yml)

This is the source for my website as a dockerized web app built with flask, gunicorn and nginx.

![website](https://user-images.githubusercontent.com/28354711/110207566-9ffef080-7e84-11eb-9f73-e4442e43c837.gif)

# Installation

## public website
* install docker and docker-compose
* run `launch.sh` to initialize ssl certificationa and boot up docker containers via docker-compose
## content management system
* in an interactive docker shell, run `flask shell` and create a user and password
* login at `<url>/login` to add content
