#!/usr/bin/env bash

docker build -t streamlit-mushroom-app:latest -f docker/Dockerfile .


aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 414252687335.dkr.ecr.us-east-1.amazonaws.com

docker tag streamlit-mushroom-app:latest 414252687335.dkr.ecr.us-east-1.amazonaws.com/streamlit-mushroom-app:latest

docker push 414252687335.dkr.ecr.us-east-1.amazonaws.com/streamlit-mushroom-app:latest

echo "✅ Success build and push to ECR"