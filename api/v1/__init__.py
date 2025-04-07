from fastapi import APIRouter
from routes.predict import router as predict_router
from routes.metrics import router as metrics_router

router = APIRouter(prefix="/api/v1")

router.include_router(predict_router)
router.include_router(metrics_router)
