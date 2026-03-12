import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

from .tools import (
    log_interaction,
    get_interactions,
    edit_interaction,
    summarize_interaction,
    suggest_followup
)

load_dotenv()

llm = ChatGroq(
    temperature=0,
    model_name="llama3-70b-8192",
    groq_api_key=os.getenv("GROQ_API_KEY")
)


def run_agent(prompt: str):

    prompt_lower = prompt.lower()

    # TOOL 1
    if "log interaction" in prompt_lower:

        try:

            parts = prompt.replace("log interaction", "").strip().split(",")

            name = parts[0].strip()
            email = parts[1].strip()
            company = parts[2].strip()

            return log_interaction(name, email, company)

        except:

            return "Format: log interaction name,email,company"


    # TOOL 2
    if "show interaction" in prompt_lower:

        return str(get_interactions())


    # TOOL 3
    if "edit interaction" in prompt_lower:

        try:

            parts = prompt.replace("edit interaction", "").strip().split(",")

            id = int(parts[0])
            name = parts[1]

            return edit_interaction(id, name)

        except:

            return "Format: edit interaction id,newname"


    # TOOL 4
    if "summarize" in prompt_lower:

        text = prompt.replace("summarize", "")

        return summarize_interaction(text)


    # TOOL 5
    if "followup" in prompt_lower:

        return str(suggest_followup())


    # AI fallback
    response = llm.invoke(prompt)

    return response.content