const fs = require('fs');
const path = require('path');

const filePath = '../Webscraper 1.0/txt.txt';
const rawText = fs.readFileSync(path.resolve(__dirname, filePath));
const blocks = rawText.trim().split('\n\n');

const courses = blocks.map(block => {
  const lines = block.split('\n');

  const [title, code] = lines[0].split(' - ');
  const description = lines[1];
  const prereqLine = lines[2];
  const hoursLine = lines[3];

  const prerequisites = prereqLine.replace('Prerequisite(s):', '').trim();
  const hours = hoursLine.replace('Hour(s):', '').trim();

  return {
    code: code.trim(),
    title: title.trim(),
    desciption: description.trim(), // matches your schema spelling
    prerequisites: prereqLine.trim(),
    hours: hoursLine.trim(),
    comments: []
  };
});

fs.writeFileSync('course.json', JSON.stringify(courses, null, 2));
console.log('Course data has been written to course.json');
