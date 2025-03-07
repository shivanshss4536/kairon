# Deep Research AI Agentic System

## Overview
The **Deep Research AI Agentic System** is an intelligent research assistant that automates online data gathering and response generation. It utilizes a **multi-agent architecture** with **Tavily API** for web crawling and **LLMs (Gemini/OpenAI)** for answer drafting. The system is built with **LangGraph** and **LangChain** for seamless agent interactions.

## Features
✅ **Automated Web Research** - Uses Tavily API to fetch relevant content.  
✅ **Dual-Agent System** - One agent collects data, another drafts responses.  
✅ **Context-Aware Summarization** - Filters irrelevant content for precise results.  
✅ **Scalable & Extensible** - Can integrate additional agents for fact-checking or analysis.  
✅ **Optimized Performance** - Implements caching to avoid redundant API calls.  

## Tech Stack
- **Python**
- **LangChain & LangGraph**
- **Tavily API** (for web research)
- **OpenAI/Gemini API** (for text generation)
- **Streamlit** (for UI, if applicable)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/shivanshss4536/kairon.git
   
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up API keys in a `.env` file:
   ```plaintext
   GOOGLE_API_KEY=your-google-api-key
   TAVILY_API_KEY=your-tavily-api-key
   ```

## Usage
Run the main script:
```bash
python app.py
```

## Contribution
Feel free to open issues or submit pull requests. 🚀