from utils.helpers import generate_response

class HotelAgent:
    """Handles hotel suggestions."""
    def get_hotels(self, location: str):
        prompt = f"Suggest good hotels in {location} for travelers."
        return generate_response(prompt)
