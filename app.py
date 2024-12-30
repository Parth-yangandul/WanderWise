from flask import Flask,request,render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

model = pickle.load(open('flight_rf.pkl','rb'))

app = Flask(__name__)

@app.route('/')
@cross_origin()
def home():
	return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method=='POST':
        dep_time = request.form['Dep_Time']

        Journey_day = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").day
        Journey_month = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").month

        Departure_hour = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").hour
        Departure_min = pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").minute
 
        arrival_time = request.form['Arrival_Time']
        Arrival_hour =  pd.to_datetime(arrival_time,format="%Y-%m-%dT%H:%M").hour
        Arrival_min =  pd.to_datetime(arrival_time,format="%Y-%m-%dT%H:%M").minute

        Total_stops = int(request.form['stops'])

        dur_hour = abs(Arrival_hour-Departure_hour)
        dur_min = abs(Arrival_min-Departure_min)

        from sklearn.preprocessing import LabelEncoder

        # Assuming you already have a trained model and LabelEncoders for each feature
        # LabelEncoders for each categorical column
        airline_encoder = LabelEncoder()
        source_encoder = LabelEncoder()
        destination_encoder = LabelEncoder()

        # Example: Pre-fit your encoders during preprocessing
        # These should be fitted on your training data
        airline_encoder.fit(['Air_ Asia', 'Air_India', 'GoAir', 'IndiGo', 'Jet_Airways', 'Jet_Airways_Business', 'Multiple_carriers', 'Multiple_carriers_Premium_economy', 'SpiceJet', 'Trujet', 'Vistara', 'Vistara_Premium_economy',])

        source_encoder.fit(['Banglore','Cochin', 'Delhi', 'Hyderabad', 'Kolkata'])
        destination_encoder.fit(['Banglore','Cochin', 'Delhi', 'Hyderabad', 'Kolkata'])

        # For Prediction:
        airline = request.form['airline']
        source = request.form['Source']
        destination = request.form['Destination']

        # Transform categorical values to integers using LabelEncoder
        airline_encoded = airline_encoder.transform([airline])[0]
        source_encoded = source_encoder.transform([source])[0]
        destination_encoded = destination_encoder.transform([destination])[0]

        # Prepare the input array for prediction
        output = model.predict([[Total_stops,
                                Journey_day,
                                Journey_month,
                                Departure_hour,
                                Departure_min,
                                Arrival_hour,
                                Arrival_min,
                                dur_hour,
                                dur_min,
                                airline_encoded,
                                source_encoded,
                                destination_encoded]])

        output = round(output[0],2)
        return render_template('home.html',predictions='You will have to Pay approx Rs. {}'.format(output))


if __name__ == '__main__':
	app.run(debug=True)