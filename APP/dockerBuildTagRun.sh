#! /bin/bash
docker build -t app .

sleep 3

docker run -d --name app -p 80:80 app