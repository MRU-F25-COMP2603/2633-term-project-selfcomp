const {Course} = require('../schema/Course');
const fs = require('fs');
const path = require('path');
const mongoose = require('mongoose');

const dotenv = require('dotenv');
dotenv.config({ path: path.resolve(__dirname, '../../.env') });
const MONGO_URI = process.env.MONGO_URI;

async function addComment(courseCode, author, text) {
    try {
        await mongoose.connect(process.env.MONGO_URI);

        const cur = await Course.findOne({code: courseCode});
        if (!cur) {
            console.log(`Course with code ${courseCode} not found.`);
            return;
        }
        cur.comments.push({author, text});
        await cur.save();
        console.log("Comment successfully added.");
        await mongoose.disconnect();
    } catch (error) {
        console.error("Error adding comment:", error);
    }   

}

module.exports = { addComment };