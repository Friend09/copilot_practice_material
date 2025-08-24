# GitHub Copilot Advanced Demo 4: Function Calling & Custom Instructions

## Overview

This demo showcases GitHub Copilot's advanced capabilities:

- **Function calling with precise context determination**
- **Custom instructions for team-specific coding standards**
- **Intelligent tool selection and usage**
- **Domain-specific code generation patterns**
- **Enterprise-grade customization and governance**

## Demo Scenario

**Financial Trading System** - Demonstrate custom instructions for financial compliance, function calling for market data integration, and team-specific architectural patterns.

🎯 **This demo shows how to customize Copilot for enterprise needs!**

---

## Custom Instructions Examples

### Financial Domain Custom Instructions

```text
# GitHub Copilot Custom Instructions: Financial Trading System

## Code Style Guidelines:
1. Use type hints for all function parameters and return values
2. Include docstrings with parameter descriptions and examples
3. Use Decimal for all financial calculations (never float)
4. Include logging for all business-critical operations
5. Add input validation for all public methods
6. Follow the Repository pattern for data access
7. Use dataclasses for value objects
8. Include error handling with custom exceptions

## Financial Domain Rules:
1. All monetary amounts must use Decimal type
2. Include currency code with all financial operations
3. Log all trading decisions with timestamps
4. Validate market hours before placing orders
5. Include risk management checks
6. Use audit trails for compliance

## Architecture Patterns:
1. Separate business logic from infrastructure
2. Use dependency injection for external services
3. Implement the Strategy pattern for trading algorithms
4. Use Observer pattern for price updates
5. Include circuit breakers for external API calls

Ask Copilot to follow these instructions when generating code!
```

---

## Foundation Code Examples

### Value Objects with Financial Domain Rules

```python
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
import json
import logging
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class Money:
    """
    Value object for monetary amounts - demonstrates custom instruction
    for using Decimal instead of float for financial calculations
    """
    amount: Decimal
    currency: str = "USD"

    def __post_init__(self):
        if not isinstance(self.amount, Decimal):
            raise ValueError("Amount must be Decimal type for financial accuracy")
        if len(self.currency) != 3:
            raise ValueError("Currency must be 3-letter ISO code")

    def add(self, other: 'Money') -> 'Money':
        """Add two Money objects with currency validation"""
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}")
        return Money(self.amount + other.amount, self.currency)

@dataclass
class Trade:
    """
    Trade entity following custom instructions for financial domain modeling
    """
    symbol: str
    quantity: int
    price: Money
    trade_type: str  # 'BUY' or 'SELL'
    timestamp: datetime
    trader_id: str
    order_id: Optional[str] = None

    def __post_init__(self):
        # Validation following custom instructions
        if self.trade_type not in ['BUY', 'SELL']:
            raise ValueError("Trade type must be 'BUY' or 'SELL'")
        if self.quantity <= 0:
            raise ValueError("Quantity must be positive")

class TradingException(Exception):
    """Custom exception following team guidelines"""
    pass

class MarketClosedException(TradingException):
    """Raised when attempting to trade outside market hours"""
    pass
```

### Function Calling Demonstration Classes

