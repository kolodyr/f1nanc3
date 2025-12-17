"""
Portfolio Management Module

Track and analyze investment portfolios.
"""

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum


class AssetClass(Enum):
    """Asset classification."""

    STOCKS = "stocks"
    BONDS = "bonds"
    CRYPTO = "crypto"
    CASH = "cash"
    REAL_ESTATE = "real_estate"
    COMMODITIES = "commodities"


class RiskLevel(Enum):
    """Risk level classification."""

    MINIMAL = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    VERY_HIGH = 5


@dataclass
class Asset:
    """Represents a single asset in portfolio."""

    name: str
    category: AssetClass
    value: float
    target_allocation: float
    risk_level: RiskLevel = RiskLevel.MEDIUM
    currency: str = "USD"

    @property
    def actual_allocation(self) -> float:
        """Will be calculated by Portfolio."""
        return 0.0


# --- API для Portfolio (згідно з вимогою) ---


@dataclass
class InvestmentPortfolio:
    """
    Мінімальний API для Portfolio, що використовує кількість активів (holdings)
    та ціни (prices) для розрахунків.
    """

    # тикер → кількість активів (наприклад, акцій, монет)
    holdings: Dict[str, float]
    name: str = "My Investment Portfolio"

    def total_value(self, prices: Dict[str, float]) -> float:
        """
        Розраховує загальну вартість портфеля, використовуючи надані ціни.

        Args:
            prices: Словник з тикерами та їхніми поточними цінами (тикер → ціна).

        Returns:
            Загальна вартість портфеля.
        """
        total = 0.0
        for ticker, quantity in self.holdings.items():
            if ticker in prices:
                total += quantity * prices[ticker]
            # Якщо ціна не надана, ігноруємо актив
            # Можна додати обробку помилок або логування

        return total

    def weights(self, prices: Dict[str, float]) -> Dict[str, float]:
        """
        Розраховує нормовані ваги активів у портфелі (від 0 до 1).

        Args:
            prices: Словник з тикерами та їхніми поточними цінами.

        Returns:
            Словник з тикерами та їхніми нормованими вагами.
        """
        total = self.total_value(prices)

        if total == 0:
            return {}

        weights_dict = {}
        for ticker, quantity in self.holdings.items():
            if ticker in prices:
                asset_value = quantity * prices[ticker]
                weights_dict[ticker] = asset_value / total

        return weights_dict

    def __repr__(self) -> str:
        """Рядкова репрезентація."""
        return f"InvestmentPortfolio('{self.name}', {len(self.holdings)} holdings)"


# --- Існуючий клас Portfolio (не змінений, як додатковий інструмент) ---


