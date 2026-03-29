import joblib
import pandas as pd
import streamlit as st

# Load the trained model
model = joblib.load("fraud_detection_model.pkl")

st.title("Fraud Detection Prediction App")
st.markdown(
    "Enter the details of the transaction to predict if it's fraudulent or not."
)
st.divider()

transaction_type = st.selectbox(
    "Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"]
)
amount = st.number_input("Amount", min_value=0.0, step=0.01, value=1000.0)
oldbalanceOrg = st.number_input(
    "Old Balance (Sender)", min_value=0.0, step=0.01, value=10000.0
)
newbalanceOrig = st.number_input(
    "New Balance (Sender)", min_value=0.0, step=0.01, value=9000.0
)
oldbalanceDest = st.number_input(
    "Old Balance (Destination)", min_value=0.0, step=0.01, value=0.0
)
newbalanceDest = st.number_input(
    "New Balance (Destination)", min_value=0.0, step=0.01, value=0.0
)

if st.button("Predict"):
    # Create a DataFrame for the input data
    input_data = pd.DataFrame(
        {
            "type": [transaction_type],
            "amount": [amount],
            "oldbalanceOrg": [oldbalanceOrg],
            "newbalanceOrig": [newbalanceOrig],
            "oldbalanceDest": [oldbalanceDest],
            "newbalanceDest": [newbalanceDest],
        }
    )

    # Make the prediction
    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction Result : {int(prediction)}")

    # Display the result
    if prediction == 1:
        st.error("The transaction is predicted to be fraudulent.")
    else:
        st.success("The transaction is predicted to be legitimate.")
