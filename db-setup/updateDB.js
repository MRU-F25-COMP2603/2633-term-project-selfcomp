require('dotenv').config();
const Course = require('../models/Course');

const MONGO_URI = process.env.MONGO_URI

const courseList = //call parser

async function updateDB() {
    try {
        await mongoose.connect(MONGO_URI, {newUrlParser: true, useUnifiedTopology: true});
        console.log("Connected to MongoDB");

        for (const courseData of courseList) {
            //first check if a course already exists
            const existingCourse = await Course.findOne({code: courseData.code});

            if (existingCourse) {
                console.log(`Course ${courseData.code} already found in db, skipping to next`);
                continue;
            }

            //create new course
            const curCourse = new Course({
                ...courseData,
                comments: []
            });
            await curCourse.save();
        }
        
        console.log("DB updated successfully");
        mongoose.disconnect();
    } catch (error) {
        console.error("Error updating DB:", error);
    }
}
updateDB();
    