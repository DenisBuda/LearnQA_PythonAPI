from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Genre(BaseModel):
    id: int
    label: str
    alias: str


class Project(BaseModel):
    id: int
    hubId: str
    ratingKinopoisk: Optional[float]
    ratingIMDB: Optional[float]
    genres: List[Genre]
    releaseDate: str
    subscriptionType: str
    category: str
    canonicalUrl: str


class BadgeItem(BaseModel):
    text: str
    color: Any


class Adfox(BaseModel):
    pixelClick: Any
    pixelImpression: Any


class Slide(BaseModel):
    id: int
    title: str
    description: str
    link: Any
    project: Project
    badge: Optional[BadgeItem]
    minAge: int
    campaignName: Optional[str]
    adfox: Adfox
    image: Optional[str]


class Data(BaseModel):
    id: int
    isActive: bool
    slides: List[Slide]


class Model2(BaseModel):
    data: Data