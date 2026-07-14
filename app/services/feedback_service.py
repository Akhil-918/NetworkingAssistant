feedback_history = []


def save_feedback(event_name, rating, feedback):

    feedback_history.append({
        "event": event_name,
        "rating": rating,
        "feedback": feedback
    })


def get_feedback():

    return feedback_history