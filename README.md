# Risk-prediction-of-cardiovascular-diseases

My first project, 2026

<p> <b>Desktop PySide6 app that predicts risk of coronary heart disease using a Random Forest model</b><br> trained on the Framingham Heart Study dataset. </p> <p> <img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-blue"> <img alt="PySide6" src="https://img.shields.io/badge/GUI-PySide6-41CD52"> <img alt="scikit-learn" src="https://img.shields.io/badge/ML-scikit--learn-F7931E"> <img alt="License" src="https://img.shields.io/badge/license-MIT-lightgrey"> </p>

This app walks the user through a series of questions on their health, feeds the answers into a pre-trained RandomForestClassifier and reports whether their estimated risk of coronary heart disease is high or low with percentile.

The classifier and its supporting artifacts (feature list, medians for missing values, optimal decision threshold) are trained in project.ipynb on the Framingham Heart Study dataset and loaded by the PySide6 GUI in main.py.

# Project structure


├── main.py               # PySide6 GUI application

├── mainwindow.py          # Auto-generated from MainWindow.ui via pyside6-uic

├── MainWindow.ui          # Qt Designer layout

├── project.ipynb          # Model training notebook

├── framingham.csv         # Source dataset

├── tree_model.pkl         # Trained RandomForestClassifier

├── feature_names.pkl      # Ordered list of model features

├── medians.pkl            # Median values used to fill missing input

└── best_threshold.pkl     # Optimal classification threshold (Youden's J)

# Model

Algorithm	RandomForestClassifier (n_estimators=300, min_samples_leaf=10, class_weight='balanced')

14 features

Missing values are filled with median

Decision threshold is selected by maximizing Youden's J statistic (TPR − FPR) on the ROC curve

# Performance:

ROC AUC	≈ 0.71
Recall ≈ 0.69
FPR ≈ 0.36

Model catches more true risk cases with the cost of more false positives.


# Installation

Requires Python 3.10+.

bash
git clone <repo-url>
cd <repo-folder>
pip install -r requirements.txt


Then run:

bash
python main.py


# Retraining the model

Place framingham.csv in the project directory.
Open and run project.ipynb top to bottom.
This regenerates tree_model.pkl, feature_names.pkl, medians.pkl, and best_threshold.pkl.
