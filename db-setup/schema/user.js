import mongoose from "mongoose";

const courseSchema = new mongoose.Schema({
    name: {type: String, required: true},
    password: {type: String, required: true},
    SID: {type: int, required: true},
    // permissions: 0 = student, 1 = professor
    permission: {type: int, required: true} 
});

export const Course = mongoose.model("Course", courseSchema);