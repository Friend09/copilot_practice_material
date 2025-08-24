# GitHub Copilot Advanced Demo 4: Function Calling & Custom Instructions

## Overview

This demo showcases GitHub Copilot's advanced capabilities:

- **Function calling with precise context determination**
- **Custom instructions for team-specific coding standards**
- **Intelligent tool selection and usage**
- **Domain-specific code generation patterns**
- **Enterprise-grade customization and governance**

## Demo Scenario

**Web Scraping Ticketing Tool** - Demonstrate custom instructions for web scraping best practices, function calling for data extraction and processing, and team-specific architectural patterns for scalable ticket monitoring systems.

🎯 **This demo shows how to customize Copilot for enterprise needs!**

---

## Custom Instructions Examples

### Web Scraping Domain Custom Instructions

```text
# GitHub Copilot Custom Instructions: Web Scraping Ticketing Tool

## Code Style Guidelines:
1. Use type hints for all function parameters and return values
2. Include docstrings with parameter descriptions and examples
3. Use dataclasses for structured data models
4. Include comprehensive logging for all scraping operations
5. Add rate limiting and retry mechanisms for all web requests
6. Follow the Repository pattern for data persistence
7. Use Pydantic models for data validation
8. Include robust error handling with custom exceptions

## Web Scraping Best Practices:
1. Always respect robots.txt and rate limits
2. Use random delays between requests to avoid detection
3. Implement proper session management and cookie handling
4. Include User-Agent rotation for different requests
5. Add proxy support for large-scale operations
6. Use headless browsers for JavaScript-heavy sites
7. Implement data validation and sanitization
8. Cache responses to minimize redundant requests

## Architecture Patterns:
1. Separate scraping logic from data processing
2. Use dependency injection for external services
3. Implement the Strategy pattern for different ticket sites
4. Use Observer pattern for real-time notifications
5. Include circuit breakers for unreliable websites
6. Use queue systems for batch processing

Ask Copilot to follow these instructions when generating code!
```

---

## Foundation Code Examples

### Value Objects with Web Scraping Domain Rules

```python
from typing import Dict, List, Optional, Any, Callable, Union
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from decimal import Decimal
import json
import logging
from abc import ABC, abstractmethod
from urllib.parse import urljoin, urlparse
import requests
from pydantic import BaseModel, validator
import time
import random

@dataclass(frozen=True)
class TicketInfo:
    """
    Value object for ticket information - demonstrates custom instruction
    for structured data modeling with validation
    """
    event_name: str
    venue: str
    date: datetime
    price: Optional[Decimal] = None
    currency: str = "USD"
    availability: str = "UNKNOWN"  # AVAILABLE, SOLD_OUT, LIMITED, UNKNOWN
    section: Optional[str] = None
    row: Optional[str] = None
    seat_numbers: Optional[List[str]] = None
    url: Optional[str] = None

    def __post_init__(self):
        if self.availability not in ['AVAILABLE', 'SOLD_OUT', 'LIMITED', 'UNKNOWN']:
            raise ValueError("Invalid availability status")
        if self.price and not isinstance(self.price, Decimal):
            raise ValueError("Price must be Decimal type for accuracy")

@dataclass
class ScrapingTarget:
    """
    Scraping target entity following custom instructions for web scraping domain modeling
    """
    url: str
    site_name: str
    selectors: Dict[str, str]  # CSS selectors for different data fields
    rate_limit: float = 1.0  # seconds between requests
    requires_js: bool = False
    headers: Dict[str, str] = field(default_factory=dict)
    cookies: Dict[str, str] = field(default_factory=dict)

    def __post_init__(self):
        # Validation following custom instructions
        if not self.url.startswith(('http://', 'https://')):
            raise ValueError("URL must start with http:// or https://")
        if self.rate_limit < 0.1:
            raise ValueError("Rate limit must be at least 0.1 seconds")

class ScrapingException(Exception):
    """Custom exception following team guidelines"""
    pass

class RateLimitExceededException(ScrapingException):
    """Raised when rate limiting is triggered"""
    pass

class SiteBlockedException(ScrapingException):
    """Raised when the scraping target blocks requests"""
    pass
```

### Function Calling Demonstration Classes

