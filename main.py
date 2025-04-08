import streamlit as st
import requests

st.set_page_config(page_title="Random Joke Generator", page_icon="😂")

st.title("🤣 Random Joke Generator")
st.write("Click the button below to fetch a random joke.")

if st.button("Get a Joke"):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    if response.status_code == 200:
        joke = response.json()
        st.success(f"{joke['setup']} ... {joke['punchline']}")
    else:
        st.error("Failed to fetch a joke. Please try again.")

st.markdown("---")
st.caption("Powered by [official-joke-api.appspot.com](https://official-joke-api.appspot.com)")