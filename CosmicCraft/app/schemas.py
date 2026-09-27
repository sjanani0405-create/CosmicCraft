from pydantic import BaseModel, Field
from typing import List


class Character(BaseModel):
    name: str
    description: str


class ComicPanel(BaseModel):
    panel_number: int
    scene: str
    dialogue: str
    caption: str
    image_prompt: str


class ComicResponse(BaseModel):
    title: str
    characters: List[Character]
    panels: List[ComicPanel]


class ComicRequest(BaseModel):
    prompt: str = Field(min_length=3)
    genre: str = "Adventure"
    tone: str = "Fun"
    language: str = "English"
    panel_count: int = Field(default=6, ge=2, le=12)