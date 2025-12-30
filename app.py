from flask import Flask, render_template, request
import tensorflow as tf
import joblib
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load model
clf = joblib.load("model/classifier.pkl")
feature_extractor = tf.keras.models.load_model(
    "model/mobilenet_feature_extractor.h5"
)

LABELS = ["Apple", "Orange"]

def preprocess_image(img):
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        file = request.files.get("image")
        if file:
            img = Image.open(file).convert("RGB")
            img = preprocess_image(img)

            features = feature_extractor.predict(img)
            pred = clf.predict(features)[0]
            prediction = LABELS[pred]

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
