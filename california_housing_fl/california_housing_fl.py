from flask import Flask, session, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField
from wtforms.validators import DataRequired
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

with open(r'C:\Users\Sahil\Data science Machine Learning\Flask_bootcamp\flask_tut\california_housing_fl\model.pkl', 'rb') as f:
    model = pickle.load(f)

class CalHouse(FlaskForm):
    medinc = FloatField('Enter medinc', validators=[DataRequired()])
    houseage = FloatField('Enter houseage', validators=[DataRequired()])
    averooms= FloatField('Enter averooms', validators=[DataRequired()])
    avebdrms= FloatField('Enter avebdrms', validators=[DataRequired()])
    population= FloatField('Enter population', validators=[DataRequired()])
    aveoccup= FloatField('Enter aveoccup', validators=[DataRequired()])
    latitude= FloatField('Enter latitude', validators=[DataRequired()])
    longitude= FloatField('Enter longitude', validators=[DataRequired()])
    submit = SubmitField('Predict price')


@app.route('/', methods = ['GET', 'POST'])
def index():
    form = CalHouse()

    if form.validate_on_submit():
        session['medinc'] = form.medinc.data
        session['houseage'] = form.houseage.data
        session['averooms'] = form.averooms.data
        session['avebdrms'] = form.avebdrms.data
        session['population'] = form.population.data
        session['aveoccup'] = form.aveoccup.data
        session['latitude'] = form.latitude.data
        session['longitude'] = form.longitude.data
        return redirect('predict')
    
    return render_template('home.html', form = form)


@app.route('/predict', methods = ['GET', 'POST'])
def predict():
    result = model.predict([[session['medinc'], session['houseage'], session['averooms'],  session['avebdrms'], session['population'],
                              session['aveoccup'], session['latitude'],   session['longitude']]])
    return render_template('result.html', result = result[0])


if __name__ == '__main__':
    app.run()