class Portfolio:
    # ... (Весь ваш оригінальний клас Portfolio тут) ...
    # Я залишу його без змін, оскільки ви просили API, що базується на 'holdings' і 'prices',
    # що краще реалізовано у InvestmentPortfolio.

    def __init__(self, name: str = "My Portfolio"):
        """
        Initialize portfolio.

        Args:
            name: Portfolio name
        """
        self.name = name
        self.assets: List[Asset] = []

    def add_asset(
        self,
        name: str,
        category: str,
        value: float,
        target_allocation: float,
        risk_level: int = 3,
        currency: str = "USD",
    ) -> None:
        """
        Add asset to portfolio.

        Args:
            name: Asset name/ticker
            category: Asset class (stocks, bonds, etc.)
            value: Current value ($)
            target_allocation: Target allocation (0.0-1.0)
            risk_level: Risk level (1-5)
            currency: Currency code
        """
        asset_class = AssetClass(category.lower())
        risk = RiskLevel(risk_level)

        asset = Asset(
            name=name,
            category=asset_class,
            value=value,
            target_allocation=target_allocation,
            risk_level=risk,
            currency=currency,
        )

        self.assets.append(asset)

    def total_value(self) -> float:
        """Calculate total portfolio value."""
        return sum(asset.value for asset in self.assets)

    def get_allocation(self) -> Dict[str, float]:
        """
        Get current asset allocation.

        Returns:
            Dictionary of asset allocations
        """
        total = self.total_value()
        if total == 0:
            return {}

        allocation = {}
        for asset in self.assets:
            allocation[asset.name] = asset.value / total

        return allocation

    def get_category_allocation(self) -> Dict[str, float]:
        """
        Get allocation by asset category.

        Returns:
            Dictionary of category allocations
        """
        total = self.total_value()
        if total == 0:
            return {}

        category_totals = {}
        for asset in self.assets:
            category = asset.category.value
            if category not in category_totals:
                category_totals[category] = 0
            category_totals[category] += asset.value

        return {cat: val / total for cat, val in category_totals.items()}

    def calculate_risk_score(self) -> float:
        """
        Calculate portfolio risk score (1-10).

        Weighted average of asset risk levels.

        Returns:
            Risk score (1-10)
        """
        total = self.total_value()
        if total == 0:
            return 0.0

        weighted_risk = sum(
            asset.value * asset.risk_level.value for asset in self.assets
        )

        # Normalize to 1-10 scale
        return (weighted_risk / total) * 2

    def suggest_rebalancing(self, tolerance: float = 0.05) -> Dict[str, Dict]:
        """
        Suggest rebalancing actions.

        Args:
            tolerance: Allocation tolerance (default 5%)

        Returns:
            Dictionary of rebalancing suggestions
        """
        total = self.total_value()
        current_allocation = self.get_allocation()
        suggestions = {}

        for asset in self.assets:
            current = current_allocation.get(asset.name, 0)
            target = asset.target_allocation
            diff = current - target

            if abs(diff) > tolerance:
                action = "sell" if diff > 0 else "buy"
                amount = abs(diff) * total

                suggestions[asset.name] = {
                    "action": action,
                    "amount": amount,
                    "current": current,
                    "target": target,
                    "difference": diff,
                }

        return suggestions

    def analyze(self) -> Dict:
        """
        Comprehensive portfolio analysis.

        Returns:
            Analysis dictionary
        """
        return {
            "name": self.name,
            "total_value": self.total_value(),
            "asset_count": len(self.assets),
            "allocation": self.get_allocation(),
            "category_allocation": self.get_category_allocation(),
            "risk_score": self.calculate_risk_score(),
            "rebalancing": self.suggest_rebalancing(),
        }

    def __repr__(self) -> str:
        """String representation."""
        return f"Portfolio('{self.name}', {len(self.assets)} assets, ${self.total_value():,.2f})"


def main():
    """Example usage of Portfolio."""

    # --- Тестування InvestmentPortfolio API ---
    print("--- InvestmentPortfolio API Test ---")

    # 1. Створюємо приклад портфеля з кількістю активів (holdings)
    holdings = {
        "TSLA": 5.0,  # 5 акцій TSLA
        "AAPL": 10.0,  # 10 акцій AAPL
        "BTC": 0.05,  # 0.05 BTC
    }
    invest_portfolio = InvestmentPortfolio(holdings=holdings, name="Tech Crypto Mix")

    # 2. Визначаємо поточні ціни
    current_prices = {
        "TSLA": 250.00,
        "AAPL": 180.00,
        "BTC": 45000.00,
    }

    # 3. Розраховуємо загальну вартість
    total_value = invest_portfolio.total_value(current_prices)
    print(f"Portfolio: {invest_portfolio.name}")
    print(f"Total Value: ${total_value:,.2f}")

    # 4. Розраховуємо ваги
    weights = invest_portfolio.weights(current_prices)
    print("\nAsset Weights:")
    for ticker, weight in weights.items():
        print(f"  {ticker}: {weight * 100:.2f}%")

    print("\n" + "=" * 50 + "\n")

    # --- Існуючий приклад використання Portfolio ---
    print("--- Existing Portfolio Class Test ---")

    # Create portfolio
    portfolio = Portfolio("IBKR Portfolio")

    # Add assets
    portfolio.add_asset("VOO", "stocks", 112, 0.6, risk_level=3)
    portfolio.add_asset("QQQ", "stocks", 56, 0.3, risk_level=4)
    portfolio.add_asset("WTAI", "stocks", 18, 0.1, risk_level=5)

    # Analyze
    analysis = portfolio.analyze()

    print(f"Portfolio: {analysis['name']}")
    print(f"Total Value: ${analysis['total_value']:,.2f}")
    print("\nAllocation:")
    for asset, alloc in analysis["allocation"].items():
        print(f"  {asset}: {alloc * 100:.1f}%")

    print(f"\nRisk Score: {analysis['risk_score']:.1f}/10")

    print("\nRebalancing Suggestions:")
    if analysis["rebalancing"]:
        for asset, suggestion in analysis["rebalancing"].items():
            print(
                f"  {suggestion['action'].upper()} ${suggestion['amount']:.2f} of {asset}"
            )
    else:
        print("  No rebalancing needed ✓")


if __name__ == "__main__":
    main()
