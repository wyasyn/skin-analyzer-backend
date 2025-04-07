from keras.models import load_model

def load_skin_condition_model(model_path: str):
    try:
        model = load_model(model_path)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
