Crop Recommendation System 🌱
A machine learning-based web application that recommends the optimal crop to grow based on soil and environmental factors. This project uses a trained LightGBM classifier to provide accurate crop suggestions.

## Overview
The goal of this project is to help farmers and agricultural enthusiasts make informed decisions about crop selection. By providing key soil metrics (Nitrogen, Phosphorous, Potassium, and pH) and environmental conditions (temperature, humidity, and rainfall), the system predicts the most suitable crop from a dataset of 22 common crops.

The application is built with a Python Flask backend and a simple HTML/CSS frontend.

## Features
Intelligent Recommendations: Utilizes a LightGBM model with ~99% accuracy to predict the best crop.

Wide Crop Variety: Trained on a dataset including 22 different crops like rice, maize, jute, cotton, coconut, fruits, and more.

User-Friendly Interface: A clean and simple web form for easy input of parameters.

Real-time Prediction: Get instant crop recommendations after submitting the required data.

Scalable: The Flask backend is lightweight and can be easily deployed to various cloud platforms.

## Tech Stack
Backend: Python, Flask

Machine Learning: Scikit-learn, LightGBM, Pandas, NumPy

Frontend: HTML, CSS

Deployment: Can be run locally and is ready for deployment on platforms like Heroku, PythonAnywhere, or AWS.

## Dataset
The model was trained on the "Crop Recommendation Dataset" from Kaggle. This dataset contains 2200 data points with 7 features (N, P, K, temperature, humidity, ph, rainfall) and one target label (the crop).

You can find the dataset here.

## Installation & Usage
Follow these steps to run the project on your local machine.

### Prerequisites
Python 3.8+

pip (Python package installer)

### 1. Clone the Repository
Bash

git clone https://github.com/mukharbajpai/crop-recommendation-system.git
cd crop-recommendation-system
### 2. Create a Virtual Environment (Recommended)
Bash

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
### 3. Install Dependencies
Install all the required libraries from the requirements.txt file.

Bash

pip install -r requirements.txt
### 4. Run the Application
Start the Flask server.

Bash

python app.py
### 5. Access the Web App
Open your web browser and navigate to the following URL:

http://127.0.0.1:5000
You should now see the application's home page. Fill in the form and get your crop recommendation!

## Project Structure
crop-recommendation-system/
├── templates/
│   └── index.html         # Frontend HTML template
├── app.py                 # Main Flask application script
├── crop_recommendation_model.joblib # Pre-trained LightGBM model
├── crop-recommendation-system.ipynb # Jupyter Notebook for model training & EDA
├── requirements.txt       # List of Python dependencies
└── README.md              # Project documentation
## Contributing
Contributions are welcome! If you have any ideas, suggestions, or want to fix a bug, please feel free to open an issue or create a pull request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
