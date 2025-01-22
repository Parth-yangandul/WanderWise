# WanderWise

## Overview
This project predicts the price of flights based on various input features such as departure and arrival times, flight duration, airline, source, destination, and the number of stops. The prediction is powered by a machine learning model trained on historical flight data.

## Features
- **Input Features**:
  - Airline
  - Source
  - Destination
  - Number of stops
  - Journey date
  - Departure time
  - Arrival time
  - Duration of flight
- **Output**:
  - Predicted flight price

## Dataset
The dataset used in this project contains information about flight details, including airlines, source and destination cities, flight duration, and prices. Data preprocessing includes handling missing values, feature encoding, and scaling.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - pandas, numpy: Data manipulation and analysis
  - sklearn: Machine learning algorithms and preprocessing
  - flask: Web application framework
  - matplotlib, seaborn: Data visualization

## Workflow
1. **Data Preprocessing**:
   - Handling missing values
   - Encoding categorical variables using LabelEncoder or OneHotEncoder
   - Scaling numerical features
2. **Feature Engineering**:
   - Extracting day and month from the journey date
   - Calculating flight duration in hours and minutes
3. **Model Training**:
   - Training a Random Forest Regressor model on the processed data
   - Evaluating the model using metrics like RMSE and R^2
4. **Web Application**:
   - Building a Flask-based web app for user interaction
   - Taking user inputs and predicting flight prices

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flight-price-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd flight-price-prediction
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```

## Usage
1. Open your web browser and navigate to `http://127.0.0.1:5000/`.
2. Enter the flight details such as airline, source, destination, and travel dates.
3. Click the "Predict" button to view the predicted flight price.

## Example
For a flight with the following details:
- Airline: Jet Airways
- Source: Delhi
- Destination: Cochin
- Journey Date: 2024-01-15
- Departure Time: 10:00
- Arrival Time: 13:00
- Number of Stops: 1

The predicted price might be: **INR 5,400**.

## Folder Structure
```
flight-price-prediction/
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── static/              # Static files (CSS, JS, images)
├── templates/           # HTML templates
├── data/                # Dataset
└── README.md            # Project documentation
```

## Future Improvements
- Incorporate real-time data for better predictions.
- Add more features like seat type and booking time.
- Deploy the application using cloud platforms such as AWS or Heroku.

## Credits
This project is inspired by various flight price prediction initiatives and machine learning techniques. Special thanks to the online resources and tutorials that guided the development process.

## License
This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

