import streamlit as st
from agents.travel_agent import TravelAgent

st.set_page_config(page_title="Travel Assistant AI", page_icon="✈️")

st.title("🌍 Travel Assistant AI")
st.markdown("Ask me about flights, hotels, or travel destinations!")

agent = TravelAgent()

user_input = st.text_input("✈️ Your query:", placeholder="e.g., Suggest hotels in Paris")

# Ask button
ask_button = st.button("Ask")

# Respond when user presses Enter OR clicks Ask
if user_input and (st.session_state.get("last_query") != user_input or ask_button):
    with st.spinner("Thinking..."):
        response = agent.handle_query(user_input)
    st.success(response)
    st.session_state["last_query"] = user_input