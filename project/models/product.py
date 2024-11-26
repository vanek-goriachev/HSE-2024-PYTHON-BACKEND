class Product:
    DEFAULT_SALE = 0

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        self.sale = self.DEFAULT_SALE

    def edit_category(self, new_category):
        self.category = new_category

    def edit_price(self, new_price):
        self.price = new_price

    def set_sale(self, sale):
        self.sale = sale

    def cancel_sale(self):
        self.sale = self.DEFAULT_SALE

    def get_price(self):
        return self.price * sale_to_multiplier(self.sale)

    def __repr__(self) -> str:
        return f"<Product {self.name}>"


def sale_to_multiplier(sale):
    return (100 - sale) / 100
