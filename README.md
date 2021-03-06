# hidonash website
![Test](https://github.com/SsmonZimmer/hidonash-website/workflows/tests/badge.svg?branch=master)

My artist website as a dockerized web app built with flask and nginx.


# installation on a fresh server
## public website
* install docker and docker-compose
* run `launch.sh` to initialize ssl certificationa and boot up docker containers via docker-compose
## content management system
* in an interactive docker shell, run `flask shell` and create a user and password
* login at `<url>/cms`

