import os
from keras.models import load_model

MODEL_PATH = "models/model-v1.keras"


def validate_model(path: str):
    if not os.path.exists(path):
        print(f"❌ Model file not found at: {path}")
        exit(1)

    try:
        model = load_model(path)
        print("✅ Model is valid and loaded successfully.")
    except Exception as e:
        print(f"❌ Model validation failed: {e}")
        exit(1)

if __name__ == "__main__":
    validate_model(MODEL_PATH)
