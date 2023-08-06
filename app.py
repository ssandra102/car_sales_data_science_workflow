from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            ppf =float(request.form['ppf'])
            efficiency =float(request.form['efficiency'])
            capacity =float(request.form['capacity'])
            size =float(request.form['size'])
            Horsepower =float(request.form['Horsepower'])
            Wheelbase =float(request.form['Wheelbase'])
            Width =float(request.form['Width'])
            Length =float(request.form['Length'])
       
         
            data = [ppf,efficiency,capacity,size,Horsepower,Wheelbase,Width,Length]
            data = np.array(data).reshape(1, 8)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	# app.run(host="0.0.0.0", port = 8080, debug=True)
	app.run(host="0.0.0.0", port = 8080)