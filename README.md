# Crypto-Analyst-AI
 Crypto Analyst AI is an intelligent chatbot that provides real-time cryptocurrency analysis, trading insights, and market trends. It uses Groq-hosted LLaMA or Mixtral language models, optionally integrates web search, and delivers responses through a user-friendly Streamlit interface backed by a FastAPI server.


A smart, fast crypto chatbot using Groq LLaMA/Mixtral models, built with LangChain, FastAPI, and Streamlit.

---------------------------------------------
📁 Project Structure
---------------------------------------------
```crypto_analyst_ai/
├── .env                  <- API keys file
├── backend/
│   ├── ai_agent.py       <- LangChain + Groq logic
│   ├── backend.py        <- FastAPI server
│   └── requirements.txt
├── frontend/
│   ├── frontend.py       <- Streamlit interface
│   └── requirements.txt
├── README.txt'''

---------------------------------------------
🔐 API Keys Setup
---------------------------------------------
Create a `.env` file in the project root:

GROQ_API_KEY=gsk_your_groq_key_here  
TAVILY_API_KEY=tvly_your_tavily_key_here

Note: TAVILY_API_KEY is optional if web search is disabled.

---------------------------------------------
⚙️ How to Run the App
---------------------------------------------

1️⃣ Backend Setup
-----------------
cd backend  
python -m venv venv  
venv\Scripts\activate       (for Windows)  
source venv/bin/activate    (for Mac/Linux)

Install dependencies:
pip install -r requirements.txt

Start the server:
uvicorn backend:app --reload --port 9999

The API will be available at:
http://localhost:9999

2️⃣ Frontend Setup
------------------
Open a new terminal:

cd frontend  
pip install -r requirements.txt  

Start the Streamlit app:
streamlit run frontend.py

The app will open in your browser at:
http://localhost:8501

---------------------------------------------
🧠 Supported Models
---------------------------------------------
Choose from the following Groq-hosted models:

- llama3-70b-8192  
- mixtral-8x7b-32768

---------------------------------------------
🙋 About
---------------------------------------------
Created by Mohit Rahangdale, a B.Tech(AI) student as a project to integrate real-time crypto insights with fast and efficient language models.

---------------------------------------------
📜 License
---------------------------------------------
MIT License – Free to use, modify, and share.
