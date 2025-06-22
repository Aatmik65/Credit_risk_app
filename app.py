{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "322137f6-2582-4b35-bb77-0b30106291c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-22 15:12:55.478 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\somya Nigam\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-06-22 15:12:55.506 Session state does not function when running a script without `streamlit run`\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "\n",
    "# Load the trained model (you can train it here for simplicity)\n",
    "data = pd.read_csv(\"C:\\\\Users\\\\somya Nigam\\\\Downloads\\\\credit_risk_dataset.csv\")\n",
    "X = data.drop('default', axis=1)\n",
    "y = data['default']\n",
    "model = RandomForestClassifier(random_state=42)\n",
    "model.fit(X, y)\n",
    "\n",
    "st.title(\"Credit Risk Prediction\")\n",
    "\n",
    "# User input\n",
    "age = st.number_input('Age', min_value=18, max_value=100)\n",
    "income = st.number_input('Income', min_value=0)\n",
    "loan_amount = st.number_input('Loan Amount', min_value=0)\n",
    "credit_score = st.number_input('Credit Score', min_value=300, max_value=850)\n",
    "employment_years = st.number_input('Employment Years', min_value=0, max_value=50)\n",
    "\n",
    "if st.button('Predict'):\n",
    "    input_data = pd.DataFrame([[age, income, loan_amount, credit_score, employment_years]],\n",
    "                              columns=['age', 'income', 'loan_amount', 'credit_score', 'employment_years'])\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    if prediction == 1:\n",
    "        st.error(\"High risk: Likely to default.\")\n",
    "    else:\n",
    "        st.success(\"Low risk: Likely to repay.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb072d76-2b21-40b2-82f6-f6ae4f034733",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
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
