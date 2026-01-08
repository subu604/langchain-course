from dotenv import load_dotenv

from typing import List
from pydantic import BaseModel, Field

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

class Source(BaseModel):
    """Schema for a source used by the agent"""
    url:str= Field(description="The Url of the source")

class AgentResponse(BaseModel):
    """"Schema for the agent response"""
    answer:str=Field(description="Agents answer for the query")
    sources:List[Source]= Field(default_factory=list, description="List of sources to generate the answer")


llm =ChatOpenAI(model="gpt-5")
# tool=[search]

tool=[TavilySearch()]
# agent=create_agent(model=llm, tools=tool) # without Structured Data code
agent=create_agent(model=llm, tools=tool, response_format=AgentResponse) #with structured data

    


def main():
    print("Hello from langchain-course!")
    result=agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an python developer using langchain in the Hyderabad on linkedin and list their details?")})
    print(result)


if __name__ == "__main__":
    main()
