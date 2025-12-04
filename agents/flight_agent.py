from utils.helpers import generate_response

class FlightAgent:
    """Handles flight search queries."""
    
    def get_flights(self, user_query: str):
        prompt = f"""
        You are a flight-search assistant. Extract all relevant travel details from the user query,
        including source, destination, dates, times, airline preferences, number of passengers, cabin class,
        or anything else mentioned.

        If the user query does not specify certain details, still provide reasonable flight options.

        User Query: "{user_query}"

        Provide the best possible flight options based on the information available.
        """

        return generate_response(prompt)
