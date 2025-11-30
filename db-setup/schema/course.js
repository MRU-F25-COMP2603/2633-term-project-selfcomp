const mongoose = require('mongoose');

const commentSchema = new mongoose.Schema({
    author: String,
    text: String,
    timestamp: { type: Date, default: Date.now }
});

const instructorSchema = new mongoose.Schema({
    name: String,
    terms: [String]
});

const courseSchema = new mongoose.Schema({
    code: String,
    title: String,
    description: String,
    prerequisites: String,
    Hours: String,
    instructors: [instructorSchema],
    comments: [commentSchema]
});

const Course = mongoose.model("Course", courseSchema);
const Comment = mongoose.model("Comment", commentSchema);
const Instructor = mongoose.model("Section", instructorSchema);
module.exports = { Course, Comment, Instructor};