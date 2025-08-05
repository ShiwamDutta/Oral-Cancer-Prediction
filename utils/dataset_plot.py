import os
import matplotlib.pyplot as plt

ROOT = "Oral Cancer Prediction"
DATA_PATH = os.path.join(ROOT, "assets", "dataset")

class_names = os.listdir(DATA_PATH)
class_counts = [
    os.listdir(os.path.join(DATA_PATH, class_names[0])).__len__(),
    os.listdir(os.path.join(DATA_PATH, class_names[1])).__len__(),
]

plt.figure(figsize=(4, 4))
plt.pie(
    class_counts,
    labels=class_names,
    autopct="%1.1f%%",
    startangle=140,
    colors=plt.cm.tab20.colors,
)
plt.title("Class Distribution in Dataset")
plt.show()
