#*******************************************************************************
 #AUTHORS: Lorenzo Primiterra
 #COURSE: COMP3533-001
 #DATE: October 30, 2025

 #FILE: webscraper.py
 #SUMMARY: Handles the logic for scraping the Mount Royal Course website and outputting it as a .txt
# Due to issues regarding the website having embedded Javascript within the HTML tags a few approaches were tried:
# - A pure HTML scrape was done with success for the course name; however, the description and additional content remained unscraped. 
# - Attempting to Scrape each page for each repective course while trying to convert it to pure HTML also yielded little success.
# - A full implmentation of a Javascript library to help scrape the reamining information that is embedded which required Browser respective drivers. 
#        While having more success then before, it also didnt correctly scrape and due to constant chrome updates would quickly become obsolete.
#        This version also included a comparsion to strict array defining each descriptions to only update if the information differed.
# - A final version just scrapes web names but uses hardcoded course information due to numerious formatting issues and bugs. 

#*******************************************************************************/

#*******************************************************************************
    #PURPOSE: A class dedicated to scraping the MRU course website via BeautifulSoup & requests libraries,
    #INPUT:   - N/A besides initalizer
    #OUTPUT:  a txt.txt file with the scraped and formatted conent to which will then be handled within the Database. 
#*******************************************************************************/




from bs4 import BeautifulSoup
import requests

class CScourse:
    def __init__(self, course_name):
        self.course_name = course_name

comp_1701 = ["Introduction to object-oriented analysis and design, programming using an object-oriented language, and implementation of linked data structures. Issues of modularity, software design, and programming style will be emphasized."
"Prerequisite(s): COMP 1631 with a minimum grade of C- or higher.",
"Lecture Hour(s): 3"
]

comp_1631 = [
    "Introduction to problem-solving and programming using a procedural programming language. Topics include data representation, program control, basic file handling, and the use of simple data structures.",
    "Note: Credit may not be obtained for both COMP 1501 and COMP 1631.",
    "Lecture Hour(s): 3"
]

comp_1633 = [
    "Introduction to object-oriented analysis and design, programming using an object-oriented language, and implementation of linked data structures. Issues of modularity, software design, and programming style will be emphasized.",
    "Prerequisite(s): COMP 1631 with a minimum grade of C- or higher.",
    "Lecture Hour(s): 3"
]

comp_2613 = [
    "Provides insight into the theoretical foundations of computing science. Topics include abstract machines (finite automata, push down automata, Turing machines), formal language hierarchy, and applications.",
    "Prerequisite(s): MATH 1271 and COMP 1633 with minimum grades of C- or higher.",
    "Lecture Hour(s): 3"
]

comp_2631 = [
    "Study of data structures including trees, graphs, and hash tables. Emphasis on searching, sorting, and algorithm efficiency.",
    "Prerequisite(s): COMP 1633 with a minimum grade of C- or higher.",
    "Lecture Hour(s): 3"
]

comp_2633 = [
    "Introduction to software development problems and processes. Covers software life cycles, process improvement, requirements analysis, design, implementation, integration, and testing.",
    "Prerequisite(s): COMP 2631 with a minimum grade of C- or higher.",
    "Lecture Hour(s): 3"
]

comp_2655 = [
    "Detailed study of CPU architecture and internal data representations. Introduction to assembly language programming and implementation of control structures and data structures.",
    "Prerequisite(s): COMP 1633 with a minimum grade of C- or higher.",
    "Lecture Hour(s): 3"
]

comp_2659 = [
    "Covers CPU organization, memory, I/O interfaces, devices, and busses. Includes digital logic design, hardware interfacing, asynchronous I/O, and interrupt processing.",
    "Prerequisite(s): PHIL 1179 and COMP 2655 with minimum grades of C- or higher.",
    "Lecture Hour(s): 3"
]

comp_3309 = [
    "Explores the implications of information technology for society including historical, legal, ethical, economic, and philosophical perspectives.",
    "Prerequisite(s): GNED 1301, GNED 1303, or GNED 1304.",
    "Lecture Hour(s): 3"
]

comp_3614 = [
    "Design and analysis of algorithms. Covers greedy algorithms, divide-and-conquer, recursive backtracking, dynamic programming, heuristics, and NP-completeness.",
    "Prerequisite(s): COMP 2631, COMP 2613 and MATH 1200 with minimum grades of C-.",
    "Lecture Hour(s): 3"
]

comp_3649 = [
    "Examines major programming paradigms with emphasis on declarative paradigms like functional and logic programming. Topics include data types, control expressions, lazy evaluation, and information hiding.",
    "Prerequisite(s): COMP 2613, COMP 2631 and PHIL 1179 with minimum grades of C- or higher.",
    "Lecture Hour(s): 3"
]

comp_3659 = [
    "Introduces principles and techniques for designing and implementing operating systems. Topics include performance, concurrency, file and process management, security, memory, and processor resources.",
    "Prerequisite(s): COMP 2631 and COMP 2659 with minimum grades of C-.",
    "Lecture Hour(s): 3"
]

