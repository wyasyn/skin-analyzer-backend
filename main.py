import os
import numpy as np
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from api.v1 import router as v1_router
from config import MODEL_PATH
from models.model_loader import load_skin_condition_model

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

logger = logging.getLogger("uvicorn.error")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up: loading model...")
    model = load_skin_condition_model(MODEL_PATH)
    if model is None:
        raise RuntimeError("Failed to load skin condition model")
    # Warm up (compile) the model graph
    dummy = np.zeros((1, 224, 224, 3), dtype=np.uint8)
    model.predict(dummy)
    app.state.model = model
    yield
    logger.info("Shutting down: clearing model from state")
    if hasattr(model, "close"):
        model.close()
    else:
        del app.state.model

app = FastAPI(
    lifespan=lifespan,
    title="Skin Condition Classifier API",
    description="Upload skin images to detect skin conditions using AI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lock this down in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthz", tags=["Health"])
async def health_check():
    return {"status": "ok"}

app.include_router(v1_router)
