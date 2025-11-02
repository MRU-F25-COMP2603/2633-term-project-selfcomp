import mongoose from "mongoose";

const courseSchema = new mongoose.Schema({
    name: {type: String, required: true},
    desciption: {type: String, required: true},
    
});

export const Course = mongoose.model("Course", courseSchema);