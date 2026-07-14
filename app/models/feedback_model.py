from pydantic import BaseModel


class FeedbackRequest(BaseModel):
    event_name: str
    rating: str
    feedback: str