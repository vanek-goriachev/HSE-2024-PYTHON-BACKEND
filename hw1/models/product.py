class Product:
    name: str
    category: str
    price: float
    sale: float

    class Constants:
        DEFAULT_SALE = 0

    def __init__(self, name: str, category: str, price: float) -> None:
        self.name = name
        self.category = category
        self.price = price
        self.sale = self.Constants.DEFAULT_SALE

    def edit_category(self, new_category: str) -> None:
        self.category = new_category

    def edit_price(self, new_price: float) -> None:
        self.price = new_price

    def set_sale(self, sale: float) -> None:
        self.sale = sale

    def cancel_sale(self) -> None:
        self.sale = self.Constants.DEFAULT_SALE

    def get_price(self) -> float:
        return self.price * sale_to_multiplier(self.sale)

    def __repr__(self) -> str:
        return f"<Product {self.name}>"


def sale_to_multiplier(sale: float) -> float:
    return (100 - sale) / 100
