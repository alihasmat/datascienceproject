from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful"

@app.route('/predict', methods=['POST', 'GET'])
def prediction():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixedAcidity'])
            volatile_acidity = float(request.form['volatileAcidity'])
            citrc_acid = float(request.form['citricAcid'])
            residual_sugar = float(request.form['residualSugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['freeSulfurDioxide'])
            total_sulfur_dioxide = float(request.form['totalSulfurDioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            data=[fixed_acidity, volatile_acidity, citrc_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
            data = np.array(data).reshape(1, 11)

            obj=PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction=str(predict))
        
        except Exception as e:
            return "An error occurred: " + str(e)
        
    else:
        return render_template('index.html')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)