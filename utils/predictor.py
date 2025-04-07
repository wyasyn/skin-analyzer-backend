import numpy as np
import keras
from config import CLASS_NAMES

def predict_skin_condition(img_array, model):
    img_array = np.expand_dims(img_array, axis=0)
    img_array = keras.applications.efficientnet.preprocess_input(img_array)

    pred_probs = model.predict(img_array)[0]
    top_index = np.argmax(pred_probs)

    return {
        "condition": CLASS_NAMES[top_index],
        "confidence": float(pred_probs[top_index]) * 100
    }
