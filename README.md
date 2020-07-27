# Diabetes/Heart_disease Dtection web api
## Table of Content
* [Demo](#demo)
* [Overview](#overview)
* [Motivation/Purpose](#Motivation/Purpose)
* [Technical Aspect](#technical-aspect)
* [Installation](#installation) 
* [Run](#run)
* [Deployement on Heroku](#deployement-on-heroku)
* [Directory Tree](#directory-tree)
* [Technologies Used](#technologies-used)
* [Team](#team)
* [License](#license)
* [Credits](#credits)

## Demo
Link:--> https://quick-health-checkup-api.herokuapp.com
<br>
PHOTO

## Overview
Simple Flask app for Diabetes and Heart patient to monitor/check their health status. <a href="https://www.kaggle.com/akhileshdkapse/starter-guide-eda-acc-87-precision-92">Model1</a> (`diabetes_pima.pkl`) trained over diabetes <a href="https://www.kaggle.com/uciml/pima-indians-diabetes-database">dataset</a> and Model2 (`Heart_model_final.pkl`) is trained over heart disease <a href="https://www.kaggle.com/ronitf/heart-disease-uci">dataset</a>. To make use of this web app you must fill up respected form with valid inputs and boom!!..Model will predict and comment it out with proper guidance/advice about your health results, which will definitely make your health bettter. 
<br>
<strong>Routes Distribution...</strong><br>
<strong>Check for diabete page:</strong><br>
          This is a ML oriented Web Application for detection of the diabetes based on the parameters that the user enters.
          <br>
<strong>Check for heart disease page:</strong><br>
          This is a ML oriented Web Application for detection of presence of heart disease based on the parameters that the user enters.
          <br>
<strong>Covid page:</strong><br>
          Page specially design for reminding people to do their duty well. Alse for thanking special people on this earth !

## Motivation/Purpose
   - **Now in this pandemic situation of covid 19, there is a high risk of getting covid affected if we go out for health check-ups specially in Hospitals serving as a Covid centers. To stop the spread out this virus we have to be in home.** Taking this thought in an account, I have made this small and effective web app which will somehow contribute in making yhe world safe and healthy!  
   - Want to contribute in Medical/Health sector by providing simple, easy to use web api for detecting diabetes and presence of heart disease which can easily practised by a person working in this sector.

## Technical Aspect
This project is divided into Three part:
1.  Use of machine learning techniques to fit our data and Hypertune model parameters for its better performance.(*Jump to traning model part by clicking on Model1 in Overview section*)
2. Downloading data and our trained models(`.pkl file formate`) from kaggle kernels and setting up environment to run our app in local machine .
3. Building and hosting a Flask web app on Heroku(PAAS).

## Installation
The Code is written in Python 3.7 in an anaconda environment. For anaconda instalation click <a href="https://www.anaconda.com/products/individual">here</a>.To make new environment in anaconda run following commands in your **Anaconda Prompt**.
```
conda create -n your_env_name python=3.7.x
```

## Run
After successfully creating anaconda environment, install the required packages and libraries by running this command in the project directory after cloning the repository:
```
pip install -r requirements.txt
```
then by running the following command, it will host this page in your local port and will also give you local link, which you can put in any web browser.
```
python app.py
``` 

## Deployement on Heroku
Vist <a href="Deployement on Heroku">here</a> for details.
PHOTO(heroku)

## Directory Tree
```
├── templates
│   ├── Base.html
│   ├── home.html
│   ├── diabetes.html
│   ├── heart.html
│   └── covid.html
├── static
│   ├── images.jpg/.png/.gif
├── app.py
├── Heart_model_final.pkl
├── diabetes_pima.pkl 
├── diabetes_scaler.bin
├── diabetes.py
├── heart_mod.py
├── .gitignore
├── README.md
├── requirements.txt
├── LICENSE
├── Procfile
└──README.md

```
