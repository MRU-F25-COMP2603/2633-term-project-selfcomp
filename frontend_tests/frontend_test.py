from bs4 import BeautifulSoup
from pathlib import Path
# This tests if our frontend is scrapable, AKA if it is a valid well structured html file.
def test_homepage_structure():
    """
    Basic frontend test:
    - HTML file exists
    - Has <title> tag
    - Links correct CSS file
    - Navigation items match expected list
    """

    #Point to file
    path = Path("templates/homepage.html")  
    assert path.exists(), "homepage.html file not found in scripts/"

    #parse HTML
    html = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    #Basic checks
    assert soup.title and soup.title.string.strip(), "Missing or empty <title> tag"

    link = soup.find("link", rel="stylesheet")
    assert link and "styles.css" in link.get("href", ""), "Missing or incorrect stylesheet link"

    nav_items = [a.get_text(strip=True) for a in soup.select("nav ul li a")]
    assert nav_items == ["Home", "Upload", "Courses"], f"Unexpected nav items: {nav_items}"