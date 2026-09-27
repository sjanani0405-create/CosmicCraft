from pathlib import Path

from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .comic_service import create_comic_page
from .db import Base, engine, get_db
from .gemini_service import generate_comic
from .models import Panel, Story
from .schemas import ComicRequest


# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent


# Create database tables
Base.metadata.create_all(bind=engine)


# Create FastAPI app
app = FastAPI(
    title="CosmicCraft - AI Comic Creator"
)


# Serve CSS and generated images
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


# HTML templates
templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# --------------------------------------------------
# GENERATE COMIC
# --------------------------------------------------

@app.post("/generate", response_class=HTMLResponse)
def generate(
    request: Request,
    prompt: str = Form(...),
    genre: str = Form("Adventure"),
    tone: str = Form("Fun"),
    language: str = Form("English"),
    panel_count: int = Form(6),
    db: Session = Depends(get_db)
):
    # Create request object
    comic_request = ComicRequest(
        prompt=prompt,
        genre=genre,
        tone=tone,
        language=language,
        panel_count=panel_count
    )

    # Generate comic data
    comic = generate_comic(comic_request)

    # Save story
    story = Story(
        title=comic.title,
        prompt=prompt,
        genre=genre,
        tone=tone,
        language=language,
        panel_count=panel_count
    )

    db.add(story)
    db.commit()
    db.refresh(story)

    # Save panels
    for panel in comic.panels:
        db_panel = Panel(
            story_id=story.id,
            panel_number=panel.panel_number,
            scene=panel.scene,
            dialogue=panel.dialogue,
            caption=panel.caption,
            image_prompt=panel.image_prompt
        )

        db.add(db_panel)

    db.commit()

    # Create comic image
    image_name = f"comic_{story.id}.png"

    create_comic_page(
        comic.title,
        comic.panels,
        image_name
    )

    # Save image path in database
    story.final_image = (
        f"/static/generated/{image_name}"
    )

    db.commit()

    # Show result page
    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "story": story,
            "comic": comic
        }
    )


# --------------------------------------------------
# HISTORY PAGE
# --------------------------------------------------

@app.get("/history", response_class=HTMLResponse)
def history(
    request: Request,
    db: Session = Depends(get_db)
):
    stories = (
        db.query(Story)
        .order_by(Story.created_at.desc())
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={
            "stories": stories
        }
    )


# --------------------------------------------------
# VIEW ONE STORY
# --------------------------------------------------

@app.get("/story/{story_id}", response_class=HTMLResponse)
def story_detail(
    story_id: int,
    request: Request,
    db: Session = Depends(get_db)
):
    story = (
        db.query(Story)
        .filter(Story.id == story_id)
        .first()
    )

    if not story:
        return HTMLResponse(
            "Story not found",
            status_code=404
        )

    return templates.TemplateResponse(
        request=request,
        name="result.html",
        context={
            "story": story,
            "comic": None
        }
    )