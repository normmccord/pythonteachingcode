'''
This is a basic web page running with Flask.
'''
# There is no link to Hiroku in D2L.  I also can't use it because I couldn't convince GitHub that I'm a student.  They didn't like that I live in Illinois, and they didn't take any visual proof (my student ID) showing that I'm actually a student at Kenessaw.

from flask import Flask, render_template, request
#This is the Flask object, we are creating an instance of the Flask class and storing it in the variable app
#__name__ is a special variable in Python that is the name of the module, which is this file's name without the .py extension
app=Flask(__name__)

#This is a decorator, it is a function that takes a function as a parameter!
#A decorator is a function that wraps another function
#This decorator is saying that when someone goes to the URL /greet, run the greet function
@app.route('/greet', methods=['POST'])
def greet():
    inputName = request.form['myName']
    ip = request.remote_addr
    #write data to file or to DB
    inputName = inputName.upper()+" hi!  Visiting from " + str(ip)
    return render_template("home.html",myName=inputName)

@app.route('/')
def home():  
    return render_template("home.html",myName="Type your name in the box and click submit!")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/norman/')
def norman():
    return render_template("mccord.html")

if __name__=="__main__":
    app.run(debug=True)
