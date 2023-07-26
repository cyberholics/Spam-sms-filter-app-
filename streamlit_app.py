import json
import requests
import streamlit as st

st.title("Spam Message Detection Web App")
st.write("Enter a message to detect if it's spam or not")

# Get user input
user_message = st.text_area("Enter your message here", value="")

# Make prediction
if st.button("Detect Spam"):
    if user_message.strip():
        data = {"message": user_message}
        data_json = json.dumps(data)

        prediction = requests.post(
            "http://52.91.134.109:3000/classify_sms", 
            headers={"content-type": "application/json"},
            data=data_json,
        ).text

        st.write(f"The message is classified as: {prediction}")
    else:
        st.warning("Please enter a message to detect.")
