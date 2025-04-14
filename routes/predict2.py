from fastapi import APIRouter, HTTPException
from PIL import Image
import numpy as np
import base64
import io

from config import CLASS_NAMES, MODEL_PATH
from utils.predictor import predict_skin_condition
from schemas.prediction import ImageRequest, PredictionResponse
from models.model_loader import load_skin_condition_model
from utils.recommend import get_recommended_products

router = APIRouter()
model = load_skin_condition_model(MODEL_PATH)

@router.post(
    "/predict/",
    response_model=PredictionResponse,
    tags=["Prediction"],
    summary="Predict Skin Condition",
    description="Send a Base64 data string to make a prediction of a skin condition."
)
async def predict(data: ImageRequest):
    if not model:
        raise HTTPException(status_code=500, detail="Model not loaded.")

    try:
        # Handle image decoding
        encoded = data.image.split(",")[1] if "," in data.image else data.image
        image_data = base64.b64decode(encoded)
        image = Image.open(io.BytesIO(image_data)).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image format. Make sure it's a valid Base64 encoded image.")

    try:
        # Preprocess image
        img = image.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Predict
        prediction = predict_skin_condition(img_array, model)
        predicted_condition = prediction["condition"]
        confidence = prediction["confidence"]

        # Prepare result
        result = {
            "predicted_condition": predicted_condition,
            "confidence": confidence,
            "info": None
        }

        if confidence >= 0.7:
            condition_data = get_recommended_products(predicted_condition)
            if not condition_data:
                raise HTTPException(status_code=404, detail=f"No recommendations found for '{predicted_condition}'")
            result["info"] = condition_data

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail="Prediction failed. Please try again later.")




