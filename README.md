# Fraud Detection Using Machine Learning

This project predicts whether a financial transaction is fraudulent using a machine learning model trained on historical transaction data from Kaggle.

The repository includes:

- a trained model file: `fraud_detection_model.pkl`
- a Streamlit app for interactive predictions: `main.py`
- a notebook for analysis and experimentation: `analysis_model.ipynb`

## Overview

Fraud detection is a binary classification problem with highly imbalanced data, where fraudulent transactions make up a small portion of all transactions.

The goal of this project is to identify fraudulent transactions while keeping false negatives low, since missed fraud cases can be especially costly.

## Dataset

The dataset is based on a Kaggle fraud detection dataset containing transaction records and fraud labels.

Main feature types include:

- transaction type
- transaction amount
- sender balances before and after the transaction
- destination balances before and after the transaction

Dataset source:

- [Kaggle Dataset](https://www.kaggle.com/datasets/amanalisiddiqui/fraud-detection-dataset)

## App Inputs

The prediction app expects the following transaction fields:

- `type`
- `amount`
- `oldbalanceOrg`
- `newbalanceOrig`
- `oldbalanceDest`
- `newbalanceDest`

The app returns:

- `1` for fraudulent
- `0` for legitimate

## Project Structure

- `main.py` - Streamlit app for fraud prediction
- `fraud_detection_model.pkl` - serialized trained model
- `analysis_model.ipynb` - notebook for analysis and model development
- `pyproject.toml` - project metadata and dependencies

## Setup

This project requires Python `3.13+`.

Install dependencies with `uv`:

```bash
uv sync
```

Or install them manually with `pip`:

```bash
pip install matplotlib numpy pandas scikit-learn seaborn streamlit joblib
```

## Run the App

Start the Streamlit app with:

```bash
streamlit run main.py
```

Then open the local URL shown in your terminal.