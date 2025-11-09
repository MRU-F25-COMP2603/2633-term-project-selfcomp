/**
 * File meant to take the output from the webscraper and parse it into a JSON
 * 
 * Output:
 *   - A JSON file named `courses.json` containing an array of course objects.
 *   - Console logs indicating progress and number of courses processed.
 *
 * Usage:
 *   This script is run as part of upDateDB.js.
 */

const fs = require('fs');
const path = require('path');
const filePath = '../Webscraper 1.0/txt.txt';
const rawText = fs.readFileSync(path.resolve(__dirname, filePath), 'utf-8');
const outputPath = './courses.json';

const blocks = rawText.trim().split(/^-{3,}$/m); // split on dashed lines
count = 0;

const courses = blocks.map(block => {
  const lines = block
    .split('\n')
    .map(line => line.trim())
    .filter(line => line.length > 0);

  var prereqLine, hoursLine, description, title, code;

  //skip final block
   if (lines.length === 0) {
    return null;
   }
  if (lines.length < 4) {
    [code, title] = lines[0].split(' - ');
    description = lines[1];
    prereqLine = "no prerequisite";
    hoursLine = lines[2];
  } else {
    [code, title] = lines[0].split(' - ');
    description = lines[1];
    prereqLine = lines[2];
    hoursLine = lines[3];
  }

  count++;
  return {
    code: code.trim(),
    title: title.trim(),
    desciption: description.trim(),
    prerequisites: prereqLine.trim(),
    Hours: hoursLine.trim(),
    comments: []
  };
}).filter(Boolean);

//check for old courses.json and delete
if (fs.existsSync(outputPath)) {
  fs.unlinkSync(outputPath, (err) => {
    if (err) {
      console.error('Error deleting old courses.json:', err);
      return;
    };
    console.log('Old courses.json deleted successfully');
  });
};

//write new courses.json
fs.writeFileSync(outputPath, JSON.stringify(courses, null, 2));
console.log(`${count} courses' data has been written to course.json`);

