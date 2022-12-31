

class Stock:
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, sell_amount: int) -> None:
        self.shares -= sell_amount

    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'
