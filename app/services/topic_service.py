from app.services.gemini_service import client


def generate_topics(event_name):
    prompt = f"""
You are an AI Networking Assistant.

The user is attending this event:

{event_name}

Generate 5 professional networking conversation topics.

Return only a numbered list.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text