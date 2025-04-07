from pydantic import BaseModel, field_validator
from typing import Literal

class PredictionResponse(BaseModel):
    condition: Literal['acne', 'dryness', 'hyperpigmentation', 'oily_skin', 'wrinkles']
    confidence: float

    @field_validator('confidence')
    def round_confidence(cls, value):
        return round(value, 2)
