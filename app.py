from flask import Flask, request , render_template
import numpy as np
import pickle
import diabetes, heart_mod

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/Dabetes_check', methods=['Get','POST'])
def dabetes():
    form_not_filled=True
    result=None
    if request.method=='POST':
        input_dict=request.form
        array= diabetes.pre_process(input_dict)
        result=diabetes.predict(array)
        form_not_filled=False
    return render_template('diabetes.html', form_not_filled=form_not_filled, result=result)


@app.route('/Heart_check', methods=['Get','POST'])
def heart():
    form_not_filled=True
    result=None
    if request.method=='POST':
        input_dict=request.form
        array= heart_mod.pre_process(input_dict)
        result=heart_mod.predict(array)
        form_not_filled=False
        print(result)
    return render_template('heart.html', form_not_filled=form_not_filled, result=result)


@app.route('/Covid Info.')
def covid():
    return render_template('covid.html')



if __name__=='__main__':
    app.run()
