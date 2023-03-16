from flask import Flask, render_template, request
app=Flask(__name__)

@app.route('/')

def index():

    return render_template("front_end.html")

if __name__ == '__main__':
    app.run(port=5000, debug =True)