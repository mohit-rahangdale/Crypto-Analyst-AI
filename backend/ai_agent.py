import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import YouTubeSearchTool
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
import traceback

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

def get_response_from_aiagent(model_id, allow_search, system_prompt, query):
    try:
        llm = ChatGroq(model=model_id, api_key=groq_api_key, temperature=0.7)

        tools = []
        if allow_search and tavily_api_key:
            tools = [
                TavilySearchResults(api_key=tavily_api_key),
                YouTubeSearchTool()
            ]

        prompt = hub.pull("hwchase17/react").partial(system_message=system_prompt)

        agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
        agent_executor = AgentExecutor(
            agent=agent,
            tools=tools,
            handle_parsing_errors=True,
            max_iterations=5,
            return_intermediate_steps=False,
            verbose=True
        )

        result = agent_executor.invoke({"input": query})
        return result["output"]

    except Exception as e:
        print(f"Agent Error: {str(e)}\n{traceback.format_exc()}")
        return f"Analysis failed: {str(e)}"
