"""
F1NANC3 - Personal Finance Toolkit

Comprehensive Python toolkit for FIRE planning and portfolio management.
"""

__version__ = "1.0.0"
__author__ = "Oleh Kudybyn"

from .fire_calculator import FIRECalculator
from .portfolio import Portfolio, Asset, AssetClass, RiskLevel

__all__ = [
    "FIRECalculator",
    "Portfolio",
    "Asset",
    "AssetClass",
    "RiskLevel",
]
