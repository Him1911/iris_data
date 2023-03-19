import pickle
import json
import numpy as np
import os 
from app import config_path
# from flask import request

class Prediction():
    def __init__(self):
        print(os.getcwd())

    def load_raw(self):
        with open(config_path.MODEL_PATH,'rb') as model_file:
            self.logi_model = pickle.load(model_file)

        with open(config_path.ASSET_PATH,'r') as col_file:
            self.asset = json.load(col_file)

        # col = self.asset['columns']c

        print(f"we are in load raw")

    def iris_pred(self,data):
        self.load_raw()
        self.data= data

        
        data = np.zeros(len(self.asset['columns']))
        data[0] = self.data['sepal_length']
        data[1] = self.data['sepal_width']
        data[2] = self.data['petal_length']
        data[3] = self.data['petal_width']

        result = self.logi_model.predict([data])
        print(result)


        if result[0] == 1:
            iris_predicted = "SETOSA"
        if result[0] == 2:
            iris_predicted = "VERSICOLOR"
        if result[0] == 3:
            iris_predicted = "VIRGINICA"
    
        return iris_predicted
    
if __name__ == "__main__":
 
    pred_obj= Prediction()
    pred_obj.load_raw()