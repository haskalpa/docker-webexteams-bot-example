# DockerWebexTeamsBotExample
This should get you started with a *Cisco WebexTeams Bot very quickly.

*used to be called Cisco Spark

### Getting started with Cisco Webex Teams 
1. https://www.webex.com/products/teams/index.html
2. click "Sign In" and enter your email address. Then follow the instructions presented.

### How to get my first bot
1. go to: https://developer.webex.com/my-apps
2. create yourself a new bot and make a note of **Bot's Access Token NOT ID** (you'll need to scrolldown)

### Getting started
You need a machine with Docker. Both Linux and window are supported and should just work for Mac as well.
#### for installing Docker see
- https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/
- https://docs.docker.com/docker-for-windows/install/
- https://docs.docker.com/docker-for-mac/install/

### Technologies used
#### 1. Docker
The most trendy container technology for running modern software apps particulalry in the cloud.

read up more @ https://www.docker.com/what-docker

#### 2. Ngrok
**problem**: for events between Webex Teams Cloud Services and your bot, you need a public interface (webhook) where you can recieve events about new messages ect.

You can setup a cloud instances which can be good for a production version of your bot but for development turnaround your laptop makes a lot of sense. And ngrok is pretty neat, in the sense that you can have a public listening web interface from your machine behind a NAT.

read up more @ https://ngrok.com/product

## Actually getting started
### 1. clone this repo recursively with submodules
```
git clone --recursive https://github.com/haskalpa/docker-webexteams-bot-example.git
```
### 2. make new config file with your new Bot's Access Token
may be:
```
cd config/
cp config_example.yaml config.yaml
vim config.yaml
```

### 3. build
```
./build.sh 
```
#### windows only
```
win_build.bat
```

### 4. run your bot
```
./run_hello_bot.sh 
```
#### windows only
```
win_run_hello_bot.bat
```

### 5. In your Webex Teams client, make a room with your new bot adding it using bot's email address
say something to it. it should say hello back.

# cheatsheet
## seeing stdout/stderr from container
```
docker logs -f hello_bot
```

## how to get a shell into the container
```
docker exec -it hello_bot bash
```

## fastest way to tinker around the bot
1. shell into container
2. kill the python bot script
3. run it on your shell in foreground
4. ctrl+c
5. hack

repeat 3,4,5 as please
```
ubuntu@haskalpa-01:~/workspace/docker-spark-bot-example$ docker exec -it hello_bot bash
root@d9d108bf3ae6:/workspace# ps auxw
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0  18028  2948 pts/0    Ss   11:45   0:00 bash /workspace/run.sh
root         7  0.2  0.0  20536 14676 pts/0    Sl   11:45   0:00 ngrok http 5000 -bind-tls=true -config /opt/config/ngrok.yaml -log=
root        23  0.1  0.2 103268 40200 pts/0    S    11:45   0:00 python hello_bot.py <------------
root        24  0.0  0.0  18236  3296 pts/0    S+   11:45   0:00 bash
root        34  0.0  0.0  18240  3384 pts/1    Ss   11:49   0:00 bash
root        44  0.0  0.0  34424  2808 pts/1    R+   11:49   0:00 ps auxw
root@d9d108bf3ae6:/workspace# kill 23
root@d9d108bf3ae6:/workspace# ps auxw 
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0  18028  2948 pts/0    Ss   11:45   0:00 bash /workspace/run.sh
root         7  0.2  0.0  20536 15160 pts/0    Sl   11:45   0:01 ngrok http 5000 -bind-tls=true -config /opt/config/ngrok.yaml -log=
root        24  0.0  0.0  18236  3296 pts/0    S+   11:45   0:00 bash
root        34  0.0  0.0  18240  3384 pts/1    Ss   11:49   0:00 bash
root        45  0.0  0.0  34424  2796 pts/1    R+   11:54   0:00 ps auxw  
root@d9d108bf3ae6:/workspace# python hello_bot.py 
```

# Looking for Ideas to improve
### Cisco Webex Team Depot
Cisco Webex Team  is relatively new but there are some public bot listing @ https://apphub.webex.com/

> A Webex Team's bot can be a nice enhancement to get your application's functionality, interacting collaborating in a leading enterprise collaboration platform. 
