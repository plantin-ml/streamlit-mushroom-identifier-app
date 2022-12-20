import io
import os
import requests
import streamlit as st
import pandas as pd
from PIL import Image

API_CLASSIFICATOR_ENDPOINT = os.getenv("API_CLASSIFICATOR_ENDPOINT")
API_DETECTION_ENDPOINT = os.getenv("API_DETECTION_ENDPOINT")

if API_CLASSIFICATOR_ENDPOINT is None or API_DETECTION_ENDPOINT is None:
    exit('You have to define `API_CLASSIFICATOR_ENDPOINT` and `API_DETECTION_ENDPOINT`')

# API_CLASSIFICATOR_ENDPOINT = "http://172.16.65.32:3000/predict_by_file"
# API_DETECTION_ENDPOINT = "http://172.16.65.32:3001/render"

st.title("🍄 Mushroom classification")


def predict(img):
    """
    A function that sends a prediction request to the API and return a cuteness score.
    """
    # Convert the bytes image to a NumPy array
    bytes_image = img.getvalue()

    # Send the image to the API
    response = requests.post(
        API_CLASSIFICATOR_ENDPOINT,
        files = {"upload_files": ("test.jpg", io.BytesIO(bytes_image), "image/png")},
        auth=('plantin', 'k26vKCddex')
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Status: {}".format(response.status_code))

def main():
    img_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if img_file is not None:
        # 🤖
        with st.spinner("🧐 Predicting..."):
            prediction = predict(img_file)
            res = pd.DataFrame.from_dict(prediction, orient='index')
            result_class = res.idxmax()[0]
            st.success(f"{result_class} ({res.max()[0]:.2f})")

            response_detection = requests.post(
                API_DETECTION_ENDPOINT,
                files = {"upload_files":  ("test.jpg", io.BytesIO(img_file.getvalue()), "image/png")},
                auth=('plantin', 'k26vKCddex')
            )
            st.image(Image.open(io.BytesIO(response_detection.content)), use_column_width=True)

if __name__ == "__main__":
    main()