```python
class WebScrapingService:
    """
    Service that demonstrates function calling capabilities
    Copilot will understand when to call these methods based on context
    """

    def __init__(self):
        self.session = requests.Session()
        self.last_request_time = {}

    def fetch_page(self, url: str, headers: Optional[Dict[str, str]] = None,
                   rate_limit: float = 1.0) -> str:
        """
        Fetch a web page with rate limiting and error handling

        Args:
            url: URL to fetch
            headers: Optional HTTP headers
            rate_limit: Minimum seconds between requests to this domain

        Returns:
            Page content as string

        Example:
            >>> service = WebScrapingService()
            >>> content = service.fetch_page('https://example.com/tickets')
            >>> print(f"Page length: {len(content)}")
        """
        domain = urlparse(url).netloc

        # Rate limiting following custom instructions
        if domain in self.last_request_time:
            time_since_last = time.time() - self.last_request_time[domain]
            if time_since_last < rate_limit:
                delay = rate_limit - time_since_last + random.uniform(0.1, 0.5)
                logging.info(f"Rate limiting: waiting {delay:.2f} seconds")
                time.sleep(delay)

        self.last_request_time[domain] = time.time()

        # Copilot will understand this needs proper error handling
        logging.info(f"Fetching page: {url}")
        try:
            response = self.session.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logging.error(f"Failed to fetch {url}: {e}")
            raise ScrapingException(f"Failed to fetch page: {e}")

    def extract_ticket_data(self, html_content: str, selectors: Dict[str, str]) -> List[TicketInfo]:
        """
        Extract ticket information from HTML content

        Args:
            html_content: Raw HTML content
            selectors: CSS selectors for different data fields

        Returns:
            List of extracted ticket information
        """
        logging.info("Extracting ticket data from HTML content")
        # Copilot will implement based on BeautifulSoup or similar
        pass

    def monitor_ticket_availability(self, targets: List[ScrapingTarget],
                                  callback: Callable[[TicketInfo], None]) -> None:
        """
        Monitor multiple ticket sites for availability changes

        Args:
            targets: List of scraping targets to monitor
            callback: Function to call when tickets become available
        """
        logging.info(f"Starting monitoring for {len(targets)} targets")
        # Copilot will implement continuous monitoring with appropriate delays
        pass

class DataProcessingService:
    """
    Demonstrates function calling for data processing and analysis
    """

    def clean_and_validate_tickets(self, raw_tickets: List[Dict[str, Any]]) -> List[TicketInfo]:
        """
        Clean and validate raw ticket data

        Args:
            raw_tickets: Raw ticket data from scraping

        Returns:
            Validated and cleaned TicketInfo objects
        """
        logging.info(f"Processing {len(raw_tickets)} raw ticket records")
        # Copilot will implement data cleaning and validation logic
        pass

    def detect_price_changes(self, current_tickets: List[TicketInfo],
                           historical_data: List[TicketInfo]) -> List[Dict[str, Any]]:
        """
        Detect price changes between current and historical data

        Args:
            current_tickets: Current ticket data
            historical_data: Historical ticket data for comparison

        Returns:
            List of price change events
        """
        logging.info("Analyzing price changes")
        # Copilot will implement price comparison algorithms
        pass

    def generate_availability_report(self, tickets: List[TicketInfo],
                                   time_range: timedelta = timedelta(days=7)) -> Dict[str, Any]:
        """
        Generate availability report for tickets

        Args:
            tickets: Ticket data to analyze
            time_range: Time range for the report

        Returns:
            Comprehensive availability analysis report
        """
        logging.info(f"Generating availability report for {len(tickets)} tickets")
        # Copilot will implement reporting and analytics
        pass

class NotificationService:
    """
    Demonstrates function calling for user notifications
    """

    def send_ticket_alert(self, ticket: TicketInfo, user_preferences: Dict[str, Any]) -> bool:
        """
        Send notification when desired tickets become available

        Args:
            ticket: Ticket information
            user_preferences: User notification preferences

        Returns:
            True if notification was sent successfully
        """
        logging.info(f"Sending alert for {ticket.event_name}")
        # Copilot will implement multiple notification channels
        pass

    def send_price_drop_alert(self, ticket: TicketInfo, old_price: Decimal,
                            new_price: Decimal) -> bool:
        """
        Send notification when ticket prices drop

        Args:
            ticket: Ticket information
            old_price: Previous price
            new_price: New lower price

        Returns:
            True if notification was sent successfully
        """
        logging.info(f"Price drop alert: {ticket.event_name} from {old_price} to {new_price}")
        # Copilot will implement price drop notifications
        pass

class ScrapingStrategy(ABC):
    """
    Abstract strategy demonstrating the Strategy pattern
    Custom instructions specify using this pattern for different ticket sites
    """

    @abstractmethod
    def can_handle_site(self, url: str) -> bool:
        """Determine if this strategy can handle the given site"""
        pass

    @abstractmethod
    def extract_tickets(self, html_content: str) -> List[TicketInfo]:
        """Extract ticket information from site-specific HTML"""
        pass

    @abstractmethod
    def get_selectors(self) -> Dict[str, str]:
        """Get CSS selectors for this specific site"""
        pass

    @abstractmethod
    def get_rate_limit(self) -> float:
        """Get appropriate rate limit for this site"""
        pass
```

