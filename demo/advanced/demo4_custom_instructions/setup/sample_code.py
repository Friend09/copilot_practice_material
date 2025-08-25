"""
Demo 4: Custom Instructions - Sample Domain Code
===============================================

This code demonstrates web scraping domain patterns that will be
enhanced when custom instructions are applied.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import requests
import time


@dataclass
class TicketInfo:
    """Basic ticket information - will be enhanced with custom instructions"""
    event_name: str
    venue: str
    price: float
    url: str


class BasicScraper:
    """
    Basic scraper that will be enhanced when custom instructions are applied.
    This shows the 'before' state - Copilot will improve this significantly.
    """

    def __init__(self):
        self.session = requests.Session()

    def fetch_page(self, url: str):
        """Basic fetch - will be enhanced with rate limiting, error handling"""
        response = self.session.get(url)
        return response.text

    def extract_tickets(self, html: str):
        """Basic extraction - will be enhanced with proper parsing"""
        # Simple placeholder - custom instructions will improve this
        return []


if __name__ == "__main__":
    print("🎫 Basic ticket scraper ready for custom instructions demo!")
    print("📝 Apply web scraping custom instructions to see improvements:")
    print("   - Rate limiting and retry mechanisms")
    print("   - Proper error handling and logging")
    print("   - Data validation with Pydantic models")
    print("   - Ethical scraping practices")
    print("\n🚀 Ask Copilot to enhance this code following custom instructions!")
