const mongoose = require('mongoose');
const { Course } = require('./schema/course.js');
const readline = require('readline');
const path = require('path');

const dotenv = require('dotenv');
dotenv.config({ path: path.resolve(__dirname, '../.env') });
const MONGO_URI = process.env.MONGO_URI;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function clearDB() {
  rl.question("We are clearing the DB for each new build for the beta, type 'beta' to continue or anything else to abort clear: ", async (query) => {
    if (query !== 'beta') {
      console.log("Aborting DB clear");
      rl.close();
      process.exit(1);
    }

    try {
      await mongoose.connect(MONGO_URI);
      console.log("Connected to MongoDB");

      const result = await Course.deleteMany({});
      console.log(`Deleted ${result.deletedCount} courses from the database.`);

      await mongoose.disconnect();
      console.log("Disconnected from MongoDB");
    } catch (err) {
      console.error("Error clearing DB:", err);
    } finally {
      rl.close();
    }
  });
}

clearDB();
