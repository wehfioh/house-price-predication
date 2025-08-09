index.html
from flask import Flask, render_template, request  # Added 'request' import
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('House_price_prediction.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from the form
        features = [
            float(request.form['CRIM']),
            float(request.form['ZN']),
            float(request.form['INDUS']),
            float(request.form['CHAS']),
            float(request.form['NOX']),
            float(request.form['RM']),
            float(request.form['AGE']),
            float(request.form['DIS']),
            float(request.form['RAD']),
            float(request.form['TAX']),
            float(request.form['PTRATIO']),
            float(request.form['B']),
            float(request.form['LSTAT'])
        ]
        # Reshape features for prediction
        features = np.array(features).reshape(1, -1)
        prediction = model.predict(features)
        return render_template('index.html', prediction_text=f'Predicted House Price: ${prediction[0]:,.2f}')
    except Exception as e:
        return render_template('index.html', prediction_text='Error in prediction. Please check your input.')

# Ensure proper indentation for the main block
if __name__ == '__main__':
    app.run(debug=True)
    C:\Users\Dell\Desktop\House Price Prediction\House Price Prediction\venv\Scripts\python.exe