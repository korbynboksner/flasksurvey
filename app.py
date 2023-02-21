from flask import Flask, render_template, request, redirect
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "s"

responses = []
@app.route("/")
def start():
    return render_template("start.html", survey = satisfaction_survey)

@app.route("/setup", methods=["POST"])
def set_up():
    return redirect("/questions/0")

@app.route("/a", methods =["POST"])
def answer():
    c = request.form['answer']
    responses.append(c)
    if len(satisfaction_survey.questions) == (len(responses)):
        return render_template("done.html")
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route("/questions/<int:id>")
def q(id):


    question = satisfaction_survey.questions[id]
   
    return render_template("questions.html", q=question, id=id)






 