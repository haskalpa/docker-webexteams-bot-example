# DockerSparkBotExample
This should get you started with a Cisco Spark Bot very quickly.

### Getting started with spark 
1. https://www.ciscospark.com/
2. click "Get Started Free" and make yourself an account

### How to get my first bot
1. go to: https://developer.ciscospark.com/apps.html
2. create yourself a new bot and make a note of "Bot's Access Token"

### Getting started
You need a machine with Docker. Both Linux and window are supported and should just work for Mac as well.
#### for installing Docker see
- https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/
- https://docs.docker.com/docker-for-windows/install/
- https://docs.docker.com/docker-for-mac/install/

### Technologies used

## Actually getting started
### 1. clone this repo recursively with submodules
```
git clone --recursive https://github.com/haskalpa/docker-spark-bot-example.git
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

### 5. In your spark client, make a room with your new bot adding it using bot's email address
say something to it. it should say hello back.

