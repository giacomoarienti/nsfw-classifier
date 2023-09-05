from transformers import pipeline
from flask import Flask, jsonify, request
from PIL import Image


pipe = pipeline("image-classification", model="giacomoarienti/nsfw-classifier")
app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def index():
    file = request.files['image']
    image = Image.open(file)
    response = pipe(image)
    return jsonify(response)


app.run()
