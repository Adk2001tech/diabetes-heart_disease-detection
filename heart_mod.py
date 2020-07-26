import numpy as np
import pickle

with open("Heart_model_final.pkl", "rb") as input_file:
    model_heart = pickle.load(input_file)


# convert input to (1,11) dim
def pre_process(input_dict):
    return np.array([[input_dict['Age'], input_dict['sex'], input_dict['cp'], input_dict['BloodPressure'],
                    input_dict['cholesterol'], input_dict['fbs'], input_dict['restecg'], input_dict['thalach'],
                    input_dict['exang'], input_dict['oldpeak'], input_dict['slope']]])


#Predict result i.e Heart disease (0 = no, 1 = yes)
def predict(arr):
    return model_heart.predict(arr)
