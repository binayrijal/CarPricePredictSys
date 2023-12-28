from flask import  Flask,render_template,request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)
car=pd.read_csv("processed_data.csv")
model=pickle.load(open("LinearRegressionmodel.csv",'rb'))

@app.route('/')
def home():
    company=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique(), reverse=True)
    fuel_type=car['fuel_type'].unique()
    return render_template('index.html',company=company,car_models=car_models,year=year,fuel_type=fuel_type)


@app.route('/predict', methods=['POST'])
def predict():
    company=request.form.get('company')
    car_models=request.form.get('car_models')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kms_driven'))
    prediction = model.predict(pd.DataFrame([[car_models,company,year,kms_driven,fuel_type]],columns=['name','company','year','kms_driven','fuel_type']))

    return str(np.round(prediction[0],2))





if __name__=="__main__":
    app.run(debug=True)
