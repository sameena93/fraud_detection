import pandas as pd
from sqlalchemy import create_engine, text
import xgboost as xgb
import joblib
# import warnings
# warnings.filterwarnings("ignore")

from flask import Flask, render_template_string
import time

app = Flask(__name__)

# Load scaler and models
scaler = joblib.load("./models/scaler.pkl")
# rf_model = joblib.load("./models/Random Forest.pkl")
xgb_model = joblib.load("./models/XGBoost.pkl")

import sys
print(sys.version)
# print(type(rf_model))  # Should output <class 'sklearn.ensemble._forest.RandomForestClassifier'>
print(type(xgb_model)) # Should output <class 'xgboost.sklearn.XGBClassifier'>
print(type(scaler))

#Engine :Database connection
try:
    engine = create_engine("mysql+pymysql://root:Elecrow%40123@localhost:3306/fraud_detection")
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Database connection successful.")
except Exception as e:
    print(f"Error connecting to database: {e}")

 
# Function to process data in chunks
def process_data():

    query = "SELECT * FROM test_data_table limit 50"
    print(query)
    chunk_size = 1000  # Adjust based on your needs
    chunks = pd.read_sql(query, engine, chunksize=chunk_size)
    
    # Take sample data
    for chunk in chunks:
        # Drop TransactionID column
        chunk = chunk.drop(columns=['TransactionID'])
        
        # Take a sample of 50 rows
        sample_data = chunk.sample(n=5, random_state=42)
        print('query' , sample_data)
        # Preprocess data
        X = sample_data# Assuming 'fraud' is the target column if it's there
        X_scaled = scaler.transform(X)
        print('scaler', X_scaled)
        # Predict using XGBoost model
        predictions = xgb_model.predict(X_scaled)
        print("prediction", predictions)
        # Add predictions to the sample data
        sample_data['Prediction'] = predictions
        
        # Display the first 10 rows
        first_10_rows = sample_data.head(5)
        
        return first_10_rows

@app.route('/')
def index():
    sample_data = process_data()
    
    # HTML template to display the data
    html_template = '''
    <html>
        <head>
            <title>Prediction Results</title>
        </head>
        <body>
            <h1>Prediction Results</h1>
            <table border="1">
                <thead>
                    <tr>
                        {% for column in sample_data.columns %}
                            <th>{{ column }}</th>
                        {% endfor %}
                    </tr>
                </thead>
                <tbody>
                    {% for index, row in sample_data.iterrows() %}
                        <tr>
                            {% for column in sample_data.columns %}
                                <td>{{ row[column] }}</td>
                            {% endfor %}
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </body>
    </html>
    '''
    
    return render_template_string(html_template, sample_data=sample_data)

if __name__ == '__main__':
    app.run(debug=True)