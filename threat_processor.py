def build_jira_payload(threat, project_key):
    # Atlassian Document Format (ADF) for description
    description = {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": threat["description"]
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": f"Category: {threat['category']}"
                    }
                ]
            },
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": f"CVSS Rating: {threat['cvss_rating']}"
                    }
                ]
            }
        ]
    }

    if threat["severity"] == "High":
        priority = "Highest"
    elif threat["severity"] == "Medium":
        priority = "High"
    else:
        priority = "Medium"

    return {
        "fields": {
            "project": {
                "key": project_key          # ✅ NOT hardcoded
            },
            "summary": threat["title"],
            "description": description,
            "issuetype": {
                "name": "Task"              # ✅ safest issue type
            },
            "priority": {
                "name": priority
            },
            "labels": [
                "security",
                threat["id"].lower()
            ]
        }
    }
