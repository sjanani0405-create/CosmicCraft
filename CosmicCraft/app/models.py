from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .db import Base


class Story(Base):
    __tablename__ = "stories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(200))
    prompt: Mapped[str] = mapped_column(Text)
    genre: Mapped[str] = mapped_column(String(50))
    tone: Mapped[str] = mapped_column(String(50))
    language: Mapped[str] = mapped_column(String(50))
    panel_count: Mapped[int] = mapped_column(Integer)
    final_image: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow
    )

    panels: Mapped[list["Panel"]] = relationship(
        back_populates="story",
        cascade="all, delete-orphan",
    )


class Panel(Base):
    __tablename__ = "panels"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    story_id: Mapped[int] = mapped_column(ForeignKey("stories.id"))
    panel_number: Mapped[int] = mapped_column(Integer)
    scene: Mapped[str] = mapped_column(Text)
    dialogue: Mapped[str] = mapped_column(Text)
    caption: Mapped[str] = mapped_column(Text)
    image_prompt: Mapped[str] = mapped_column(Text)
    image_path: Mapped[str | None] = mapped_column(
        String(500), nullable=True
    )

    story: Mapped["Story"] = relationship(back_populates="panels")