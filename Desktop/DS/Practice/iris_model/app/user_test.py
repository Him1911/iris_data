import pickle
import json
import numpy as np
import os 



class Prediction():
    def __init__(self):
        print(os.getcwd())


    with open(config_path.MODEL_PATH,'rb') as file:
        model = pickle.load(file)

    with open(config_path.ASSET_PATH,'r') as file:
        asset = json.load(file)

    col = asset['columns']

    def data():
        input_data = request.form
        print(input_data)
        
        data = np.zeros(len(col))
        data[0] = input_data['sepal_length']
        data[1] = input_data['sepal_width']
        data[2] = input_data['petal_length']
        data[3] = input_data['petal_width']
        
        result = model.predict([data])
        print(result)

        if result[0] == 1:
            iris_value = "SETOSA"
        if result[0] == 2:
            iris_value = "VERSICOLOR"
        if result[0] == 3:
            iris_value = "VIRGINICA"
            return result
    
# if __name__ == "__main__":
 
#     pred_obj = Prediction()
#     pred_obj.load_raw()