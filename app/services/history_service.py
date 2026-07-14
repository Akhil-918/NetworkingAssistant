history = []


def save_history(event_name, analysis):
    history.append({
        "event": event_name,
        "analysis": analysis
    })


def get_history():
    return history