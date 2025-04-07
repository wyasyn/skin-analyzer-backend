from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image
import numpy as np
import io

from config import CLASS_NAMES, MODEL_PATH
from utils.predictor import predict_skin_condition
from schemas.prediction import PredictionResponse
from models.model_loader import load_skin_condition_model

router = APIRouter()
model = load_skin_condition_model(MODEL_PATH)

@router.post(
    "/predict/",
    response_model=PredictionResponse,
    tags=["Prediction"],
    summary="Predict Skin Condition",
    description="Upload a skin image to predict the most likely skin condition with confidence."
)
async def predict(file: UploadFile = File(...)):
    if not model:
        raise HTTPException(status_code=500, detail="Model not loaded.")

    try:
        contents = await file.read()
        img = Image.open(io.BytesIO(contents)).convert("RGB")
        img = img.resize((224, 224))
        img_array = np.array(img)

        prediction = predict_skin_condition(img_array, model)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
