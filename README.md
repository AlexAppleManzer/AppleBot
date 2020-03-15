# AppleBot
Applebot, the number one fruit powered discord bot.
This is a discord bot setup for my personal use and memes. If you want to contribute, go ahead.

## Deployment
Any commits on master will be deployed to azure via github actions. 

## setup
All you need is python 3.8+. 
- setup your venv with requirements.txt
- add these enviromental variables in a .env file in the root project directory
```
DISCORD_TOKEN={discord bot token}
RIOT_API_KEY={riot games api key (optional if you want riot api things to work)}
```
- run AppleBot.py to start!

`python AppleBot.py`
- you are up and running :fire:

## testing docker
to build this on docker, use the dockerfile to build an image

`docker image build -t applebot:1.0 .`

to run the image in a container

`docker container run --detach --name ab applebot:1.0`
