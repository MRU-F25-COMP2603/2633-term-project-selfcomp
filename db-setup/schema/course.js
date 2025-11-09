import mongoose from "mongoose";

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

export const Course = mongoose.model("Course", courseSchema);
export const Comment = mongoose.model("Comment", commentSchema);