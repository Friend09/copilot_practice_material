"""
GitHub Copilot Advanced Demo 4: Function Calling & Custom Instructions
=====================================================================

This demo showcases GitHub Copilot's advanced capabilities:
- Function calling with precise context determination
- Custom instructions for team-specific coding standards
- Intelligent tool selection and usage
- Domain-specific code generation patterns

Demo Scenario: Financial Trading System
- Custom instructions for financial compliance
- Function calling for market data integration
- Team-specific architectural patterns

🎯 This demo shows how to customize Copilot for enterprise needs!
"""

from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass
from datetime import datetime, timedelta
from decimal import Decimal
import json
import logging
from abc import ABC, abstractmethod

# ============================================================================
# CUSTOM INSTRUCTIONS DEMONSTRATION
# ============================================================================

"""
📋 CUSTOM INSTRUCTIONS FOR THIS PROJECT:

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
"""

# ============================================================================
# BASE CLASSES THAT DEMONSTRATE CUSTOM INSTRUCTION COMPLIANCE
# ============================================================================

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

# ============================================================================
# FUNCTION CALLING DEMONSTRATION CLASSES
# ============================================================================

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

# ============================================================================
# FUNCTION CALLING ORCHESTRATOR
# ============================================================================

class TradingEngine:
    """
    Main trading engine that demonstrates intelligent function calling
    Copilot will understand which services to call based on context
    """

    def __init__(self, market_service: MarketDataService, risk_service: RiskManagementService):
        self.market_service = market_service
        self.risk_service = risk_service
        self.logger = logging.getLogger(__name__)

    def execute_trading_strategy(self, strategy: TradingStrategy, symbols: List[str], capital: Money) -> List[Trade]:
        """
        Execute trading strategy across multiple symbols

        This method demonstrates how Copilot will intelligently call
        various functions based on the business logic requirements

        Args:
            strategy: Trading strategy to execute
            symbols: List of symbols to analyze
            capital: Available capital for trading

        Returns:
            List of executed trades
        """
        self.logger.info(f"Executing trading strategy for {len(symbols)} symbols")
        executed_trades = []

        for symbol in symbols:
            try:
                # Copilot will understand this needs market data
                current_price = self.market_service.get_current_price(symbol)

                # Copilot will understand this needs historical context
                historical_data = self.market_service.get_historical_data(symbol, 30)

                # Copilot will call strategy methods appropriately
                if strategy.should_buy(symbol, {"current_price": current_price, "historical": historical_data}):
                    quantity = strategy.calculate_quantity(symbol, capital)

                    # Copilot will understand risk validation is needed
                    proposed_trade = Trade(
                        symbol=symbol,
                        quantity=quantity,
                        price=current_price,
                        trade_type="BUY",
                        timestamp=datetime.now(),
                        trader_id="SYSTEM"
                    )

                    # Copilot will call risk management automatically
                    if self.risk_service.validate_trade_limits(proposed_trade, {}):
                        executed_trades.append(self._execute_trade(proposed_trade))
                        capital = Money(capital.amount - (current_price.amount * quantity), capital.currency)

            except Exception as e:
                self.logger.error(f"Error processing {symbol}: {e}")
                continue

        return executed_trades

    def _execute_trade(self, trade: Trade) -> Trade:
        """
        Execute individual trade with proper logging and validation
        Following custom instructions for audit trails
        """
        self.logger.info(f"Executing trade: {trade.trade_type} {trade.quantity} {trade.symbol} @ {trade.price.amount}")
        # Copilot will implement actual trade execution logic
        return trade

# ============================================================================
# DEMO INSTRUCTIONS AND PROMPTS
# ============================================================================

"""
🎯 DEMO INSTRUCTIONS FOR PRESENTER:

1. **Setup Custom Instructions**:
   - Show the custom instructions at the top of this file
   - Explain how these guide Copilot's behavior
   - Mention team-specific coding standards

2. **Demonstrate Function Calling**:

   a) **Ask Copilot to implement a simple trading strategy**:
      "Create a MovingAverageStrategy that implements TradingStrategy interface"

   b) **Ask for market data integration**:
      "Implement the MarketDataService methods to connect to Alpha Vantage API"

   c) **Request risk management logic**:
      "Implement the RiskManagementService with position sizing and VAR calculations"

3. **Show Intelligent Context Selection**:
   - Copilot will choose appropriate functions to call
   - It will understand the sequence of operations
   - It will handle error cases appropriately

4. **Demonstrate Custom Instruction Compliance**:
   - Generated code will use Decimal for money
   - It will include proper logging
   - It will follow the architectural patterns
   - Type hints will be included automatically

5. **Advanced Function Calling**:
   - Ask: "Create a portfolio rebalancing algorithm"
   - Ask: "Add real-time market monitoring with alerts"
   - Ask: "Implement backtesting framework"

Expected Behaviors:
✅ Follows team coding standards automatically
✅ Calls appropriate functions based on business logic
✅ Includes financial domain validations
✅ Uses proper error handling patterns
✅ Implements audit logging
✅ Suggests appropriate design patterns
"""

# Advanced prompts for function calling demo
FUNCTION_CALLING_PROMPTS = [
    "Create a momentum trading strategy using the strategy pattern",
    "Implement real-time portfolio monitoring with risk alerts",
    "Add backtesting capabilities with historical data analysis",
    "Create automated rebalancing with tax-loss harvesting",
    "Implement multi-asset portfolio optimization",
    "Add compliance reporting with audit trails",
    "Create algorithmic execution with TWAP/VWAP strategies",
    "Implement options pricing and Greeks calculation",
    "Add machine learning for price prediction",
    "Create real-time risk dashboard with WebSocket updates"
]

# Custom instruction examples for different domains
CUSTOM_INSTRUCTION_EXAMPLES = {
    "financial": "Use Decimal for money, include audit trails, validate market hours",
    "healthcare": "Follow HIPAA compliance, validate patient data, include consent tracking",
    "ecommerce": "Include inventory checks, implement payment processing, add order tracking",
    "gaming": "Optimize for performance, include player state management, add telemetry",
    "iot": "Handle device connectivity, implement data buffering, add security protocols"
}

if __name__ == "__main__":
    print("🎯 GitHub Copilot Function Calling & Custom Instructions Demo")
    print("===========================================================")
    print("This demo shows intelligent function calling and team customization.")
    print("\n📋 Custom Instructions Active:")
    print("   • Use Decimal for financial calculations")
    print("   • Include comprehensive logging")
    print("   • Follow Repository and Strategy patterns")
    print("   • Add input validation and error handling")
    print("\n🎯 Try asking Copilot to:")
    for prompt in FUNCTION_CALLING_PROMPTS[:3]:
        print(f"   • {prompt}")
