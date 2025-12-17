from f1nanc3.fire_calculator import FIRECalculator

def test_basic_summary_runs():
    calc = FIRECalculator(
        current_net_worth=5000,
        monthly_savings=300,
        annual_expenses=12000,
        annual_return=0.07,
    )
    calc.summary()  # або що там повертає/друкує