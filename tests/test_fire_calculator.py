from f1nanc3.fire_calculator import FIRECalculator

def test_basic_summary_runs():
    calc = FIRECalculator(
        current_net_worth=5000,
        monthly_savings=300,
        annual_expenses=12000,
        annual_return=0.07,
    )

    out = calc.summary()

    assert isinstance(out, dict)
    assert "fire_number" in out
    assert out["fire_number"] > 0
    assert out["progress_percent"] >= 0