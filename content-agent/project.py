import os
from typing import TypedDict
from langchain_groq import ChatGroq
from dotenv import load_env

load_env()
class pipelinestate():
    raw_input: str
    edited_txt: str
    script_txt: str
    final_output: str

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

def editor_node(state: pipelinestate) -> dict:
    """"Stage 1: Cleans up grammar, removes typos, and refines the tone."""
    
    prompt = (
        "You are an expert copy copyeditor. Clean up the following raw text."
        "Fix any grammatical errors, spelling mistakes, and smooth out the transition flow"
        "While keeping the core message intact. return the edited text.\n\n"
        f"Text:\n{state["raw_input"]}"
    )

    response = llm.invoke(prompt)

    return {"edited_txt": response.content.strip()}

def script_node(state: pipelinestate) -> dict:
    """"Stage 2: Formats the clean text into engagin video style script."""
    
    prompt = (
        "You are an charismatic content creator. Take this edited text and transform."
        "it into a highly engaging, punchy, conversational video script hook. Make it sound"
        "like a real person speaking passionately. Return only the script content. \n\n"
        f"Edited Text:\n{state["edited_txt"]}"
    )

    response = llm.invoke(prompt)

    return {"script_txt": response.content.strip()}

def hinglish_node(state: pipelinestate) -> dict:
    """"Stage 3: Translate the script into natural flowing hinglish."""
    
    prompt = (
        "You are an expert content localizer for the indian market. Take the following script"
        "and convert it into natural flowing 'Hinglish'. Do not simply translate it or"
        "repeat information. Alternating comfortably between hindi and english phrases"
        "an intelligent tech educator would speak naturally on a Live stream keep the energy high."
        "Return only the hinglish text.\n\n"
        f"Scripted Text:\n{state["script_txt"]}"
    )

    response = llm.invoke(prompt)

    return {"hinglish_txt": response.content.strip()}

    