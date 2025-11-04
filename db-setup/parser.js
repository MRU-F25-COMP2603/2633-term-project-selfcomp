const fs = require('fs');
const path = require('path');

const filePath = '../Webscraper 1.0/txt.txt';
const rawText = fs.readFileSync(path.resolve(__dirname, filePath), 'utf-8'); // ✅ fix here

const blocks = rawText.trim().split(/^-{3,}$/m); // split on dashed lines
count = 0;

const courses = blocks.map(block => {
  const lines = block
    .split('\n')
    .map(line => line.trim())
    .filter(line => line.length > 0);

  if (lines.length < 4) return null;

  const [title, code] = lines[0].split(' - ');
  const description = lines[1];
  const prereqLine = lines[2];
  const hoursLine = lines[3];

  count++;
  return {
    code: code.trim(),
    title: title.trim(),
    desciption: description.trim(),
    prerequisites: prereqLine.replace('Prerequisite(s):', '').trim(),
    hours: hoursLine.replace('Hour(s):', '').trim(),
    comments: []
  };
}).filter(Boolean);

fs.writeFileSync('course.json', JSON.stringify(courses, null, 2));
console.log(`${count} courses' data has been written to course.json`);

