import os
import requests
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "36f28749-dce2-474e-b448-2bfdbc63b234"
FLOW_ID = "8125f769-faa4-4025-a4a7-67b2f705fea6"
APPLICATION_TOKEN = os.environ.get("LANGFLOW_TOKEN")
ENDPOINT = "social_media_analyzer"


def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }
    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Route to handle request and analyze content
@app.route("/analyze", methods=["POST"])
def analyze_content():
    try:
        # Get the content from the request
        content = request.json.get("content")

        # Run the AI analysis
        response = run_flow(content)
        analysis_text = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]

        # Return the result
        return jsonify({"analysis": analysis_text})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
