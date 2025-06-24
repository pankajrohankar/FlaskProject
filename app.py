#import lib
from flask import Flask, request, render_template, url_for, redirect, jsonify

app = Flask(__name__)

#Main Route
@app.route("/",methods=["GET"])
def welcome():
    return("<h1>Welcome to Flask Learning</h1>")


@app.route('/home/<int:name>')
def home(name):
    return "Welcome "+str(name)+", to home page."


@app.route("/index",methods=["GET"])
def index():
    return("<h2>Welcome to index page</h2>")


@app.route("/success/<int:score>")
def success(score): 
    return "<h2>Student passed with scored marks : "+str(score)+" </h2>"

@app.route("/fail/<int:score>")
def fail(score): 
    return "<h2>Student failed with scored marks : "+str(score)+" </h2>"

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('calculate.html')

    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        num3 = float(request.form['num3'])
        avg = (num1 + num2 + num3) / 3

        #return render_template('calculate.html',average=avg)
        if avg >= 40:
            return redirect(url_for('success', score=avg))
        else:
            return redirect(url_for('fail', score=avg))
    
@app.route('/api',methods=['POST'])
def api():
    data = request.get_json()
    a_val = dict(data)['a']
    b_val = dict(data)['b']

    return (str(a_val+b_val))


if __name__ == "__main__":
    app.run(debug=True)




 

 











