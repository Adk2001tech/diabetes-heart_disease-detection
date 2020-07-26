import numpy as np
import pickle

with open("diabetes_pima.pkl", "rb") as input_file:
    model_diabetes = pickle.load(input_file)

with open("diabetes_scaler.bin", "rb") as input_file:
    scalar_diabetes = pickle.load(input_file)



# pre_process converts input---> (1,8)dim
def pre_process(input_dict):
    array= np.array([[input_dict['Pregnancies'], input_dict['Glucose'], input_dict['BloodPressure'], input_dict['SkinThickness'],
                    input_dict['Insulin'], input_dict['BMI'], input_dict['Diabetes_pedigree'], input_dict['Age']]])
    return scalar_diabetes.transform(array)


# predict results......  1(diabetes patient)-----0(NON diabetes patient)
def predict(arr):
    return model_diabetes.predict(arr)
