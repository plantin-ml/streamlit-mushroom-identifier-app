FROM python:3.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501

ENV API_CLASSIFICATOR_ENDPOINT /predict_by_file
ENV API_DETECTION_ENDPOINT /render

COPY src/app.py .
ENTRYPOINT ["streamlit", "run"]
CMD ["app.py", "--server.address=0.0.0.0", "--server.port=8501"]

# docker build -t streamlitapp:latest -f docker/Dockerfile .
# docker run -p 8501:8501 -e "API_CLASSIFICATOR_ENDPOINT=http://mushroom-classification.models.ml.myplantin.com/predict_by_file" -e "API_DETECTION_ENDPOINT=http://mushroom-detection.models.ml.myplantin.com/render" streamlitapp:latest

