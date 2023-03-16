from flask import Flask, render_template, request
import config_path
import app.user_test
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("front_end.html")

@app.route("/get_data", methods = ["POST"])
def data():
    input_data = request.form
    print(input_data)
    return render_template("front_end.html",PREDICT_VALUE=iris_value)

if __name__ == '__main__':
    app.run(host=config_path.HOST_NAME, port= config_path.PORT_NUMBER, debug =True)






# 00000000000000000000000000000000


    
    # data = np.zeros(len(col))
    # data[0] = input_data['sepal_length']
    # data[1] = input_data['sepal_width']
    # data[2] = input_data['petal_length']
    # data[3] = input_data['petal_width']
    
    # result = model.predict([data])
    # print(result)

    # if result[0] == 1:
    #     iris_value = "SETOSA"
    # if result[0] == 2:
    #     iris_value = "VERSICOLOR"
    # if result[0] == 3:
    #     iris_value = "VIRGINICA"

    # 
