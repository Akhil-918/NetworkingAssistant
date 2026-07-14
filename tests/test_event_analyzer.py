from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Personalized Networking Assistant"
    }


def test_event_analyzer(mocker):

    mocker.patch(
        "app.routes.event_routes.analyze_event_with_gemini",
        return_value="This is a mocked AI analysis."
    )

    response = client.post(
        "/api/analyze-event-ai",
        json={
            "event_name": "AI Conference Hyderabad"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["event"] == "AI Conference Hyderabad"
    assert data["analysis"] == "This is a mocked AI analysis."


def test_topic_generator(mocker):

    mocker.patch(
        "app.routes.event_routes.generate_topics",
        return_value=[
            "AI Ethics",
            "Machine Learning",
            "Networking"
        ]
    )

    response = client.post(
        "/api/generate-topics",
        json={
            "event_name": "AI Conference Hyderabad"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["event"] == "AI Conference Hyderabad"
    assert data["topics"] == [
        "AI Ethics",
        "Machine Learning",
        "Networking"
    ]


def test_fact_checker(mocker):

    fake_response = MagicMock()
    fake_response.text = "This statement is mostly true."

    mocker.patch(
        "app.services.fact_checker_service.client.models.generate_content",
        return_value=fake_response
    )

    response = client.post(
        "/api/fact-check",
        json={
            "event_name": "Artificial Intelligence is transforming industries."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["statement"] == "Artificial Intelligence is transforming industries."
    assert data["fact_check"] == "This statement is mostly true."
def test_history():
    response = client.get("/api/history")

    assert response.status_code == 200

    data = response.json()

    assert "history" in data


def test_feedback():
    response = client.post(
        "/api/feedback",
        json={
            "event_name": "AI Conference Hyderabad",
            "rating": "⭐⭐⭐⭐⭐ Excellent",
            "feedback": "Very useful analysis."
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Feedback saved successfully."


def test_feedback_history():
    response = client.get("/api/feedback-history")

    assert response.status_code == 200

    data = response.json()

    assert "feedback_history" in data