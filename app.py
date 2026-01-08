import streamlit as st
import requests

st.set_page_config(page_title="AI Text Analyzer", layout="centered")

st.title("AI Text Analyzer")
st.write("Analyze text for **summary, sentiment, and keywords** using AI.")

text_input = st.text_area("Input Text", height=200)

if st.button("Analyze"):
    if text_input.strip():
        with st.spinner("Analyzing text..."):
            response = requests.post(
                "http://127.0.0.1:8000/analyze",
                json={"text": text_input}
            )

        if response.status_code == 200:
            result = response.json()
            st.subheader("Summary")
            summary = result.get("summary")

            if summary:
                st.success(summary)
            else:
                st.warning("Summary not available")

            st.subheader("Sentiment")
            sentiment=result.get("sentiment")

            if sentiment:  
                st.info(f"{sentiment.get('label')}")
            else:
                st.warning("sentiment data not available")

            st.subheader("Keywords:")
            keywords=result.get("keywords")

            if keywords:
               st.write(",".join(keywords))
            else:
                st.warning("keywords not available")

        else:
            st.error("Backend error. Make sure FastAPI is running.")
    else:
        st.warning("Please enter some text.")