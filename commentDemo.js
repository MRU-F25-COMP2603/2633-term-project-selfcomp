/**
 * Script to run addComment.js from command line inputs for the beta demonsatration.
 * Usage: node commentDemo.js -> follow prompts
 * Depends on: db-setup/update/addComment.js
 */
const addComment = require('./db-setup/update/addComment').addComment;
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question("Enter Course Code (ex. COMP1701): ", (courseCode) => {
    rl.question("what is your name?: ", (author) => {
        rl.question("Enter your comment: ", (text) => {
            addComment(courseCode, author, text).then(() => {
                rl.close();
            });
        });
    });
});