import os
from typing import Dict, List
from tavily import TavilyClient
import google.generativeai as genai
from langgraph.graph import StateGraph, END
from dotenv import load_dotenv  
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))  # Add this line
llm = genai.GenerativeModel('gemini-1.5-pro')  # Remove api_key parameter here

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))  # <- fix hyphen to =
llm = genai.GenerativeModel('gemini-1.5-pro')
                              # <- fix here


def research_agent(state: Dict):
    response = tavily.search(state["query"])
    return {
        "research_results": response.get('results', []),
        "drafted_answer": state["drafted_answer"],
        "query": state["query"]
    }

def drafting_agent(state: Dict):
    context = "\n".join([res.get('content', '') for res in state["research_results"]])
    response = llm.generate_content(f"Summarize: {context}")
    return {
        "research_results": state["research_results"],
        "drafted_answer": response.text,
        "query": state["query"]
    }

def build_workflow():
    workflow = StateGraph(dict)
    workflow.add_node("research", research_agent)
    workflow.add_node("drafting", drafting_agent)
    workflow.add_edge("research", "drafting")
    workflow.add_edge("drafting", END)
    workflow.set_entry_point("research")
    return workflow.compile()

def run_research_system(query: str):
    workflow = build_workflow()
    result = workflow.invoke({
        "research_results": [],
        "drafted_answer": "",
        "query": query
    })
    return result["drafted_answer"]

if __name__ == "__main__":
    response = run_research_system("Impact of AI on cybersecurity in points")
    print(response)