from flask import Flask, render_template, jsonify, Response
from bson.json_util import dumps
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient(os.getenv('MONGO_URI'))
db = client.get_database('test')
courses_collection = db.get_collection('courses')

@app.route('/courses')
def show_courses():
    courses = list(courses_collection.find())
    return render_template('course_list.html', courses=courses)

@app.route('/courses/<code>')
def course_detail(code):
    course = courses_collection.find_one({'code': code.upper()})
    return render_template('course_detail.html', course=course)

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/uploads')
def upload():
    return render_template('upload.html')

@app.route('/api/course/<code>')
def get_course_json(code):
    course = courses_collection.find_one({'code': code.upper()})
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    return Response(dumps(course), mimetype='application/json')