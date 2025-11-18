from flask import Flask, render_template, jsonify, Response, request, session, redirect, url_for
from bson.json_util import dumps
from pymongo import MongoClient
from dotenv import load_dotenv
from auth import authenticate, login_required
import os

load_dotenv()
app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_SECRET_KEY")

client = MongoClient(os.getenv('MONGO_URI'))
db = client.get_database('test')

courses_collection = db.get_collection('courses')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if authenticate(username,password):
            session["user"] = username
            return redirect(url_for("home"))
        return "Invalid credentials, refresh page to try again",401
    return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("home"))


@app.route('/courses')
@login_required
def show_courses():
    courses = list(courses_collection.find())
    return render_template('course_list.html', courses=courses)

@app.route('/courses/<code>')
@login_required
def course_detail(code):
    course = courses_collection.find_one({'code': code.upper()})
    return render_template('course_detail.html', course=course)

@app.route('/')
@login_required
def home():
    return render_template('homepage.html')

@app.route('/uploads')
@login_required
def upload():
    return render_template('upload.html')

@app.route('/api/course/<code>')
@login_required
def get_course_json(code):
    course = courses_collection.find_one({'code': code.upper()})
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    return Response(dumps(course), mimetype='application/json')