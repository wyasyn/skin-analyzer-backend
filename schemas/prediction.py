from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class ImageRequest(BaseModel):
    image: str  # base64 image string

class Product(BaseModel):
    title: str
    price: str
    description: str
    ingredients: List[str]
    image_url: HttpUrl
    link: HttpUrl


class ConditionInfo(BaseModel):
    condition: str
    description: str
    recommended_products: List[Product]


class PredictionResponse(BaseModel):
    predicted_condition: str
    confidence: float
    info: Optional[ConditionInfo]  # This will be populated only if confidence > 0.8
