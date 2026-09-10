import os
from typing import TypedDict
from langchain_groq import ChatGroq
from dotenv import load_env()

load_env()

class pipelinestate():
    raw_input: str
    edited_txt: str
    script_txt: str
    final_output: str

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

def editor_node():
    