---

## 🎯 Demo Instructions for Presenter

### 1. Setup Custom Instructions (5 minutes)

#### Step A: Configure Custom Instructions

**What to show:**

1. Open VS Code Settings or Copilot configuration
2. Show repository-level custom instructions setup
3. Paste the web scraping domain instructions
4. Explain how this guides all Copilot behavior

**Key Message:** _"Custom instructions ensure Copilot follows your team's web scraping best practices and domain expertise"_

#### Step B: Demonstrate Instruction Impact

**Before/After Comparison:**

- Show code generation without custom instructions
- Apply web scraping domain instructions
- Show how the same prompt now produces domain-specific code with proper rate limiting, error handling, and data validation

### 2. Function Calling Intelligence (12 minutes)

#### Step A: Basic Function Calling

**Primary Demo Prompt:**

```text
Create a TicketMasterStrategy that implements the ScrapingStrategy interface
and uses the WebScrapingService to extract concert and event ticket data
```

**Expected Copilot Behavior:**

- ✅ Implements ScrapingStrategy interface correctly
- ✅ Calls WebScrapingService methods appropriately
- ✅ Uses TicketInfo class for structured data
- ✅ Includes proper rate limiting and error handling
- ✅ Follows web scraping domain custom instructions

#### Step B: Complex Function Orchestration

**Advanced Demo Prompt:**

```text
Create a complete ticket monitoring system that:
1. Uses multiple scraping strategies for different ticket sites
2. Calls data processing services for validation and analysis
3. Monitors ticket availability and price changes in real-time
4. Sends notifications when desired tickets become available
5. Handles rate limiting, errors, and site blocking gracefully
```

**Expected Intelligent Function Calling:**

- ✅ Orchestrates multiple scraping services correctly
- ✅ Calls functions in logical sequence with proper delays
- ✅ Handles inter-service dependencies and data flow
- ✅ Implements error handling and retry mechanisms
- ✅ Maintains audit trails and monitoring logs

### 3. Domain-Specific Code Generation (10 minutes)

#### Step A: Web Scraping Compliance Features

**Compliance-Focused Prompt:**

```text
Add comprehensive logging and ethical scraping features to the ticket monitoring system
including robots.txt compliance, rate limiting enforcement, and user-agent rotation
```

**Expected Compliance Code:**

- Robots.txt parsing and compliance
- Rate limiting with backoff strategies
- User-agent rotation and management
- Request caching and deduplication
- Error tracking and monitoring

#### Step B: Performance and Scalability

**Performance Optimization Prompt:**

```text
Optimize the ticket monitoring system for high-volume scraping with concurrent
processing, intelligent caching, and real-time notification delivery
```

**Expected Optimizations:**

- Async/await patterns for concurrent scraping
- Connection pooling for HTTP requests
- Intelligent caching strategies for ticket data
- Queue systems for batch processing
- Performance monitoring and metrics
- Memory-efficient data structures

### 4. Custom Instruction Compliance Demo (8 minutes)

#### Step A: Show Automatic Compliance

**Test Prompts:**

```text
Create a new ticket price tracking service
```

```text
Add user notification preferences management
```

```text
Implement proxy rotation for large-scale scraping
```

**Demonstrate that Copilot automatically:**

- ✅ Uses proper data validation with Pydantic models
- ✅ Includes comprehensive type hints and docstrings
- ✅ Implements proper rate limiting and delays
- ✅ Follows architectural patterns (Strategy, Observer)
- ✅ Includes ethical scraping considerations
- ✅ Adds comprehensive logging and monitoring

---

## Function Calling Capabilities

### Intelligent Context Selection

| Scenario                    | Function Selection                                      | Context Understanding                |
| --------------------------- | ------------------------------------------------------- | ------------------------------------ |
| **Ticket Monitoring**       | Calls scraping service → data validation → notification | Understands monitoring workflow      |
| **Price Analysis**          | Calls data services → comparison → alert generation     | Sequences operations logically       |
| **Site Strategy Selection** | Calls strategy detection → scraping → data processing   | Implements intelligent site handling |
| **Compliance Checking**     | Calls robots.txt → rate limit → ethical validation      | Maintains ethical scraping standards |

