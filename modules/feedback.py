from langsmith import Client

def send_feedback(run_id, score):
    """Sends user feedback to LangSmith."""
    client = Client()
    client.create_feedback(run_id, "user_score", score=score)