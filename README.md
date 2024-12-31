# Fraud Detection Project

---

This project involves predicting fraud in transactions using advanced machine learning techniques and data preprocessing methods. The dataset includes various transaction details, such as card information, email domains, and device details, making it a rich source for feature engineering and analysis.

---

## Project Description

The objective of this project is to:

- Detect fraudulent transactions using supervised and unsupervised learning methods.
- Explore data visualization and preprocessing techniques to enhance feature quality.
- Implement advanced machine learning and deep learning models for fraud detection.

---


## Data Visualization

Several visualizations were created to explore the dataset and understand feature distributions. Below are the key plots and their descriptions:

1. **Fraud Distribution Pie Chart:** Visualizes the proportion of fraudulent vs. non-fraudulent transactions.
![query](https://github.com/sameena93/fraud_detection/blob/main/static/fraud%20distribution.png)

2. **Feature Distribution (cols=['id_30', 'id_31', 'id_33', 'DeviceInfo']):** 
   - Plotted using count plots for categorical variables to display their distributions.
   - 
![querysc](https://github.com/sameena93/fraud_detection/blob/main/static/featuredistr1.png)
![querysc](https://github.com/sameena93/fraud_detection/blob/main/static/featuredistr2.png)

3. **Email Domain and Card Details (cols=['P_emaildomain', 'R_emaildomain', 'card1', 'card2', 'card3', 'card5', 'addr1', 'addr2']):** 
   - Count plots show the frequency of different values in each feature.
   - 
![querysc](https://github.com/sameena93/fraud_detection/blob/main/static/emaildomian.png)


4. **Product and Device Information (cols=['ProductCD', 'card4', 'card6', 'M4', 'M1', 'M2', 'M3', 'M5', 'M6', 'M7', 'M8', 'M9', 'DeviceType']):**
   - Count plots visualize the frequency of key categorical features.
   
![querysc](https://github.com/sameena93/fraud_detection/blob/main/static/carddetail.png)

5 **Imbalanced Data Distribution:** A count plot of the `isFraud` column highlights the data imbalance.

![](https://github.com/sameena93/fraud_detection/blob/main/static/count%20plot%20of%20fraud.png)

6. **Transaction Timestamp Analysis:** Histograms for `TransactionDT` show the distribution of transactions over time for training and test datasets.

![querysc](https://github.com/sameena93/fraud_detection/blob/main/static/transaction%20of%20timestamp.png)

---

## Data Preprocessing

Key data preprocessing steps include:

1. **Handling Missing Values:** Imputed missing values using statistical techniques.
2. **Feature Engineering:**
   - Extracted OS names from `id_30`.
   - Split email domains into servers and suffixes (`P_emailserver`, `P_suffix`, `R_emailserver`, `R_suffix`).
   - Extracted browser and device names from `id_31` and `DeviceInfo`.
3. **Outlier Removal:** Applied Z-score to remove outliers.
4. **Encoding Categorical Features:** Utilized one-hot encoding and label encoding for categorical variables.
5. **Standardization:** Normalized numerical features to standard scales.
6. **SMOTE:** Balanced the dataset classes using Synthetic Minority Oversampling Technique (SMOTE).

---

## Modeling and Techniques

Multiple machine learning and deep learning models were implemented:

1. **Dimensionality Reduction:**
   - Applied PCA for feature selection and dimensionality reduction.
2. **Feature Importance:**
   - Visualized using Random Forest and XGBoost.
3. **Machine Learning Models:**
   - Random Forest
   - XGBoost
4. **Deep Learning Models:**
   - LSTM Autoencoder for anomaly detection.
5. **Stacking Models:**
   - Combined multiple models for improved accuracy.

---

## Repository Structure

- **code/**: Python scripts for preprocessing, modeling, and evaluation.
- **data/**: Includes training and test datasets.
- **images/**: Contains graphs and plots used in the project.
- **README.md**: Comprehensive project documentation.