```python
class MarketDataService:
    """
    Service that demonstrates function calling capabilities
    Copilot will understand when to call these methods based on context
    """

    def get_current_price(self, symbol: str) -> Money:
        """
        Get current market price for a symbol

        Args:
            symbol: Stock symbol (e.g., 'AAPL', 'GOOGL')

        Returns:
            Current market price as Money object

        Example:
            >>> service = MarketDataService()
            >>> price = service.get_current_price('AAPL')
            >>> print(f"AAPL: {price.amount} {price.currency}")
        """
        # Copilot will understand this needs external API integration
        logging.info(f"Fetching current price for {symbol}")
        # Mock implementation - Copilot will suggest real API integration
        return Money(Decimal("150.25"), "USD")

    def get_historical_data(self, symbol: str, days: int = 30) -> List[Dict[str, Any]]:
        """
        Get historical price data

        Args:
            symbol: Stock symbol
            days: Number of days of historical data

        Returns:
            List of price data points
        """
        logging.info(f"Fetching {days} days of historical data for {symbol}")
        # Copilot will implement based on requirements
        pass

    def subscribe_to_price_updates(self, symbol: str, callback: Callable) -> None:
        """
        Subscribe to real-time price updates

        Args:
            symbol: Stock symbol to monitor
            callback: Function to call when price updates
        """
        logging.info(f"Subscribing to price updates for {symbol}")
        # Copilot will implement websocket or streaming connection
        pass

class RiskManagementService:
    """
    Demonstrates function calling for risk assessment
    """

    def calculate_position_risk(self, symbol: str, quantity: int, current_portfolio: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate risk metrics for a potential trade

        Args:
            symbol: Stock symbol
            quantity: Proposed trade quantity
            current_portfolio: Current portfolio positions

        Returns:
            Risk assessment including concentration risk, VAR, etc.
        """
        logging.info(f"Calculating position risk for {quantity} shares of {symbol}")
        # Copilot will implement sophisticated risk calculations
        pass

    def validate_trade_limits(self, trade: Trade, trader_limits: Dict[str, Any]) -> bool:
        """
        Validate trade against risk limits

        Args:
            trade: Proposed trade
            trader_limits: Risk limits for the trader

        Returns:
            True if trade is within limits
        """
        logging.info(f"Validating trade limits for {trade.symbol}")
        # Copilot will implement limit checking logic
        pass

class TradingStrategy(ABC):
    """
    Abstract strategy demonstrating the Strategy pattern
    Custom instructions specify using this pattern for algorithms
    """

    @abstractmethod
    def should_buy(self, symbol: str, market_data: Dict[str, Any]) -> bool:
        """Determine if symbol should be bought"""
        pass

    @abstractmethod
    def should_sell(self, symbol: str, market_data: Dict[str, Any]) -> bool:
        """Determine if symbol should be sold"""
        pass

    @abstractmethod
    def calculate_quantity(self, symbol: str, available_capital: Money) -> int:
        """Calculate appropriate trade quantity"""
        pass
```

---

## 🎯 Demo Instructions for Presenter

### 1. Setup Custom Instructions (5 minutes)

#### Step A: Configure Custom Instructions

**What to show:**

1. Open VS Code Settings or Copilot configuration
2. Show repository-level custom instructions setup
3. Paste the financial domain instructions
4. Explain how this guides all Copilot behavior

**Key Message:** _"Custom instructions ensure Copilot follows your team's specific requirements and domain expertise"_

#### Step B: Demonstrate Instruction Impact

**Before/After Comparison:**

- Show code generation without custom instructions
- Apply financial domain instructions
- Show how the same prompt now produces domain-specific code

### 2. Function Calling Intelligence (12 minutes)

#### Step A: Basic Function Calling

**Primary Demo Prompt:**

```text
Create a MovingAverageStrategy that implements the TradingStrategy interface
and uses the MarketDataService to make trading decisions
```

**Expected Copilot Behavior:**

- ✅ Implements TradingStrategy interface correctly
- ✅ Calls MarketDataService methods appropriately
- ✅ Uses Money class for financial calculations
- ✅ Includes proper error handling and logging
- ✅ Follows financial domain custom instructions

#### Step B: Complex Function Orchestration

**Advanced Demo Prompt:**

```text
Create a complete trading engine that:
1. Uses multiple strategies to evaluate trades
2. Calls risk management for validation
3. Executes trades through the market data service
4. Logs all decisions for audit compliance
5. Handles errors and market closures gracefully
```

**Expected Intelligent Function Calling:**

- ✅ Orchestrates multiple services correctly
- ✅ Calls functions in logical sequence
- ✅ Handles inter-service dependencies
- ✅ Implements error handling and rollbacks
- ✅ Maintains audit trails

### 3. Domain-Specific Code Generation (10 minutes)

#### Step A: Financial Compliance Features

**Compliance-Focused Prompt:**

```text
Add comprehensive audit logging and compliance features to the trading system
including trade reporting, risk monitoring, and regulatory compliance checks
```

**Expected Compliance Code:**

- Audit trail implementation
- Regulatory reporting features
- Risk monitoring and alerts
- Compliance validation checks
- Data retention policies

#### Step B: Performance and Scalability

**Performance Optimization Prompt:**

```text
Optimize the trading system for high-frequency trading with real-time
market data processing and sub-millisecond execution requirements
```

