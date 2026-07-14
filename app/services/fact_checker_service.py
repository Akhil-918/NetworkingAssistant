from app.services.gemini_service import client


def fact_check(statement):
    prompt = f"""
You are an AI Fact Checker.

Verify whether the following statement is true.

Statement:
{statement}

If it is correct:
Say "Correct" and give a short explanation.

If it is incorrect:
Say "Incorrect", explain why, and provide the correct information.

Keep the answer concise.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text