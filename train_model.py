{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f38370a2-ef3a-480e-bf51-fe508f7e3994",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "# Load your dataset\n",
    "data = pd.read_csv('credit_risk_dataset.csv')\n",
    "\n",
    "# Split data into features and target\n",
    "X = data.drop('default', axis=1)\n",
    "y = data['default']\n",
    "\n",
    "# Split into training and test sets\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Build the model\n",
    "model = RandomForestClassifier(random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Test the model\n",
    "y_pred = model.predict(X_test)\n",
    "print(\"Accuracy:\", accuracy_score(y_test, y_pred))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "",
   "name": ""
  },
  "language_info": {
   "name": ""
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
