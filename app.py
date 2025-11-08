import os
from flask import Flask, request, jsonify, render_template
from langdetect import detect_langs, DetectorFactory
from flask_cors import CORS
from utils import get_language_name

#Introducing randomness control for consistent language detection results
DetectorFactory.seed = 0

app = Flask(__name__)
CORS(app)

# Home route to serve the main page
@app.route('/')
def home():
    return render_template('index.html')

# Route to get the instance ID
@app.route('/instance', methods=['GET'])
def get_instance():
    try:
        dirs = os.listdir('/var/lib/cloud/instances/')
        instance_id = dirs[0] if dirs else "No instance found"
        return jsonify({'instance_id': instance_id})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to detect language
@app.route('/detect', methods=['POST'])
def detect_language():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Please provide text in JSON format.'}), 400

    try:
        langs = detect_langs(data['text'])
        top = langs[0]
        code = top.lang
        prob = round(top.prob * 100, 2)
        language_name = get_language_name(code)
        return jsonify({
            'language': language_name,
            'probability': f"{prob}%"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
