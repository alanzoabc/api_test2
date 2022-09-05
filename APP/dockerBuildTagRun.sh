#! /bin/bash
docker build -t App .

sleep 3

docker run -d --name App -p 80:80 App