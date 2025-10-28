from utils.helpers import generate_response

class TravelAgent:
    """Main travel assistant agent."""
    def __init__(self):
        pass

    def handle_query(self, query: str) -> str:
        prompt = f"You are a travel assistant. Help the user with travel info.\nUser: {query}"
        return generate_response(prompt)
