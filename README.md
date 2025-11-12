# Language Detection API

A simple Flask API that detects the language of a given text using the `langdetect` library.  
It includes endpoints for language detection, supported language listings, EC2 instance details, and health checks.

## Features

- Detects language and confidence probability from input text  
- Returns full language name using a predefined mapping  
- Lists all supported languages  
- Includes a health check endpoint for uptime monitoring  
- Retrieves EC2 instance ID when deployed on AWS  


## Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/` | GET | Serves the frontend (`index.html`) |
| `/health` | GET | Health check for API status |
| `/instance` | GET | Returns EC2 instance ID |
| `/detect` | POST | Detects the language of input text |
| `/supported_languages` | GET | Lists all supported languages and their codes |

---

## Setup (This can be used to replicate in an EC2 Instance as well)

```bash
git clone https://github.com/sharathandres51-eng/sharath-langdetect-flask.git
cd sharath-langdetect-flask
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