### Advanced Function Orchestration

**🧠 What Copilot Understands:**

- ✅ Function dependencies and call ordering for web scraping workflows
- ✅ Error handling and retry scenarios for unreliable websites
- ✅ Data flow between scraping, processing, and notification services
- ✅ Ethical scraping constraints and rate limiting requirements
- ✅ Performance and scalability requirements for high-volume monitoring

---

## Custom Instructions for Different Domains

### E-commerce Scraping Domain Example

```text
# GitHub Copilot Custom Instructions: E-commerce Price Monitoring

**Compliance Requirements:**
- Respect robots.txt and website terms of service
- Implement rate limiting to avoid overloading servers
- Use proper User-Agent headers and session management
- Include data validation and sanitization for all scraped content

**Code Standards:**
- Use structured data models for product information
- Implement retry mechanisms with exponential backoff
- Include comprehensive logging for audit trails
- Follow ethical scraping practices and legal compliance
```

### Data Analytics Platform Example

```text
# GitHub Copilot Custom Instructions: Data Analytics Platform

**Business Rules:**
- Include data lineage tracking for all transformations
- Implement data quality checks and validation pipelines
- Add performance monitoring for ETL processes
- Include data governance and privacy compliance

**Performance Requirements:**
- Optimize for large dataset processing with parallel execution
- Implement caching for frequently accessed analytics
- Use streaming processing for real-time data analysis
- Include monitoring for data pipeline health and performance
```

---

## Advanced Custom Instruction Prompts

For enterprise-grade customization:

1. **"Set up custom instructions for our web scraping and data extraction team"**
2. **"Create domain-specific instructions for social media monitoring systems"**
3. **"Implement custom instructions for competitive intelligence automation"**
4. **"Configure instructions for content aggregation and curation platforms"**
5. **"Set up instructions for market research and sentiment analysis tools"**
6. **"Create instructions for real-time news and event monitoring systems"**
7. **"Implement instructions for price comparison and e-commerce analytics"**
8. **"Configure instructions for SEO and digital marketing automation"**
9. **"Set up instructions for API integration and data pipeline development"**
10. **"Create instructions for automated testing and quality assurance systems"**

---

## Success Metrics

After this demo, your audience should understand:

✅ **Customization is powerful** - AI adapts to team-specific web scraping requirements
✅ **Function calling is intelligent** - AI understands data extraction workflows
✅ **Domain expertise matters** - Custom instructions encode scraping best practices
✅ **Consistency is automatic** - Ethical scraping standards enforced across development
✅ **Enterprise ready** - Professional governance and compliance features

---

## Troubleshooting

### If custom instructions aren't being followed

- Check instruction syntax and clarity
- Make instructions more specific and actionable
- Test with simple prompts first
- Verify instructions are properly configured

### If function calling seems random

- Provide more context about business workflows
- Use more descriptive function names and docstrings
- Ask Copilot to explain its reasoning
- Break complex workflows into simpler steps

### If domain expertise seems shallow

- Enhance custom instructions with more web scraping details
- Provide more domain-specific examples and use cases
- Use industry-standard terminology for data extraction
- Ask for explanations of scraping and automation concepts

---

## Implementation Strategy

### Phase 1: Basic Custom Instructions

- Define core coding standards
- Establish architectural patterns
- Set up domain vocabulary
- Test with simple code generation

### Phase 2: Advanced Domain Rules

- Add business logic constraints
- Implement compliance requirements
- Define security and audit standards
- Create workflow orchestration rules

### Phase 3: Team Optimization

- Gather feedback from developers
- Refine instructions based on usage
- Add team-specific patterns
- Optimize for productivity gains

### Phase 4: Enterprise Integration

- Scale to organization level
- Implement governance frameworks
- Add compliance reporting
- Measure ROI and effectiveness

---

## Next Steps for Your Team

1. **Audit current practices** - Identify team web scraping standards and patterns
2. **Define custom instructions** - Create domain-specific guidance for data extraction
3. **Test and iterate** - Refine instructions based on scraping results
4. **Train team members** - Show how to leverage customization for data projects
5. **Measure effectiveness** - Track consistency and productivity improvements
6. **Scale organization-wide** - Expand successful patterns to other data teams

**📁 Files needed**: Save this markdown file and prepare your team's specific web scraping custom instructions examples for demonstration.
