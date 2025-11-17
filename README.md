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


## Releases

[Beta Release](https://github.com/MRU-F25-COMP2603/2633-term-project-selfcomp/releases/tag/beta-release) - 11/16/25

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

## User Guide
A user guide detailing use cases, building/installing the system and bugs can be found [here](https://docs.google.com/document/d/1ZUxEfDBjf170Lx-l5YD-ClSKfzw7ZeP7q8oQVgStXmw/edit?tab=t.0)

## Developer Guide
A developer guide deatiling developer tools, directory layout and making tests/release can be found [here](https://docs.google.com/document/d/1Jw3TtNEqlt9BFf0zdAct5kiCbT-Wn5PSbdegKB5hXlo/edit?tab=t.0#heading=h.hex88dxhuw91)

## Building and hosting an instance of SelfCOMP
These steps have been moved to and are detailed in the user guide

## Operational Use Cases and Features
As of the beta release our use case 1a from the living document is functional. This has an actor entering the course catalogue and viewing the details for all courses from a list actively updated by the DB.

Our working Features:
- Webscraper scraping from MRU site
- Updating DB based on output from scraper
- Viewable, updated course page

## start of semester commit check
<details>
<Summary> Commit Check </summary>

Section to sign off and make sure everyone can commit to main.

Done:<br>
Matthew Kim<br>
Yacob Mesfun<br>
Ujjwal Bhandari<br>
Lorenzo Primiterra
</details>
