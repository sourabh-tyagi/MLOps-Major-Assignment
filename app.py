from flask import Flask, render_template, request
from flask import send_from_directory
from joblib import load
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = load("savedmodel.pth")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    image_path = None

    if request.method == "POST":

        file = request.files["image"]

        if file:

            filepath = os.path.join(
                UPLOAD_FOLDER,
                file.filename
            )

            file.save(filepath)

            img = Image.open(filepath).convert("L")
            img = img.resize((64, 64))

            img_array = np.array(
                img,
                dtype=np.float32
            )

            img_array = img_array / 255.0
            img_array = img_array.reshape(1, -1)

            pred = model.predict(img_array)

            prediction = (
                f"Predicted Face Class: {pred[0]}"
            )

            image_path = filepath

    return render_template(
        "index.html",
        prediction=prediction,
        image_path=image_path
    )

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(
        UPLOAD_FOLDER,
        filename
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )