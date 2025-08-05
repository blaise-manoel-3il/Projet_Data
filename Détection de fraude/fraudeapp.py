import streamlit as st
import pandas as pd
import joblib

# --- Custom CSS ---
st.markdown("""
    <style>
    .main {
        background-color: grey;
    }
    h1 {
        color: #003366;
        text-align: center;
    }
    .stButton>button {
        background-color: #003366;
        color: white;
        border-radius: 10px;
        padding: 0.5em 1.5em;
        font-size: 16px;
        margin-top: 20px;
    }
    .stMarkdown {
        text-align: center;
    }
    .box {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #003366;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        margin: 30px auto;
    }
    </style>
""", unsafe_allow_html=True)

# --- Chargement du modèle ---
try:
    model = joblib.load("fraud_detection_pipeline.pkl")
except Exception as e:
    st.error(f"❌ Erreur de chargement du modèle : {e}")
    st.stop()

# --- Titre et instructions ---
st.title(" Application de Détection de Fraude")
st.markdown(" Veuillez entrer les détails de la transaction, puis cliquer sur le bouton **Prédire**")
st.divider()

# --- Boîte avec bordure ---
st.markdown("<div class='box'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    transaction_type = st.selectbox("Type de transaction", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"])
    amount = st.number_input(" Montant", min_value=0.0, value=1000.0)
    oldbalanceOrg = st.number_input(" Ancien solde (expéditeur)", min_value=0.0, value=1000.0)

with col2:
    newbalanceOrig = st.number_input(" Nouveau solde (expéditeur)", min_value=0.0, value=9000.0)
    oldbalanceDest = st.number_input(" Ancien solde (destinataire)", min_value=0.0, value=0.0)
    newbalanceDest = st.number_input("Nouveau solde (destinataire)", min_value=0.0, value=0.0)

st.markdown("</div>", unsafe_allow_html=True)

# --- Bouton Prédire ---
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button(" Prédire"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]
    st.subheader(f" Résultat : **{int(prediction)}**")
    if prediction == 1:
        st.error("⚠️ Cette transaction est potentiellement frauduleuse.")
    else:
        st.success("✅ Cette transaction semble normale.")

st.markdown("</div>", unsafe_allow_html=True)