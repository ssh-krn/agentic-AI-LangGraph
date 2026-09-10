import os
from typing import TypedDict
from dataclasses import dataclass, field
from pydantic import BaseModel, field_validator
from langgraph.graph import MessagesState

class State(TypedDict):
    topic: str
    summary: str = ""
    score: int
    
    @field_validator
    def score_positive(cls, v):
        if v < 0:
            raise ValueError("Score must be positive")

@dataclass
class State:
    topic: str = ""
    summary: str = ""
    messages: list = field(default_factory=list)

class State(MessagesState):
    user_name: str
    language: str
    