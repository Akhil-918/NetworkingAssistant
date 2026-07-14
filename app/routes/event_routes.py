from app.models.feedback_model import FeedbackRequest
from app.services.feedback_service import save_feedback, get_feedback
from app.services.history_service import save_history, get_history
from app.services.fact_checker_service import fact_check
from app.services.topic_service import generate_topics
from fastapi import APIRouter
from app.models.event_model import EventRequest
from app.services.gemini_service import analyze_event_with_gemini

router = APIRouter(
    prefix="/api",
    tags=["Networking Assistant"]
)

@router.post("/analyze-event-ai")
def analyze_event_ai(request: EventRequest):

    result = analyze_event_with_gemini(request.event_name)

    save_history(request.event_name, result)

    return {
        "event": request.event_name,
        "analysis": result
    }
@router.post("/generate-topics")
def generate_topics_api(request: EventRequest):
    topics = generate_topics(request.event_name)

    return {
        "event": request.event_name,
        "topics": topics
    }
@router.post("/fact-check")
def fact_check_api(request: EventRequest):
    result = fact_check(request.event_name)

    return {
        "statement": request.event_name,
        "fact_check": result
    }
@router.post("/feedback")
def feedback_api(request: FeedbackRequest):

    save_feedback(
        request.event_name,
        request.rating,
        request.feedback
    )

    return {
        "message": "Feedback saved successfully."
    }
@router.get("/feedback-history")
def feedback_history_api() -> dict:

    return {
        "feedback_history": get_feedback()
    }
@router.get("/gemini")
def gemini_test() -> dict:
    return {
        "response": analyze_event_with_gemini("AI Conference Hyderabad")
    }
@router.get("/history")
def history_api() -> dict:
    return {
        "history": get_history()
    }