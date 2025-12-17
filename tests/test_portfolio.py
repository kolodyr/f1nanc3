import pytest
from f1nanc3.portfolio import InvestmentPortfolio

# Базові дані для тестування
@pytest.fixture
def sample_portfolio():
    """Фікстура для створення базового об'єкта InvestmentPortfolio."""
    holdings = {
        "TSLA": 5.0,     # 5 акцій
        "AAPL": 10.0,    # 10 акцій
        "BTC": 0.05,     # 0.05 BTC
    }
    return InvestmentPortfolio(holdings=holdings, name="Test Portfolio")

@pytest.fixture
def sample_prices():
    """Фікстура для надання цін для всіх активів."""
    return {
        "TSLA": 250.00,
        "AAPL": 180.00,
        "BTC": 45000.00,
    }

class TestInvestmentPortfolioContract:
    """Тести для перевірки виконання контракту InvestmentPortfolio."""

    # 1. total_value повертає число > 0 для базового кейсу
    def test_total_value_returns_positive_number_for_base_case(self, sample_portfolio, sample_prices):
        """Перевірка, що загальна вартість розраховується коректно і є позитивною."""
        
        # Очікуване значення:
        # TSLA: 5 * 250 = 1250
        # AAPL: 10 * 180 = 1800
        # BTC: 0.05 * 45000 = 2250
        # Total: 1250 + 1800 + 2250 = 5300.0
        
        total = sample_portfolio.total_value(sample_prices)
        
        # Перевірка типу
        assert isinstance(total, float)
        
        # Перевірка, що значення позитивне
        assert total > 0.0
        
        # Перевірка на точне значення (базовий кейс)
        assert total == 5300.0
    
    # 2. weights повертає dict, сума ваг ≈ 1.0
    def test_weights_returns_normalized_dict_and_sums_to_one(self, sample_portfolio, sample_prices):
        """Перевірка, що метод weights повертає словник, а сума ваг близька до 1.0."""
        
        weights = sample_portfolio.weights(sample_prices)
        
        # Перевірка типу
        assert isinstance(weights, dict)
        
        # Перевірка, що словник містить всі активи
        assert set(weights.keys()) == set(sample_portfolio.holdings.keys())
        
        # Перевірка, що всі ваги знаходяться в діапазоні [0, 1]
        for weight in weights.values():
            assert 0.0 <= weight <= 1.0
            
        # Перевірка, що сума ваг дорівнює 1.0 (з допустимою похибкою)
        sum_of_weights = sum(weights.values())
        assert sum_of_weights == pytest.approx(1.0)
        
    # 3. Якщо нема ціни для тикера → ігнор
    def test_missing_price_is_ignored_in_total_value(self, sample_portfolio, sample_prices):
        """
        Перевірка, що актив, для якого відсутня ціна, ігнорується,
        і не викликається KeyError.
        """
        
        # Видаляємо ціну для BTC
        prices_missing_btc = sample_prices.copy()
        del prices_missing_btc["BTC"]
        
        # Очікуваний Total: 1250 (TSLA) + 1800 (AAPL) = 3050.0
        
        # Перевіряємо, що метод не викликає помилки (KeyError)
        total = sample_portfolio.total_value(prices_missing_btc)
        
        # Перевіряємо, що total дорівнює сумі вартостей лише наявних активів
        assert total == 3050.0

    # 4. Якщо нема ціни для тикера → ігнор (зафіксуй тестом для weights)
    def test_missing_price_is_ignored_in_weights_calculation(self, sample_portfolio, sample_prices):
        """
        Перевірка, що актив, для якого відсутня ціна, не входить
        у розрахунок ваг, і загальна сума ваг все одно ≈ 1.0.
        """
        
        # Видаляємо ціну для BTC
        prices_missing_btc = sample_prices.copy()
        del prices_missing_btc["BTC"]

        weights = sample_portfolio.weights(prices_missing_btc)
        
        # Перевіряємо, що BTC відсутній у словнику ваг
        assert "BTC" not in weights
        
        # Перевіряємо, що у словнику ваг лише 2 активи
        assert len(weights) == 2 
        
        # Перевіряємо, що сума ваг (для TSLA та AAPL) все одно ~1.0, 
        # оскільки вони нормуються на їхню загальну вартість (3050.0)
        sum_of_weights = sum(weights.values())
        assert sum_of_weights == pytest.approx(1.0)