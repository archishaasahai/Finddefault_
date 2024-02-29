

https://github.com/archishaasahai/Finddefault_/assets/161445997/87c1e0f9-db10-4924-943e-9ca1ce2aac58

**Project Title:** Credit Card Fraud Detection

**Overview**

This project aims to build a robust classification model to accurately predict fraudulent credit card transactions. It addresses a significant issue in the financial industry. The solution involves the following steps:

1. **Data Preprocessing and Cleaning:**
   * Load the dataset.
   * Explore and address data quality issues (missing values, outliers, etc.).
   * Convert date features to appropriate datatypes.

2. **Feature Engineering and Selection:**
   * Apply feature engineering techniques to create informative features.
   * Employ feature selection methods to identify the most relevant features.

3. **Data Balancing:**
   * Address the class imbalance issue through techniques like undersampling.

4. **Modeling and Hyperparameter Tuning**
   * Experiment with various classification models (e.g., Logistic Regression, Random Forest, XGBoost).
   * Implement hyperparameter tuning with GridSearchCV to optimize model performance.

5. **Model Evaluation**
   * Evaluate models using metrics like accuracy, precision, recall, F1-score, and ROC-AUC.
   * Visualize model performance using confusion matrices and classification reports.

6. **Model Deployment**
   * Save the final trained model (e.g., using pickle).
   * Provide instructions for loading and utilizing the model to make predictions.

**Installation**

1. **Clone this repository:**
   ```bash
   git clone https://github.com/archishaasahai/FindDefault.git
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   cd production
   virtualenv venv
   venv\Scripts\activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

**Execution**

1. **Run the main script:**
   ```bash
   streamlit run app.py
   ```
   This script will perform all the necessary steps, including data preprocessing, model training, evaluation, and saving the final model.

**Files**

* **app.py:**  The main Python script responsible for the end-to-end pipeline.
* **requirements.txt:** Contains a list of required Python packages.
* **clf.pkl:**  The saved final model using pickle.
* **iqr_thresholds.json:** JSON file storing IQR thresholds for outlier handling.

**Usage**

After following the installation steps and running the `app.py` script:

1. Use the saved model (`clf.pkl`) and thresholds (`iqr_thresholds.json`) for predicting fraud on new credit card transactions.

Thank you for reading...
