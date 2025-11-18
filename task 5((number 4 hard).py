class DiscountStrategy:
    def calculate(self, amount):
        return amount

class NoDiscount(DiscountStrategy):
    pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self._percentage = percentage
    
    def calculate(self, amount):
        return amount * (1 - self._percentage / 100)

class FixedDiscount(DiscountStrategy):
    def __init__(self, discount_amount):
        self._discount_amount = discount_amount
    
    def calculate(self, amount):
        return max(0, amount - self._discount_amount)

class PriceCalculator:
    def __init__(self, discount_strategy=NoDiscount()):
        self._discount_strategy = discount_strategy
    
    def set_discount_strategy(self, strategy):
        self._discount_strategy = strategy
    
    def calculate_price(self, amount):
        return self._discount_strategy.calculate(amount)

if __name__ == "__main__":
    calculator = PriceCalculator()
    
    items_price = 1000
    
    calculator.set_discount_strategy(NoDiscount())
    print(f"Без скидки: {calculator.calculate_price(items_price)}")
    
    calculator.set_discount_strategy(PercentageDiscount(10))
    print(f"Скидка 10%: {calculator.calculate_price(items_price)}")
    
    calculator.set_discount_strategy(FixedDiscount(200))
    print(f"Скидка 200 руб: {calculator.calculate_price(items_price)}")
