# import streamlit as st
# from agents.travel_agent import TravelAgent

# st.set_page_config(page_title="Travel Assistant AI", page_icon="✈️")

# st.title("🌍 Travel Assistant AI")
# st.markdown("Ask me about flights, hotels, or travel destinations!")

# agent = TravelAgent()

# # Initialize session state keys if they don't exist
# if "last_query" not in st.session_state:
#     st.session_state["last_query"] = ""
# if "response" not in st.session_state:
#     st.session_state["response"] = ""

# # Text input
# user_input = st.text_input("✈️ Your query:", placeholder="e.g., Suggest hotels in Paris")

# # Ask button
# ask_button = st.button("Ask")

# # Respond when user presses Enter OR clicks Ask
# if (user_input and user_input != st.session_state["last_query"]) or ask_button:
#     with st.spinner("Thinking..."):
#         st.session_state["response"] = agent.handle_query(user_input)
#         st.session_state["last_query"] = user_input

# # Display response
# if st.session_state["response"]:
#     st.success(st.session_state["response"])


import streamlit as st
from agents.travel_agent import TravelAgent

st.set_page_config(page_title="Travel Assistant AI", page_icon="✈️")

st.title("🌍 Travel Assistant AI")
st.markdown("Ask me about flights, hotels, or travel destinations!")

agent = TravelAgent()

# Initialize session_state keys safely
if "last_query" not in st.session_state:
    st.session_state["last_query"] = ""
if "response" not in st.session_state:
    st.session_state["response"] = ""

# Wrap input and button logic in a form to prevent session_state KeyError
with st.form(key="travel_form"):
    user_input = st.text_input(
        "✈️ Your query:", 
        placeholder="e.g., Suggest hotels in Paris"
    )
    ask_button = st.form_submit_button("Ask")

# Respond only when form is submitted or new query
if ask_button and user_input:
    with st.spinner("Thinking..."):
        st.session_state["response"] = agent.handle_query(user_input)
        st.session_state["last_query"] = user_input

# Display response
if st.session_state["response"]:
    st.success(st.session_state["response"])
