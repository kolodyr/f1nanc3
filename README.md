# 💰 F1NANC3 - Personal Finance Toolkit

**Comprehensive Python toolkit for FIRE (Financial Independence, Retire Early) planning, portfolio analysis, and investment tracking.**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---
## 👤 Who is this for?

This project is intended for:
- Individuals interested in FIRE (Financial Independence, Retire Early)
- Beginners learning Python through a real-world finance project
- Developers building personal finance tools or dashboards

## 🚀 Quick Start

```
git clone git@github.com:kolodyr/f1nanc3.git
cd f1nanc3

python3 -m venv .venv
source .venv/bin/activate

pip3 install -r requirements.txt

# Run examples
PYTHONPATH=. python3 examples/fire_example.py
```

## 🎯 Features

### 🔥 FIRE Calculator
- Calculate years to financial independence
- Simulate different savings rates and returns
- Account for inflation and lifestyle changes
- Multiple withdrawal strategies (4% rule, dynamic)

### 📊 Portfolio Analyzer
- Multi-asset portfolio tracking (stocks, bonds, crypto, deposits)
- Risk assessment and diversification analysis
- Rebalancing recommendations
- Performance metrics and benchmarking

### 💵 Investment Tools
- Compound interest calculations
- Dollar-cost averaging simulator
- Asset allocation optimizer
- Currency conversion (USD/UAH/EUR)

### 📈 Data Visualization
- Interactive portfolio charts
- FIRE progress tracking
- Historical performance analysis
- Net worth timeline

---

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/kolodyr/f1nanc3.git
cd f1nanc3

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```python
from src.fire_calculator import FIRECalculator

# Initialize calculator
calc = FIRECalculator(
    current_net_worth=3581,
    monthly_savings=200,
    annual_return=0.08,
    annual_expenses=9600
)

# Calculate years to FIRE
years = calc.calculate_years_to_fire()
print(f"Years to FIRE: {years:.1f}")

# Simulate different scenarios
calc.simulate_scenarios(
    savings_rates=[200, 300, 500],
    returns=[0.06, 0.08, 0.10]
)
```

---

## 📁 Project Structure

```
f1nanc3/
├── src/
│   ├── __init__.py
│   ├── fire_calculator.py      # FIRE calculations and projections
│   ├── portfolio.py             # Portfolio tracking and analysis
│   ├── investment_tools.py      # Investment utilities
│   ├── visualizer.py            # Data visualization
│   └── utils.py                 # Helper functions
├── examples/
│   ├── fire_example.py          # FIRE calculation examples
│   ├── portfolio_example.py     # Portfolio analysis examples
│   └── visualization_example.py # Charting examples
├── tests/
│   ├── test_fire_calculator.py
│   ├── test_portfolio.py
│   └── test_utils.py
├── data/
│   └── sample_portfolio.json    # Sample portfolio data
├── docs/
│   ├── fire_guide.md            # FIRE methodology guide
│   ├── portfolio_guide.md       # Portfolio management guide
│   └── api_reference.md         # API documentation
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
└── README.md                    # This file
```

---

## 🎓 Examples

### FIRE Calculator

```python
from src.fire_calculator import FIRECalculator

# Create calculator instance
fire = FIRECalculator(
    current_net_worth=3581,      # Current savings ($)
    monthly_savings=200,          # Monthly contribution ($)
    annual_return=0.08,           # Expected annual return (8%)
    annual_expenses=9600,         # Annual living expenses ($)
    safe_withdrawal_rate=0.04     # 4% rule
)

# Calculate FIRE number
fire_number = fire.calculate_fire_number()
print(f"FIRE Number (25x expenses): ${fire_number:,.0f}")

# Years to FIRE
years = fire.calculate_years_to_fire()
print(f"Years to reach FIRE: {years:.1f}")

# Monthly breakdown
timeline = fire.generate_timeline()
for month, data in timeline.items():
    print(f"Month {month}: ${data['net_worth']:,.0f}")
```

### Portfolio Analysis

```python
from src.portfolio import Portfolio

# Initialize portfolio
portfolio = Portfolio()

# Add assets
portfolio.add_asset("VOO", category="stocks", value=112, allocation=0.6)
portfolio.add_asset("QQQ", category="stocks", value=56, allocation=0.3)
portfolio.add_asset("WTAI", category="stocks", value=18, allocation=0.1)

# Analyze
analysis = portfolio.analyze()
print(f"Total Value: ${analysis['total']:,.2f}")
print(f"Asset Allocation: {analysis['allocation']}")
print(f"Risk Score: {analysis['risk_score']}/10")

# Rebalancing suggestions
rebalance = portfolio.suggest_rebalancing(
    target_allocation={"VOO": 0.7, "QQQ": 0.25, "WTAI": 0.05}
)
print(f"Rebalancing needed: {rebalance}")
```

---

## 🛠️ Technologies

- **Python 3.8+** - Core language
- **Pandas** - Data manipulation
- **NumPy** - Numerical calculations
- **Matplotlib/Plotly** - Visualization
- **Pytest** - Testing

---

## 📖 Documentation

Full documentation available in the [`docs/`](docs/) directory:

- [FIRE Planning Guide](docs/fire_guide.md) - Complete guide to FIRE methodology
- [Portfolio Management](docs/portfolio_guide.md) - Asset allocation strategies
- [API Reference](docs/api_reference.md) - Detailed API documentation

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🎯 Roadmap

### v1.0 (Current)
- [x] Basic FIRE calculator
- [x] Portfolio tracking structure
- [x] Sample examples

### v1.1 (Planned)
- [ ] Interactive web dashboard (Streamlit)
- [ ] Historical data import (CSV/Excel)
- [ ] Tax optimization calculator
- [ ] Multi-currency support (UAH/USD/EUR)

### v2.0 (Future)
- [ ] Real-time market data integration
- [ ] AI-powered recommendations
- [ ] Mobile app companion
- [ ] Social features (anonymous benchmarking)

---

## 💡 Use Cases

This toolkit is perfect for:

- 🎯 **FIRE Enthusiasts** - Track your path to financial independence
- 📊 **Investors** - Analyze and optimize your portfolio
- 💰 **Savers** - Calculate compound growth projections
- 🌍 **Expats** - Multi-currency portfolio management
- 🇺🇦 **Ukrainian investors** - UAH-specific tools and context

---

## 🙏 Acknowledgments

- Built with knowledge from the FIRE community
- Inspired by personal FIRE journey (target: 2037-2040)
- Special thanks to the Python financial tools ecosystem

---

## 📬 Contact

**Author:** Oleh Kudybyn
**Project:** [github.com/kolodyr/f1nanc3](https://github.com/kolodyr/f1nanc3)

---

**💙 Built in Ukraine 🇺🇦**

**Героям Слава!**
