"""
Example: FIRE Calculator Usage

Demonstrates how to use the FIRE calculator for financial planning.
"""

import sys
sys.path.append('..')

from f1nanc3.fire_calculator import FIRECalculator


def example_basic_fire():
    """Basic FIRE calculation example."""
    print("=" * 60)
    print("EXAMPLE 1: Basic FIRE Calculation")
    print("=" * 60)
    
    # Your current situation
    calc = FIRECalculator(
        current_net_worth=3581,      # Current savings
        monthly_savings=200,          # Monthly contribution
        annual_return=0.08,           # 8% annual return
        annual_expenses=9600          # $800/month expenses
    )
    
    # Calculate FIRE metrics
    fire_number = calc.calculate_fire_number()
    years_to_fire = calc.calculate_years_to_fire()
    target_year = 2025 + int(years_to_fire)
    
    print(f"\n📊 Your FIRE Numbers:")
    print(f"   Current Net Worth: ${calc.current_net_worth:,.0f}")
    print(f"   Monthly Savings: ${calc.monthly_savings:,.0f}")
    print(f"   Annual Expenses: ${calc.annual_expenses:,.0f}")
    print(f"\n🎯 FIRE Target:")
    print(f"   FIRE Number (25x expenses): ${fire_number:,.0f}")
    print(f"   Years to FIRE: {years_to_fire:.1f} years")
    print(f"   Target Year: {target_year}")
    print(f"\n💡 This means you need to save ${fire_number - calc.current_net_worth:,.0f} more!")


def example_scenarios():
    """Compare different savings scenarios."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Scenario Comparison")
    print("=" * 60)
    
    calc = FIRECalculator(
        current_net_worth=3581,
        monthly_savings=200,
        annual_return=0.08,
        annual_expenses=9600
    )
    
    # Test different scenarios
    scenarios = calc.simulate_scenarios(
        savings_rates=[200, 300, 500, 1000],
        returns=[0.06, 0.08, 0.10]
    )
    
    print("\n📈 Different Scenarios (Savings × Returns):")
    print(f"\n{'Scenario':<25} {'Years to FIRE':<15} {'Target Year':<15}")
    print("-" * 55)
    
    for name, data in sorted(scenarios.items(), key=lambda x: x[1]['years']):
        years = data['years']
        target = 2025 + int(years)
        print(f"{name:<25} {years:>10.1f} years   {target:>10}")
    
    print("\n💡 Key Insight:")
    print("   Increasing savings rate has MORE impact than higher returns!")


def example_coast_fire():
    """Calculate Coast FIRE."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Coast FIRE Calculation")
    print("=" * 60)
    
    calc = FIRECalculator(
        current_net_worth=3581,
        monthly_savings=200,
        annual_return=0.08,
        annual_expenses=9600
    )
    
    # Coast FIRE at different ages
    current_age = 27
    
    print(f"\n🏖️  Coast FIRE Numbers (Age {current_age}):")
    print(f"\n{'Retire At':<15} {'Need Now':<20} {'Status':<20}")
    print("-" * 55)
    
    for retire_age in [40, 45, 50, 55, 60]:
        coast_number = calc.calculate_coast_fire(retire_age, current_age)
        status = "✅ Achieved!" if calc.current_net_worth >= coast_number else f"Need ${coast_number - calc.current_net_worth:,.0f} more"
        print(f"Age {retire_age:<10} ${coast_number:>15,.0f}   {status}")
    
    print("\n💡 Coast FIRE means:")
    print("   Stop contributing, let money grow to FIRE by target age")


def example_timeline():
    """Show month-by-month timeline."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Year-by-Year Projection")
    print("=" * 60)
    
    calc = FIRECalculator(
        current_net_worth=3581,
        monthly_savings=200,
        annual_return=0.08,
        annual_expenses=9600
    )
    
    timeline = calc.generate_timeline(years=15)
    fire_number = calc.calculate_fire_number()
    
    print(f"\n📅 Net Worth Projection (Next 15 Years):")
    print(f"\n{'Year':<10} {'Net Worth':<20} {'Progress':<15}")
    print("-" * 45)
    
    # Show yearly milestones
    for year in range(0, 16):
        month = year * 12
        if month in timeline:
            data = timeline[month]
            nw = data['net_worth']
            progress = data['progress']
            year_label = f"{2025 + year}"
            print(f"{year_label:<10} ${nw:>15,.0f}   {progress:>6.1f}%")
    
    print(f"\n🎯 Target: ${fire_number:,.0f} (100%)")


def main():
    """Run all examples."""
    example_basic_fire()
    example_scenarios()
    example_coast_fire()
    example_timeline()
    
    print("\n" + "=" * 60)
    print("🎉 Examples Complete!")
    print("=" * 60)
    print("\n💡 Next Steps:")
    print("   1. Adjust numbers to match your situation")
    print("   2. Try different savings rates")
    print("   3. Experiment with return assumptions")
    print("   4. Track your progress monthly")
    print("\n🇺🇦 Built in Ukraine | Героям Слава!")


if __name__ == "__main__":
    main()
