const fs = require('fs');
const scraperOutput = './Webscraper/txt.txt';
const parserOutput = './db-setup/courses.json';
const dotenv = require('dotenv');
const mongoose = require('mongoose');
const {Course} = require('./schema/Course');

dotenv.config();
const MONGO_URI = process.env.MONGO_URI;

// Parser tests
describe('parser test', () => {
  test('Total number of courses parsed correctly', () => {
      // Check courses in course.json
      const rawText = fs.readFileSync(parserOutput, 'utf-8');
      const courses = JSON.parse(rawText);
      const courseCount = courses.length;

      // Check number of entries in txt.txt
      const txt = fs.readFileSync(scraperOutput, 'utf-8');
      const lines = txt.split('\n');
      let count = 0;

      for (const line of lines) {
        if (line.trim().startsWith('---')) {
          count++;
        }
      }
    expect(courseCount).toBe(count)
  })
});

// Database tests
describe('updateDB test', () => {
  beforeAll(async () => {
    await mongoose.connect(MONGO_URI);
  });

  afterAll(async () => {
    await mongoose.disconnect();
  });

  test('Course codes have been added to the database correctly', async () => {
    const courses = await Course.find({});
    const regex =  /^[A-Z]{4}\d{4}$/; //regex for course code format given by copilot

    courses.forEach(course => {
      expect(regex.test(course.code)).toBe(true);
    });
  });

  test('test for no null fields in db', async () => {
    const allCourses = await Course.find({})
    
    allCourses.forEach(course => {
      expect(course.code).not.toBeNull();
      expect(course.name).not.toBeNull();
      expect(course.description).not.toBeNull();
      expect(course.hours).not.toBeNull();
      expect(course.comments).not.toBeNull();
    });
  });
});