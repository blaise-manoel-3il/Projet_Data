{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ecb55d81-7881-450d-b64a-5978708acd07",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "44c094b4-2461-41ea-8c23-e3c8e86bf7f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "model = joblib.load(\"fraud_detection_pipeline.pkl\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bf89516b-179d-45d7-a664-13e1aceb0ebb",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-08-03 14:14:55.872 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\MANOEL\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title(\"Application de détection de fraude\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c1289560-8b17-4c88-b2c7-beca1e0d65cc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.markdown(\"veillez entrer les détails de la transaction et utiliser le bouton predire\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ee9a4dd2-ee79-482e-a059-d26ccfeaa8c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.divider()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "cd322b17-ce87-4df2-8a47-3bada5f1220a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-08-03 14:15:29.289 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "transaction_type = st.selectbox(\"Transaction Type\",[\"PAYMENT\",\"TRANSFER\",\"CASH_OUT\",\"DEPOSIT\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "a4185c3c-4821-4db4-a476-afcffda33e02",
   "metadata": {},
   "outputs": [],
   "source": [
    "amount = st.number_input(\"Amount\", min_value=0.0,value=1000.0)\n",
    "oldbalanceOrg = st.number_input(\"Old Balance (Sender)\", min_value=0.0, value=1000.0)\n",
    "newbalanceOrg = st.number_input(\"New Balance (Sender)\", min_value=0.0, value=9000.0)\n",
    "oldbalanceDest = st.number_input(\"Old Balance (Receiver)\", min_value=0.0, value=0.0)\n",
    "newbalanceDest = st.number_input(\"New Balance (Receiver)\", min_value=0.0, value=0.0)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "95d6d547-c1e2-4240-a3c1-46883a966317",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "if st.button(\"predict\"):\n",
    "    input_data = pd.DataFrame ([{\n",
    "        \"type\" : transaction_type,\n",
    "        \"amount\" : amount,\n",
    "        \"oldbalanceOrg\" : oldbalanceOrg,\n",
    "        \"newbalanceOrg\" : newbalanceOrg,\n",
    "        \"oldbalanceDest\" : oldbalanceDest,\n",
    "        \"newbalanceDest\" : newbalanceDest\n",
    "    }])\n",
    "\n",
    "    prediction = model.predict(input_data)[0]\n",
    "\n",
    "    st.subheader(f\"Prediction : '{int(prediction)}'\")\n",
    "    if prediction == 1:\n",
    "        st.error(\"This transaction can be fraud\")\n",
    "    else :\n",
    "        st.success(\"This transaction looks like it is not a fraud\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": none,
   "id": "3dbf0028-b0aa-41ea-8c80-7a456c823a48",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
