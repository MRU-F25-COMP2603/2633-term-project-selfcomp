import mongoose from "mongoose";

const commentSchema = new mongoose.Schema({
    author: String,
    text: String,
    timestamp: { type: Date, default: Date.now }
});

const courseSchema = new mongoose.Schema({
    code: String, //Comp2633
    title: String, //software engineering
    description: String,
    comments: [commentSchema]
});

export const Course = mongoose.model("Course", courseSchema);