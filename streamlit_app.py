import streamlit as st
import requests

st.set_page_config(page_title="Personalized Networking Assistant")

st.title("🤝 Personalized Networking Assistant")

# -----------------------------------
# Streamlit Session State
# -----------------------------------

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "event" not in st.session_state:
    st.session_state.event = ""

if "fact_result" not in st.session_state:
    st.session_state.fact_result = None

# -----------------------------------
# Event Analysis Section
# -----------------------------------

event_name = st.text_input("Enter Event Name")

if st.button("Analyze Event"):

    response = requests.post(
        "http://127.0.0.1:8000/api/analyze-event-ai",
        json={"event_name": event_name}
    )

    if response.status_code == 200:

        result = response.json()

        # Save in Session State
        st.session_state.analysis = result["analysis"]
        st.session_state.event = result["event"]

    else:
        st.error("Failed to connect to FastAPI")

# Display stored analysis
if st.session_state.analysis:

    st.success("✅ Analysis Generated Successfully!")

    st.subheader("📌 Event")
    st.write(st.session_state.event)

    with st.expander("🤖 View AI Analysis", expanded=True):
        st.write(st.session_state.analysis)

    st.divider()

    # -----------------------------------
    # Feedback Section
    # -----------------------------------

    st.subheader("⭐ Feedback")

    feedback = st.radio(
        "Was this analysis helpful?",
        [
            "⭐⭐⭐⭐⭐ Excellent",
            "⭐⭐⭐⭐ Good",
            "⭐⭐⭐ Average",
            "⭐⭐ Poor"
        ]
    )

    comments = st.text_area("Additional Comments (Optional)")

    if st.button("Submit Feedback"):

        feedback_response = requests.post(
            "http://127.0.0.1:8000/api/feedback",
            json={
                "event_name": st.session_state.event,
                "rating": feedback,
                "feedback": comments
            }
        )

        if feedback_response.status_code == 200:
            st.success("🎉 Thank you for your feedback!")
        else:
            st.error("Failed to save feedback.")

# -----------------------------------
# Fact Checker Section
# -----------------------------------

st.divider()

st.header("🔍 Fact Checker")

fact_statement = st.text_input("Enter a statement to verify")

if st.button("Check Fact"):

    fact_response = requests.post(
        "http://127.0.0.1:8000/api/fact-check",
        json={
            "event_name": fact_statement
        }
    )

    if fact_response.status_code == 200:

        result = fact_response.json()

        # Save in Session State
        st.session_state.fact_result = result["fact_check"]

    else:
        st.error("Failed to check fact.")

# Display stored fact check result
if st.session_state.fact_result:

    st.success("✅ Fact Check Completed")

    st.subheader("Fact Check Result")
    st.write(st.session_state.fact_result)

# -----------------------------------
# Conversation History Section
# -----------------------------------

st.divider()

st.header("📜 Conversation History")

if st.button("Load History"):

    history_response = requests.get(
        "http://127.0.0.1:8000/api/history"
    )

    if history_response.status_code == 200:

        history = history_response.json()["history"]

        if len(history) == 0:
            st.info("No conversation history available.")

        else:
            for item in history:

                st.subheader(item["event"])

                with st.expander("📄 View Analysis"):
                    st.write(item["analysis"])

                st.divider()

    else:
        st.error("Failed to load history.")

# -----------------------------------
# Feedback History Section
# -----------------------------------

st.divider()

st.header("📝 Feedback History")

if st.button("Load Feedback History"):

    feedback_history_response = requests.get(
        "http://127.0.0.1:8000/api/feedback-history"
    )

    if feedback_history_response.status_code == 200:

        feedback_history = feedback_history_response.json()["feedback_history"]

        if len(feedback_history) == 0:
            st.info("No feedback history available.")

        else:
            for item in feedback_history:

                st.subheader(item["event"])

                st.write("⭐ Rating:", item["rating"])
                st.write("💬 Feedback:", item["feedback"])

                st.divider()

    else:
        st.error("Failed to load feedback history.")