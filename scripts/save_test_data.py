import os
import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.utils import to_categorical

IMG_SIZE = (224, 224)
TEST_DIR = "dataset/test"
CLASS_NAMES = sorted(os.listdir(TEST_DIR))  # Assumes folders = classes
NUM_CLASSES = len(CLASS_NAMES)

X_test = []
y_test = []

# Map class names to indices
class_to_index = {cls_name: idx for idx, cls_name in enumerate(CLASS_NAMES)}

print("🔍 Processing test images...")
for cls_name in CLASS_NAMES:
    cls_path = os.path.join(TEST_DIR, cls_name)
    for fname in os.listdir(cls_path):
        fpath = os.path.join(cls_path, fname)
        try:
            img = load_img(fpath, target_size=IMG_SIZE)
            img_array = img_to_array(img) / 255.0  # Normalize
            X_test.append(img_array)
            y_test.append(class_to_index[cls_name])
        except Exception as e:
            print(f"⚠️ Skipped {fpath}: {e}")

# Convert to arrays
X_test = np.array(X_test, dtype="float32")
y_test = to_categorical(y_test, num_classes=NUM_CLASSES)

# Save
os.makedirs("data", exist_ok=True)
np.save("data/X_test.npy", X_test)
np.save("data/y_test.npy", y_test)
print(f"✅ Saved {X_test.shape[0]} test samples to 'data/X_test.npy' and 'data/y_test.npy'")
