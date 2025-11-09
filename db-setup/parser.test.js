const fs = require('fs');
const scraperOutput = './webscraper/txt.txt';
const parserOutput = './db-setup/courses.json';


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


test('Total number of courses parsed correctly', () => {
  expect(courseCount).toBe(count)
});