from flask import Flask, jsonify, request
import numpy as np
import PIL
from PIL import Image
from keras.models import load_model

app = Flask(__name__)

model = load_model('/var/www/flaskapi/flaskapi/model.h5')

@app.route('/predict', methods=["POST"])
def predict_image():
        # Preprocess the image so that it matches the training input
        image = request.files['file']
        image = Image.open(image)
        image = np.asarray(image.resize((28,28)))
        image = image.reshape(1,1,28,28)

        # Use the loaded model to generate a prediction.
        pred = model.predict(image)

        # Prepare and send the response.
        digit = np.argmax(pred)
        prediction = {'digit':int(digit)}
        return jsonify(prediction)

if __name__ == "__main__":
        app.run()