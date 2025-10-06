from flask import Flask, request, render_template
from pyngrok import ngrok, conf
import joblib
import numpy as np
import os

# --- IMPORTANT ---
# Paste your new authtoken here
AUTHTOKEN = "33ePfcfmJm8jQdEqRuCNT2PR2MB_3V1tMahxjuZ8TJU9ajM9G"
# -----------------

conf.get_default().auth_token = AUTHTOKEN

# Initialize the Flask app
app = Flask(__name__)

# Open a tunnel to the Flask app
public_url = ngrok.connect(5000).public_url
print(f" * Tunnel URL: {public_url}")

# Load the trained model
model = joblib.load('crop_recommendation_model.joblib')

# Define the home page route
@app.route('/')
def home():
    # Update the action URL in the form to use the public URL
    return render_template('index.html', action_url=f"{public_url}/predict")

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    output = prediction[0]
    # Re-render the page with the result
    return render_template('index.html', prediction_text=f'The recommended crop is: {output}', action_url=f"{public_url}/predict")

# Run the app
if __name__ == "__main__":
    app.run(port=5000)
