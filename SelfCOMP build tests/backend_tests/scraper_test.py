import pytest
import os
import sys
from unittest.mock import patch, Mock
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SCRAPER_DIR = os.path.join(BASE_DIR, "../../scraper")
sys.path.append(SCRAPER_DIR)

import webscraper

# This is just a basic web scraper dependency test, sees if it can actually run and scrape a hypothetical html file. If it fails, dependencies are missing!
def test_scrape_function_extracts_titles():
    html_content = """
    <html>
        <body>
            <h2 class="title">First Title</h2>
            <h2 class="title">Second Title</h2>
        </body>
    </html>
    """

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = html_content

    with patch("requests.get", return_value=mock_response):
        result = webscraper.scrape_function("http://example.com")
        assert result == ["First Title", "Second Title"]