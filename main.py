from agents.travel_agent import TravelAgent

def main():
    agent = TravelAgent()
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        response = agent.handle_query(query)
        print("Assistant:", response)

if __name__ == "__main__":
    main()
