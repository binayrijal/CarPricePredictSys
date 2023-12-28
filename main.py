from flask import  Flask,render_template,request
import pandas as pd
import numpy as np


app=Flask(__name__)
car=pd.read_csv("processed_data.csv")

@app.route('/')
def home():
    company=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique(), reverse=True)
    fuel_type=car['fuel_type'].unique()
    return render_template('index.html',company=company,car_models=car_models,year=year,fuel_type=fuel_type)


@app.route('/predict')
def predict():
    company=request.form.get('company')
    car_models=request.form.get('car_models')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven=int(request.form.get('kms_driven'))
    print(company,car_models,year,fuel_type,kms_driven)

    return ""





if __name__=="__main__":
    app.run(debug=True)
