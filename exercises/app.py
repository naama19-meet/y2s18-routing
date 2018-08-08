from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/student_id/<int:student_id>')
def display_student(student_id):
    find = query_by_id(student_id)

    return render_template('student.html', student_id=student_id, student=find)


app.run(debug=True)
