from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1 import router as v1_router

app = FastAPI(
    title="Skin Condition Classifier API",
    description="Upload skin images to detect skin conditions using AI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

# Include versioned API
app.include_router(v1_router)

