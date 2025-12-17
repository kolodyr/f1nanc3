"""
FIRE Calculator Module

Calculate Financial Independence, Retire Early (FIRE) projections.
"""

from typing import Dict, List


class FIRECalculator:
    """
    Calculate FIRE (Financial Independence, Retire Early) metrics.

    Based on the 4% rule and compound interest calculations.
    """

    def __init__(
        self,
        current_net_worth: float,
        monthly_savings: float,
        annual_return: float,
        annual_expenses: float,
        safe_withdrawal_rate: float = 0.04,
        inflation_rate: float = 0.03,
    ):
        """
        Initialize FIRE calculator.
        """
        self.current_net_worth = current_net_worth
        self.monthly_savings = monthly_savings
        self.annual_return = annual_return
        self.annual_expenses = annual_expenses
        self.safe_withdrawal_rate = safe_withdrawal_rate
        self.inflation_rate = inflation_rate

    def calculate_fire_number(self) -> float:
        """Calculate FIRE number (25x annual expenses)."""
        return self.annual_expenses / self.safe_withdrawal_rate

    def calculate_years_to_fire(self) -> float:
        """Calculate years to reach FIRE number."""
        fire_number = self.calculate_fire_number()

        if self.monthly_savings <= 0:
            return float("inf")

        if self.current_net_worth >= fire_number:
            return 0.0

        monthly_rate = (1 + self.annual_return) ** (1 / 12) - 1

        months = 0
        net_worth = self.current_net_worth

        while net_worth < fire_number and months < 12 * 100:
            net_worth = net_worth * (1 + monthly_rate) + self.monthly_savings
            months += 1

        return months / 12

    def generate_timeline(self, years: int = 30) -> Dict[int, Dict[str, float]]:
        """Generate month-by-month projection timeline."""
        monthly_rate = (1 + self.annual_return) ** (1 / 12) - 1
        timeline: Dict[int, Dict[str, float]] = {}

        net_worth = self.current_net_worth

        for month in range(years * 12):
            net_worth = net_worth * (1 + monthly_rate) + self.monthly_savings
            timeline[month] = {
                "net_worth": net_worth,
                "year": month // 12,
                "month": month % 12,
                "progress": (net_worth / self.calculate_fire_number()) * 100,
            }

        return timeline

    def simulate_scenarios(
        self,
        savings_rates: List[float],
        returns: List[float],
    ) -> Dict[str, Dict]:
        """Simulate multiple FIRE scenarios."""
        scenarios: Dict[str, Dict] = {}

        for savings in savings_rates:
            for return_rate in returns:
                calc = FIRECalculator(
                    current_net_worth=self.current_net_worth,
                    monthly_savings=savings,
                    annual_return=return_rate,
                    annual_expenses=self.annual_expenses,
                    safe_withdrawal_rate=self.safe_withdrawal_rate,
                )

                years = calc.calculate_years_to_fire()
                name = f"${savings}/mo @ {return_rate * 100:.0f}%"

                scenarios[name] = {
                    "years": years,
                    "savings": savings,
                    "return": return_rate,
                    "fire_number": calc.calculate_fire_number(),
                }

        return scenarios

    def calculate_coast_fire(self, target_age: int, current_age: int) -> float:
        """Calculate Coast FIRE number."""
        years = target_age - current_age
        fire_number = self.calculate_fire_number()
        return fire_number / ((1 + self.annual_return) ** years)

    def summary(self) -> dict:
        """
        Return a high-level summary of FIRE status.
        """
        fire_number = self.calculate_fire_number()
        years_to_fire = self.calculate_years_to_fire()

        progress_percent = (
            self.current_net_worth / fire_number * 100 if fire_number > 0 else 0.0
        )

        return {
            "fire_number": fire_number,
            "current_net_worth": self.current_net_worth,
            "progress_percent": progress_percent,
            "years_to_fire": None if years_to_fire == float("inf") else years_to_fire,
            "monthly_savings": self.monthly_savings,
            "annual_expenses": self.annual_expenses,
            "annual_return": self.annual_return,
        }


def main():
    """Example usage of FIRE Calculator."""
    calc = FIRECalculator(
        current_net_worth=3581,
        monthly_savings=200,
        annual_return=0.08,
        annual_expenses=9600,
    )

    print(calc.summary())


if __name__ == "__main__":
    main()
