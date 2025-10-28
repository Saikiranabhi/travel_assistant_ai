from utils.helpers import generate_response

class FlightAgent:
    """Handles flight search queries."""
    def get_flights(self, source: str, destination: str):
        prompt = f"Find available flights from {source} to {destination}."
        return generate_response(prompt)
