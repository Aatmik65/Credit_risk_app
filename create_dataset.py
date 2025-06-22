{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "74e7f8bc-76c5-48cc-a329-c1e257349393",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dataset created and saved as credit_risk_dataset.csv\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "\n",
    "# Number of samples (rows) in your dataset\n",
    "N = 500\n",
    "\n",
    "# Generate random data for each column\n",
    "np.random.seed(42)  # For consistent results each time you run\n",
    "\n",
    "age = np.random.randint(18, 70, size=N)\n",
    "income = np.random.randint(20000, 200000, size=N)\n",
    "loan_amount = np.random.randint(1000, 50000, size=N)\n",
    "credit_score = np.random.randint(300, 850, size=N)\n",
    "employment_years = np.random.randint(0, 40, size=N)\n",
    "\n",
    "# Calculate a simple risk score for default\n",
    "risk_score = (\n",
    "    0.3 * (income < 50000).astype(int) +\n",
    "    0.4 * (loan_amount > 30000).astype(int) +\n",
    "    0.3 * (credit_score < 600).astype(int) +\n",
    "    0.2 * (employment_years < 2).astype(int)\n",
    ")\n",
    "\n",
    "# Convert risk_score to default (1 = default, 0 = no default)\n",
    "default = (risk_score + np.random.rand(N) > 0.8).astype(int)\n",
    "\n",
    "# Create a DataFrame and save as CSV\n",
    "df = pd.DataFrame({\n",
    "    'age': age,\n",
    "    'income': income,\n",
    "    'loan_amount': loan_amount,\n",
    "    'credit_score': credit_score,\n",
    "    'employment_years': employment_years,\n",
    "    'default': default\n",
    "})\n",
    "\n",
    "df.to_csv('credit_risk_dataset.csv', index=False)\n",
    "print(\"Dataset created and saved as credit_risk_dataset.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a45a1890-bfbf-407e-a435-0df6b29dafcb",
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
