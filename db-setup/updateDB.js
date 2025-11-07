/**
 * File meant to a json file containing course objects (as seen in schema/Course.js) and update the MongoDB database with any new courses not already present.
 *
 * Usage:
 *   Run this script in a Node.js environment after the webscraper has generated `txt.txt`.
 */


const {Course} = require('./schema/Course');
const fs = require('fs');
const path = require('path');
const mongoose = require('mongoose');

//import mongoURI from .env
const dotenv = require('dotenv');
dotenv.config({ path: path.resolve(__dirname, '../.env') });
const MONGO_URI = process.env.MONGO_URI;

const filePath = path.resolve("./courses.json");
const rawText = fs.readFileSync(filePath, 'utf-8');
const courseList = JSON.parse(rawText);

async function updateDB() {
    try {
        await mongoose.connect(MONGO_URI);
        console.log("Connected to MongoDB");

        let inserted = 0;
        let cur;

        for (cur of courseList) {
            //first check if a course already exists
            const existingCourse = await Course.findOne({code: cur.code});

            if (existingCourse) {
                console.log(`Course ${cur.code} already found in db, skipping to next`);
                continue;
            }

            //create new course
            const curCourse = new Course({
                ...cur,
                comments: []
            });
            await curCourse.save();
            inserted++;

        }
        
        console.log(`DB update complete. ${inserted} new courses added.`);
        await mongoose.disconnect();
    } catch (error) {
        console.error("Error updating DB:", error);
    }
}
updateDB();
    