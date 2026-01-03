from dotenv import load_dotenv

load_dotenv()
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain_tavily import TavilySearch # tavily has their own search engine developed with  proper responses
# from tavily import TavilyClient #a 3rd party company


# tavily=TavilyClient()

# @tool
# def search(query:str) -> str:
#     """
#     Tool that search over internet
#     Args: 
#         query:  Qouery to Search for
#     Returns:
#         The Search Result     
#     """
#     # return "Munnar is cold place."
#     return tavily.search(query=query)


llm =ChatOpenAI(model="gpt-5")
# tool=[search]

tool=[TavilySearch()]
agent=create_agent(model=llm, tools=tool)

    


def main():
    print("Hello from langchain-course!")
    result=agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an python developer using langchain in the Hyderabad on linkedin and list their details?")})
    print(result)


if __name__ == "__main__":
    main()
