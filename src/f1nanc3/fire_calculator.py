"""
FIRE Calculator Module

Calculate Financial Independence, Retire Early (FIRE) projections.
"""

from typing import Dict, List, Optional
import numpy as np


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
        inflation_rate: float = 0.03
    ):
        """
        Initialize FIRE calculator.
        
        Args:
            current_net_worth: Current total net worth ($)
            monthly_savings: Monthly savings amount ($)
            annual_return: Expected annual return rate (e.g., 0.08 for 8%)
            annual_expenses: Annual living expenses ($)
            safe_withdrawal_rate: Safe withdrawal rate (default: 0.04 = 4% rule)
            inflation_rate: Expected inflation rate (default: 0.03 = 3%)
        """
        self.current_net_worth = current_net_worth
        self.monthly_savings = monthly_savings
        self.annual_return = annual_return
        self.annual_expenses = annual_expenses
        self.safe_withdrawal_rate = safe_withdrawal_rate
        self.inflation_rate = inflation_rate
    
    def calculate_fire_number(self) -> float:
        """
        Calculate FIRE number (25x annual expenses).
        
        Returns:
            FIRE number ($ needed to retire)
        """
        return self.annual_expenses / self.safe_withdrawal_rate
    
    def calculate_years_to_fire(self) -> float:
        """
        Calculate years to reach FIRE number.
        
        Returns:
            Years until financial independence
        """
        fire_number = self.calculate_fire_number()
        
        if self.monthly_savings <= 0:
            return float('inf')
        
        # Monthly return rate
        monthly_rate = (1 + self.annual_return) ** (1/12) - 1
        
        # Future value of annuity formula
        # FV = PV(1+r)^n + PMT * [((1+r)^n - 1) / r]
        
        # Solve for n (months)
        if self.current_net_worth >= fire_number:
            return 0.0
        
        months = 0
        net_worth = self.current_net_worth
        
        while net_worth < fire_number and months < 12 * 100:  # Max 100 years
            net_worth = net_worth * (1 + monthly_rate) + self.monthly_savings
            months += 1
        
        return months / 12
    
    def generate_timeline(self, years: int = 30) -> Dict[int, Dict[str, float]]:
        """
        Generate month-by-month projection timeline.
        
        Args:
            years: Number of years to project
            
        Returns:
            Dictionary with monthly projections
        """
        monthly_rate = (1 + self.annual_return) ** (1/12) - 1
        timeline = {}
        
        net_worth = self.current_net_worth
        months = years * 12
        
        for month in range(months):
            net_worth = net_worth * (1 + monthly_rate) + self.monthly_savings
            
            timeline[month] = {
                'net_worth': net_worth,
                'year': month // 12,
                'month': month % 12,
                'progress': (net_worth / self.calculate_fire_number()) * 100
            }
        
        return timeline
    
    def simulate_scenarios(
        self,
        savings_rates: List[float],
        returns: List[float]
    ) -> Dict:
        """
        Simulate multiple FIRE scenarios.
        
        Args:
            savings_rates: List of monthly savings amounts to test
            returns: List of annual return rates to test
            
        Returns:
            Dictionary of scenarios with years to FIRE
        """
        scenarios = {}
        
        for savings in savings_rates:
            for return_rate in returns:
                calc = FIRECalculator(
                    current_net_worth=self.current_net_worth,
                    monthly_savings=savings,
                    annual_return=return_rate,
                    annual_expenses=self.annual_expenses,
                    safe_withdrawal_rate=self.safe_withdrawal_rate
                )
                
                years = calc.calculate_years_to_fire()
                
                scenario_name = f"${savings}/mo @ {return_rate*100:.0f}%"
                scenarios[scenario_name] = {
                    'years': years,
                    'savings': savings,
                    'return': return_rate,
                    'fire_number': calc.calculate_fire_number()
                }
        
        return scenarios
    
    def calculate_coast_fire(self, target_age: int, current_age: int) -> float:
        """
        Calculate Coast FIRE number (savings that will grow to FIRE by target age).
        
        Args:
            target_age: Age you want to retire
            current_age: Your current age
            
        Returns:
            Coast FIRE number (amount needed now to coast to FIRE)
        """
        years = target_age - current_age
        fire_number = self.calculate_fire_number()
        
        # Present value of FIRE number
        coast_fire = fire_number / ((1 + self.annual_return) ** years)
        
        return coast_fire


def main():
    """Example usage of FIRE Calculator."""
    
    # Example: Calculate FIRE for typical scenario
    calc = FIRECalculator(
        current_net_worth=3581,
        monthly_savings=200,
        annual_return=0.08,
        annual_expenses=9600
    )
    
    fire_number = calc.calculate_fire_number()
    years = calc.calculate_years_to_fire()
    
    print(f"FIRE Number (25x expenses): ${fire_number:,.0f}")
    print(f"Years to FIRE: {years:.1f}")
    print(f"Target year: {2025 + int(years)}")
    
    # Scenarios
    print("\nScenarios:")
    scenarios = calc.simulate_scenarios(
        savings_rates=[200, 300, 500],
        returns=[0.07, 0.08, 0.10]
    )
    
    for name, data in scenarios.items():
        print(f"{name}: {data['years']:.1f} years")


if __name__ == "__main__":
    main()
