import os
import shutil
import tensorflow as tf

ROOT = "Oral Cancer Prediction"
DATA_PATH = os.path.join(ROOT, "assets", "dataset")
BROKEN_PATH = os.path.join(ROOT, "assets", "broken")

for class_name in os.listdir(DATA_PATH):
    class_dir = os.path.join(DATA_PATH, class_name)
    for img_name in os.listdir(class_dir):
        img_path = os.path.join(class_dir, img_name)
        try:
            img = tf.io.read_file(img_path)
            # This will crash if the image is broken
            img = tf.io.decode_jpeg(img)
        except Exception as e:
            print(f"[BROKEN] {img_path}")
            os.makedirs(BROKEN_PATH, exist_ok=True)
            shutil.move(img_path, os.path.join(BROKEN_PATH, img_name))
