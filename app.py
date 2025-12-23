from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

from jira_client import JiraClient
from threat_processor import build_jira_payload

load_dotenv()

app = Flask(__name__)

jira = JiraClient(
    base_url=os.getenv("JIRA_BASE_URL"),
    email=os.getenv("JIRA_EMAIL"),
    api_token=os.getenv("JIRA_API_TOKEN")
)

PROJECT_KEY = os.getenv("JIRA_PROJECT_KEY")

@app.route("/", methods=["GET"])
def initial():
    return("This web server is running")

@app.route("/convert", methods=["POST"])
def convert_threats():
    data = request.json
    results = []

    for threat in data.get("threats", []):
        try:
            payload = build_jira_payload(threat, PROJECT_KEY)
            issue = jira.create_issue(payload)

            results.append({
                "id": threat["id"],
                "status": "created",
                "jira_key": issue["key"]
            })

        except Exception as e:
            results.append({
                "id": threat["id"],
                "status": "error",
                "message": str(e)
            })

    return jsonify(results), 201

if __name__ == "__main__":
    app.run(debug=True)
