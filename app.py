from flask import Flask, render_template, request

import marks as m

# Lets create a webpage

app = Flask(__name__)

# This is the pattern of our URL
@app.route("/", methods = ['GET', 'POST'])
def marks():
    if request.method == "POST":
        hrs = request.form["hrs"]
        marks_pred = m.marks_prediction(hrs)
        mks = marks_pred
    else:
        mks = "Enter the marks"
        #print(marks_pred)
    return render_template("index.html", my_marks = mks)




# @app.route("/submit", methods =['POST'])
# def submit():
#     # Here, we are taking data from HTML file to Python file
#     if request.method == "POST":
#         # Its a dictionary, therefore in square brackets
#         name = request.form["username"]

#     # Here, we are pushing data from Python file to HTML file    
#     return render_template("submit.html", n = name)


if __name__ == "__main__":
    app.run(debug=True)
