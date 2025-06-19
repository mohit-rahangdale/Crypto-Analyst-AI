import streamlit as st
import requests

st.set_page_config(page_title="Crypto Analyst AI", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []

SYSTEM_PROMPT = "You are a crypto expert assistant. Give detailed analysis with sources."

BACKEND_URL = "http://localhost:9999"

st.title("🚀 Crypto Analyst AI")

with st.sidebar:
    model_id = st.selectbox("Model", ["llama3-70b-8192", "mixtral-8x7b-32768"])
    allow_search = st.checkbox("Enable Web Search", value=True)

    if st.button("Check API"):
        try:
            res = requests.get(f"{BACKEND_URL}/health")
            if res.status_code == 200:
                st.success("✅ API running")
            else:
                st.error("⚠️ API error")
        except:
            st.error("❌ API not reachable")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask about crypto trends or trading..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):
            try:
                res = requests.post(f"{BACKEND_URL}/chat", json={
                    "model_id": model_id,
                    "system_prompt": SYSTEM_PROMPT,
                    "allow_search": allow_search,
                    "messages": [prompt]
                })
                if res.status_code == 200:
                    result = res.json()
                    answer = result["response"]
                else:
                    answer = f"Error: {res.status_code}\n{res.text}"
            except Exception as e:
                answer = f"Error: {str(e)}"

        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
