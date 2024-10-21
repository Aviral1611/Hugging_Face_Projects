from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# NSFW Image Detection API URL
NSFW_API_URL = "https://api-inference.huggingface.co/models/Falconsai/nsfw_image_detection"

API_KEY = os.getenv("HUGGING_FACE_API_KEY")

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/octet-stream'
}

# Function to send image data to the Hugging Face API
def query_image(image_data):
    response = requests.post(NSFW_API_URL, headers=headers, data=image_data)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        return {"error": "Model request failed", "status_code": response.status_code}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get the uploaded image file
    file = request.files['file1']
    
    # Read the image data
    image_data = file.read()

    # Send image data to the Hugging Face model API
    model_response = query_image(image_data)

    if "error" in model_response:
        return jsonify(model_response)

    # Format predictions for better readability
    predictions = [
        {'label': entry['label'], 'score': round(entry['score'] * 100, 2)} 
        for entry in model_response
    ]

    # Pass the predictions to be displayed on the page
    return render_template('index.html', predictions=predictions)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
