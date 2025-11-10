# SelfComp

SelfComp is a website meant to house course outlines for, and information/advice from alumni for Mount Royal University's COMP courses.

## Contributors
<!-- Can add link to all your guys' githubs as well is u want to add -->
- [Ujjwal Bhandari](https://github.com/Ujjwalb101)
- [Matthew Kim](https://github.com/EassunKim)
- [Yacob Mesfun](https://github.com/Ymesfun) 
- [Lorenzo Primiterra]

## Other Rescources

Aside from this repo we will also be sharing files using [Google Drive](https://drive.google.com/drive/folders/1nUbFmQfhxza2xoQnU6ltNtXfH2xv4htr?usp=sharing) and [Discord](https://discord.gg/7ah7GDtwgA)

## Testing and CI
SelfCOMP uses three testing frameworks: Jest, Pytest, and Beautiful Soup in order to test the database, webscraper and frontend repspectively

This project utilized GitHub Actions to run tests for any push. We arrived in GitHub actions due to its ease of use 

Our CI workflow is detailed in the yml files in ./.github/workflows
<details>
<summary>Running Tests</summary>

<p>The test suites can also be run manually by running the following commands:</p>

- npm install
- pip install -r "requirements.txt"
- npm test
- pytest
</details>

## Building and hosting an instance of SelfCOMP
<details>
<summary> 1. initial requirements </summary>
installations of:

- Visual studio build tools 2022
- Python (3.12.10 used for development)
- Node.js (v22.15.0 used for development)
</details>

<details>
<summary> 2. setup MongoDB </summary>

1. got to [MongoDB](https://www.mongodb.com/), create account, create a cluster called 'courses' in your desired project and setup DB user
2. Under 'connect' tab find MongoDB URI connected to your db user
3. Save this for later
</details>

<details>
<summary> 3. setting up repo </summary>

1. Run ``` git clone ``` on this repo
2. In the root of the git folder create a ``` .env ``` file and inside of it make sure the following line is included:
``` MONGO_URI=mongodb+srv://<MONGO_USERNAME>:<MONGO_PASSWORD>@courses.hoehaew.mongodb.net/?appName=courses ```
with your MongoURI from step 2
</details>

<details>
<summary> 4. building the system and DB </summary>

Building the system can be done by running ``` python builder.py ``` from a terminal in the root directory

Steps performed in a build:

- install dependencies
- run webscraper
- parse scraper output and updateDB based on that
- site can then be hosted/deployed using flask

NOTE:
-  DB update does not currently update all fields for the beta release. The builder still functions but it does so by clearing the DB and updating from the new parser output
- Scraper only functions on given MRU page, so hosting an instance of SelfCOMP for another school isnt currently possivlegi
</details>

<details>
<summary> 5. hosting the system (local) </summary>

NOTE: as of the beta release SelfCOMP is not hosted on a server but it can be hosted locally on your system

run ``` flask run ```

app is now running at https://ip.from.flask (link given from flask run return)
</details>

## Operatoinal Use Cases and Features
As of the beta release our use case 1a from the living document is functional. This has an actor entering the course catalogue and viewing the details for all courses from a list actively updated by the DB.

Our working Features:
- Webscraper scraping from MRU site
- Updating DB based on output from scraper
- Viewable, updated course page

### start of semester commit check
<details>
<Summary> Commit Check </summary>

Section to sign off and make sure everyone can commit to main.

Done:<br>
Matthew Kim<br>
Yacob Mesfun<br>
Ujjwal Bhandari<br>
Lorenzo Primiterra
</details>
