/* schedule.js
* This file will run primarily as part of the builder.py script 
* It will read from any xlsx files in ./xlsx/*.xlsx and update the courses.json
*
* xlsx reading guided by microsoft copilot
*/

//translate terms
function toTerm(date){ 
    var output;
    if (date == "202501") {
        output = "Winter 2025"
    } else if (date == "202401") {
        output = "Winter 2024";
    } else if (date == "202502") {
        output = "Spring 2025";
    } else if (date == "202402") {
        output = "Spring 2024";
    } else if (date == "202504") {
        output = "Fall 2025";
    } else if (date == "202404") {
        output = "Fall 2025";
    }
    return output;
}

// readCourses.js
const fs = require('fs');
const xlsx = require("xlsx");
const path = require("path");

// find xlsx files and read all
const xlsxFolder = "./db-setup/xlsx";
const files = fs.readdirSync(xlsxFolder).filter(f => f.endsWith(".xlsx"));

//Load course.json
const coursesPath = "./db-setup/courses.json";
const courseData = JSON.parse(fs.readFileSync(coursesPath, "utf-8"));

for (const file of files) {
    const filePath = path.join(xlsxFolder, file);

    const workbook = xlsx.readFile(filePath);
    const sheetName = workbook.SheetNames[0];
    const sheet = workbook.Sheets[sheetName];
    const rows = xlsx.utils.sheet_to_json(sheet);


    for (const row of rows) {
        const code = row.Course;
        const term = row.Term;
        const name = row.Firstname + " " + row.Lastname;

        const course = courseData.find( c => c.code === code);

        if (!course) {
            console.warn(`${code} not found in courses.json`);
            continue; 
        };
        let instructor = course.instructors.find(i => i.name === name);

        if (!instructor) {
            instructor = { name: name.trim(), terms: [] };
            course.instructors.push(instructor);
        }
        const termWords = toTerm(term);
        if (!instructor.terms.includes(termWords)) {
            instructor.terms.push(termWords);
        }

    }  
}
fs.writeFileSync(coursesPath, JSON.stringify(courseData, null, 2));

console.log("✅ courses.json updated with instructor sessions");

// console.log(rows);