math_1200 = [
    "Introduction to calculus with applications in science, business, and economics. Covers limits, derivatives, integrals, and techniques of integration.",
    "Prerequisite(s): 60% or higher in Mathematics 30-1 or MATH 0130, or C- or higher in MATH 1283, MATH 1285, or equivalent.",
    "Lecture Hour(s): 4"
]

math_1203 = [
    "Introduction to linear algebra for science students. Topics include vector and matrix algebra, systems of linear equations, determinants, linear transformations, polar coordinates, complex numbers, and applications using eigenvalues and eigenvectors.",
    "Prerequisite(s): Mathematics 30-1 with a 60% or higher.",
    "Lecture Hour(s): 3"
]

math_1271 = [
    "Introduction to symbolic logic, techniques of proof, sets, equivalence relations, mathematical induction, recursion, counting principles, graphs, and trees.",
    "Prerequisite(s): MATH 1203 with a grade of C- or higher.",
    "Lecture Hour(s): 3"
]

math_2234 = [
    "Covers descriptive statistics, probability theory, and inferential statistics. Topics include population means and proportions, regression, correlation, chi-square tests, and ANOVA. Labs use statistical software to apply concepts to real data.",
    "Prerequisite(s): MATH 1200 with a grade of C- or higher.",
    "Lecture Hour(s): 4"
]

phil_1179 = [
    "Introduces sentential and first-order logic from deductive and semantic perspectives. Includes discussion of elementary metatheorems.",
    "Prerequisite(s): None listed.",
    "Lecture Hour(s): 3"
]

comp_3533 = [
    "This course covers the principles and practice of computer networking, focusing on the high-level protocol-oriented aspects of computer networks. Networking as it relates to database and file service applications is examined along with Internet structure, protocols and routing. Various aspects of security in networked information systems are studied.",
    "Prerequisite(s): COMP 3532 with a minimum grade of C-.",
    "Lecture Hour(s): 3"
]

comp_3553 = [
    "This course covers the fundamental theory and practice in the design and evaluation of human-computer interfaces. The impacts of computer-based information systems on individuals and organizations are examined along with the rationale for a user-centric approach in all IT applications and systems.",
    "Prerequisite(s): COMP 2511 and COMP 2503 with a minimum grade of C-.",
    "Lecture Hour(s): 3"
]

comp_3612 = [
    "This course provides an overview of web development suitable for computer science majors. It covers the broad spectrum of technologies used within this environment. Design, tools, and development processes unique to web development will also be covered.",
    "Prerequisite(s): COMP 2633 with a minimum grade of C-.",
     "Lecture Hour(s): 3"
]

math_3625 = [
    "This course provides an introduction to artificial intelligence concepts and techniques. Topics include the characteristics of problems for which intelligent systems can be built, the agent paradigm, search strategies, knowledge representation, logical reasoning, reasoning under uncertainty, and machine learning. Multi-agent systems, robotics, computer vision, and/or natural language processing will be introduced, as time permits.",
    "Prerequisite(s): A minimum grade of “C-” in all of COMP 2631, COMP 2613 and MATH 2234.",
    "Lecture Hour(s): 3"
]

math_3626 = [
    "This course provides a broad understanding of the issues in developing and analyzing evolutionary and swarm computation systems. Topics that may be covered are genetic algorithms, evolution strategies, evolution programming, genetic programming, classifier systems, swarm optimization, constraint handling, dynamic environments, co-evolutionary systems, cellular automata, and neural networks.",
    "Prerequisite(s): COMP 2631 with a minimum grade of C-.",
    "Lecture Hour(s): 3"
]

course_info_array = [
    comp_1633,
    comp_1701,
    comp_2613,
    comp_2631,
    comp_2633,
    comp_2655,
    comp_2659,
    comp_3309,
    comp_3614,
    comp_3649,
    comp_3659,
    math_1200,
    math_1203,
    math_1271,
    math_2234,
    phil_1179,
    comp_3533, 
    comp_3553, 
    comp_3612, 
    math_3625, 
    math_3626,
    
]    




   

url = "https://catalog.mtroyal.ca/preview_program.php?catoid=31&poid=5723&print"
result = requests.get(url)
soup = BeautifulSoup(result.text, "lxml")

course_blocks = soup.find_all("li", class_="acalog-course")
courses = []

for block in course_blocks:
    # Course name
    name_tag = block.find("a")
    course_name = name_tag.get_text(strip=True).replace('\xa0', ' ') if name_tag else "Unknown"

   
    # Create course object
    course = CScourse(course_name)
    courses.append(course)                              

   

with open("txt.txt", "w") as f:
    for i in range(min(len(courses), len(course_info_array))):
        f.write(f"{courses[i].course_name}\n")
        for line in course_info_array[i]:
            f.write(line + "\n")
        f.write("\n" + "-" * 40 + "\n")

