const fs = require('fs');

// Check courses in course.json
const rawText = fs.readFileSync('./db-setup/course.json', 'utf-8');
const courses = JSON.parse(rawText);

const courseCount = courses.length;

// Check number of entries in txt.txt
const txt = fs.readFileSync('./Webscraper 1.0/txt.txt', 'utf-8');
const lines = txt.split('\n');
let count = 0;

for (const line of lines) {
  if (line.trim().startsWith('---')) {
    count++;
  }
}
count++; // account for first course not having a --- line before it


test('Total number of courses parsed correctly', () => {
  expect(courseCount).toBe(count)
});