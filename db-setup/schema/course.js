const mongoose = require('mongoose');

const commentSchema = new mongoose.Schema({
    author: String,
    text: String,
    timestamp: { type: Date, default: Date.now }
});

const courseSchema = new mongoose.Schema({
    code: String,
    title: String,
    desciption: String,
    prerequisites: String,
    Hours: String,
    comments: [commentSchema]
});

const Course = mongoose.model("Course", courseSchema);
const Comment = mongoose.model("Comment", commentSchema);

module.exports = { Course, Comment };