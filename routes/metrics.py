from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import json


router = APIRouter()

def load_metrics():
    with open("data/metrics.json") as f:
        return json.load(f)

@router.get(
    "/metrics/",
    response_model=dict,
    tags=["Evaluation"],
    summary="Model Performance Metrics",
    description="Returns accuracy, precision, recall, and F1-score of the model on test data."
)
def get_model_metrics():
    try:
        metrics = load_metrics()
        return JSONResponse(content=metrics)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
