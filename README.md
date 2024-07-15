# Credit-Card-Default-Prediction

This project was created to predict whether a customer will default on their credit card in a month and the model is expected to minimize False Negatives (failed to pay but predicted otherwise) and suppress False Positives (not defaulted but predicted otherwise). The machine learning used is Supervised Classification Machine Learning. The algorithms used include KNN, Logistic Regression, and SVM. Therefore, the metric used to measure the performance of this program (model) is F1 Score because it can see the harmonization of Precision and Recall. The dataset is obtained from Bigquery with the query in the notebook. The results of the predictions are deployed on Hugging Face with the URL provided in the URL script.

## Project Purpose
The main purpose of this project is to develop a model that can accurately predict credit card defaults, helping financial institutions manage risk and prevent losses.

## Problem Statement
Credit card defaults pose significant risks to financial institutions. Accurately predicting which customers are likely to default allows these institutions to take preventive measures and manage their credit risk effectively.

## Background
Credit risk management is crucial for financial institutions to maintain financial stability and profitability. This project leverages machine learning techniques to predict credit card defaults, enabling proactive risk management.

## Project Output
A trained classification model to predict credit card defaults.
Insights into the factors influencing default likelihood.
Model performance evaluation using F1 Score.

## Methods
Exploratory Data Analysis (EDA): Understanding the dataset and identifying patterns.
Feature Engineering: Creating and selecting features to improve model performance.
Modeling: Training classification models using KNN, Logistic Regression, and SVM.
Evaluation: Assessing model performance using F1 Score.

## Technology Stack

Programming Language: Python

Data Analysis and Manipulation: Pandas, NumPy

Data Visualization: Matplotlib, Seaborn

Machine Learning: Scikit-Learn

Notebook Environment: Jupyter Notebook

Deployment: Hugging Face

## Files

1. Credit Card Prediction.ipynb

Dataset Information: Detailed description of the dataset used.
Exploratory Data Analysis (EDA): Identifying patterns and visualizing trends.
Feature Engineering: Creating and selecting features.
Modeling: Training classification models.
Evaluation: Assessing model performance.

2. P1G5_Set_1_kelvin_rizky.csv
This CSV file contains the dataset obtained from Google BigQuery.

3. model_scaler.pkl
A model for scaling the data using MinMaxScaler.

4. model_svm_random.pkl
The trained SVM model for prediction.

## Deployment Files

1. app.py
Script for creating the web interface on Hugging Face.

2. credit_card.jpg
Image to be displayed in the app.

3. eda.py
Script focused on Exploratory Data Analysis.

4. prediction.py
Script for processing predictions.
