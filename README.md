# Oral Cancer Prediction Using Deep Learning

This project presents a deep learning-based system for detecting oral cancer from clinical mouth images. It compares multiple models including EfficientNetB0, ResNet50, DenseNet169, a custom CNN, and XGBoost (with CNN-extracted features). The goal is to identify an effective and efficient model suitable for integration into real-world diagnostic workflows or mobile screening tools.

---

## 📁 Project Structure

```
├── notebooks/
│    ├── efficientnet_training.ipynb # Final EfficientNetB0 training
│    ├── efficientnet_xgboost_training_results.ipynb # XGBoost with DL feature extraction
│    └── archives/
│        ├── 1_baseline_and_resnet_trials.ipynb
│        ├── 2_cnn_and_resnet_mid_trials-1.ipynb
│        ├── 3_cnn_and_resnet_mid_trials-2.ipynb
│        └── 4_all_models_testing.ipynb
├── utils/
│    ├── dataset_plot.py # Plot a pie chart of Dataset
│    └── remove_broken_image.py # Script to remove unreadable images
├── assets/
│    └── dataset/
│        ├── cancer/ # Folder for cancer images (not included)
│        └── normal/ # Folder for normal images (not included)
```

---

## 📊 Models and Results

| Model          | Accuracy | AUC  |
| -------------- | -------- | ---- |
| EfficientNetB0 | 95%      | 0.98 |
| DenseNet169    | 89%      | 0.98 |
| XGBoost        | 91%      | 0.95 |
| ResNet50       | 77%      | 0.73 |
| Manual CNN     | 75%      | 0.72 |

> EfficientNetB0 consistently showed the best performance in terms of AUC and recall, making it the best candidate for deployment.

---

## 📂 Dataset

- The dataset contains clinical images of oral cavities labeled as either **cancer** or **normal**.
- ⚠️ Due to size and licensing restrictions, the image dataset is **not included** in this repository.
- 📁 Directory structure (after downloading):

```
 assets/dataset/
        ├── cancer/
        └── normal/
```

---

## ⚙️ How to Use

1. Clone this repo:

   ```bash
   git clone https://github.com/yourusername/oral-cancer-prediction.git
   cd oral-cancer-prediction
   ```

2. Prepare the dataset:

   - Download or place your images in the `assets/dataset/cancer/` and `assets/dataset/normal/` folders.

3. Run cleanup (Use every time new images are added):

   ```bash
   python utils/remove_broken_image.py
   ```

4. Run a notebook from the `notebooks/` folder (preferably in Colab or Jupyter).

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- XGBoost
- Jupyter / Google Colab

---

## 🧠 Future Work

- Model conversion to TensorFlow Lite for mobile deployment.
- Integration with a Flutter or Android app for real-time screening.
- Testing with larger and real-world clinical datasets.

---

## 👤 Author

**Shiwam Dutta**  
Summer Training Project, 2025  
Department of Electronics & Communication Engineering  
Birla Institute of Technology, Mesra

---
