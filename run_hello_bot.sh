#!/usr/bin/env bash
REPO_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
NAME="hello_bot"

docker stop $NAME
docker rm -f $NAME
docker run -itd \
--name $NAME \
-p 5001:4040 \
-p 5002:5000 \
-v $REPO_DIR/hello_bot:/workspace \
-v $REPO_DIR/helpers:/workspace/helpers \
-v $REPO_DIR/config:/opt/config \
-e PYTHONPATH=/workspace/ \
--entrypoint /workspace/run.sh \
hello_bot $@
