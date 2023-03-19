from flask import Flask, render_template, request
import config_path
from app.user_test import Prediction
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("front_end.html")

@app.route("/get_data", methods = ["POST","GET"])
def iris_pred():
    data = request.form
    pred_obj= Prediction()
    iris_predicted = pred_obj.iris_pred(data)
    print(iris_predicted)
    return render_template("front_end.html", PREDICT_VALUE= iris_predicted)

if __name__ == '__main__':
    app.run(host=config_path.HOST_NAME, port= config_path.PORT_NUMBER, debug =True)

