from flask import Flask,request,render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__) # creatting object of Flask..... and __name__ gives the entry point where we need to execute
app=application

#route for home page
@app.route("/")
def index():
    return render_template("index.html") # welcome page

# route for prediction page
@app.route("/predictdata", methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return  render_template("home.html") # the page which having input fields...
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))
            ) 
        # calling CustomData() method which we have written in predict_pipeline.py file,
        #by passing the values of forms which have entered by the end user

        pred_df=data.get_data_as_dataframe()# calling get_data_as_dataframe() method which we have written in predict_pipeline.py file
        print(pred_df)

        pred_pipeline=PredictPipeline()
        results=pred_pipeline.predict(pred_df)# calling predict() method which we have written in predict_pipeline.py file
        return render_template('home.html',results=results[0]) # index 0,bcz it returns the result in list format..


if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)