from langchain.agents import create_agent
from langchain_sarvam import ChatSarvam
from langchain_core.output_parsers import StrOutputParser
from src.tools.tools import websearch,scrape_url
from langchain_core.prompts import ChatPromptTemplate
from rich import print

from dotenv import load_dotenv

load_dotenv()

llm = ChatSarvam(model="sarvam-105b", tempurature=0)
# 1st agent
def build_search_agent():
    return create_agent(
        model=llm,
        tools=[websearch]   
    )
    
# 2nd Agent: Reader Agent
def build_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url] 
    )
    
writer_prompt = ChatPromptTemplate.from_messages([
    ("system","You are an expert research writer. Write clear, structured and insighted reports"),
    ("human","""Write a detailed research report on the topic below.
Topic: {topic}
Research Gathered:
{research}

Structure the report as:
-Introduction
-Key Findings (minimum3 well-explained points)
-Conclusion
-Sources (list all URLs found in the reasearch)
Be detailed, factual and proffesional."""),
    
])

critic_prompt = ChatPromptTemplate.from_messages([
     ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()