**Expected Optimizations:**

- Async/await patterns for performance
- Connection pooling for market data
- Caching strategies for frequently accessed data
- Memory-efficient data structures
- Performance monitoring and metrics

### 4. Custom Instruction Compliance Demo (8 minutes)

#### Step A: Show Automatic Compliance

**Test Prompts:**

```text
Create a new portfolio management service
```

```text
Add payment processing functionality
```

```text
Implement user authentication for the trading platform
```

**Demonstrate that Copilot automatically:**

- ✅ Uses Decimal for all financial amounts
- ✅ Includes comprehensive type hints
- ✅ Implements proper logging
- ✅ Follows architectural patterns
- ✅ Includes security considerations
- ✅ Adds audit trailing

---

## Function Calling Capabilities

### Intelligent Context Selection

| Scenario               | Function Selection                                    | Context Understanding             |
| ---------------------- | ----------------------------------------------------- | --------------------------------- |
| **Trading Decision**   | Calls market data → risk assessment → execution       | Understands business workflow     |
| **Portfolio Analysis** | Calls data services → calculation → reporting         | Sequences operations logically    |
| **Risk Management**    | Calls position analysis → limit validation → alerting | Implements safety checks          |
| **Audit Reporting**    | Calls data retrieval → aggregation → formatting       | Maintains compliance requirements |

### Advanced Function Orchestration

**🧠 What Copilot Understands:**

- ✅ Function dependencies and call ordering
- ✅ Error handling and rollback scenarios
- ✅ Data flow between service calls
- ✅ Business logic constraints
- ✅ Performance and scalability requirements

---

## Custom Instructions for Different Domains

### Healthcare Domain Example

```text
# GitHub Copilot Custom Instructions: Healthcare Systems

**Compliance Requirements:**
- Follow HIPAA guidelines for all patient data handling
- Include consent tracking for all data operations
- Use encryption for all sensitive data storage and transmission
- Implement audit logging for all patient data access

**Code Standards:**
- Use strongly typed patient identifiers
- Include data validation for all medical inputs
- Implement proper error handling without exposing patient data
- Follow HL7 FHIR standards for healthcare data exchange
```

### E-commerce Domain Example

```text
# GitHub Copilot Custom Instructions: E-commerce Platform

**Business Rules:**
- Include inventory checks before order processing
- Implement payment processing with PCI compliance
- Add order tracking and status management
- Include customer notification systems

**Performance Requirements:**
- Optimize for high traffic during sales events
- Implement caching for product catalogs
- Use async processing for order fulfillment
- Include monitoring for conversion funnels
```

---

## Advanced Custom Instruction Prompts

For enterprise-grade customization:

1. **"Set up custom instructions for our Django REST API development team"**
2. **"Create domain-specific instructions for IoT device management systems"**
3. **"Implement custom instructions for cloud-native microservices architecture"**
4. **"Configure instructions for machine learning model deployment pipelines"**
5. **"Set up instructions for blockchain and cryptocurrency applications"**
6. **"Create instructions for real-time gaming and simulation systems"**
7. **"Implement instructions for enterprise security and compliance systems"**
8. **"Configure instructions for data engineering and analytics platforms"**
9. **"Set up instructions for mobile app development with React Native"**
10. **"Create instructions for DevOps automation and infrastructure management"**

---

## Success Metrics

After this demo, your audience should understand:

✅ **Customization is powerful** - AI adapts to team-specific requirements
✅ **Function calling is intelligent** - AI understands business workflows
✅ **Domain expertise matters** - Custom instructions encode team knowledge
✅ **Consistency is automatic** - Standards are enforced across all development
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

- Enhance custom instructions with more detail
- Provide more domain-specific examples
- Use industry-standard terminology consistently
- Ask for explanations of domain concepts

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

1. **Audit current practices** - Identify team coding standards and patterns
2. **Define custom instructions** - Create domain-specific guidance
3. **Test and iterate** - Refine instructions based on results
4. **Train team members** - Show how to leverage customization
5. **Measure effectiveness** - Track consistency and productivity improvements
6. **Scale organization-wide** - Expand successful patterns to other teams

**📁 Files needed**: Save this markdown file and prepare your team's specific custom instructions examples for demonstration.
