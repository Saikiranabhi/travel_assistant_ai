from utils.helpers import generate_response

class TrainAgent:
    """Handles train search queries."""

    def get_trains(self, user_query: str):
        prompt = f"""
        You are a train-search assistant. Extract all relevant travel details from the user query,
        including source, destination, travel date, time preferences, train type (express, superfast, local),
        coach class (sleeper, AC, chair car, etc.), seat/berth preference, and number of passengers.

        If some details are not explicitly mentioned, infer them or provide reasonable and helpful options.

        User Query: "{user_query}"

        Provide the best possible train options based on the extracted information.
        """

        return generate_response(prompt)
