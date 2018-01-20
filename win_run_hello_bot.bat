set "NAME=hello_bot"

docker stop %NAME%
docker rm -f %NAME%
docker run -itd ^
--name %NAME% ^
-p 5001:4040 ^
-p 5002:5000 ^
-v %cd%\hello_bot:/workspace ^
-v %cd%\helpers:/workspace/helpers ^
-v %cd%\config:/opt/config ^
-e PYTHONPATH=/workspace/ ^
--entrypoint /workspace/run.sh ^
haskalpa/docker-spark-bot-example
