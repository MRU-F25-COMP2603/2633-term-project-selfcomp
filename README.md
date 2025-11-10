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

## Building the System
Building the system can be done by running ``` python builder.py ``` from a terminal in the root directory

<details>
<summary>Steps performed in a build</summary>

- install dependencies
- run webscraper
- parse scraper output and updateDB based on that
- site can then be hosted/deployed using flask

NOTE: DB update does not currently update all fields for the beta release. The builder still functions but it does so by clearing the DB and updating from the new parser output
</details>

## Running SelfCOMP
SelfCOMP can be locally hosted through flask. After running the builder (desribed in "Building the System") you can run ``` flask run ``` in a terminal from the root folder and following any on screen prompts

## Operatoinal Use Cases and Features
As of the beta release our use case 1a from the living document is functional. This has an actor entering the course catalogue and viewing the details for all courses from a list actively updated by the DB.

Our working Features:
- Webscraper scraping from MRU site
- Updating DB based on output from scraper
- Viewable, updated course page

<details>
<Summary> Commit Check </summary>

Section to sign off and make sure everyone can commit to main.

Done:<br>
Matthew Kim<br>
Yacob Mesfun<br>
Ujjwal Bhandari<br>
Lorenzo Primiterra
</details>
