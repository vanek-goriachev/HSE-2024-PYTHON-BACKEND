from models.product import Product


def select_products_by_category(products: list[Product], category):
    return list(
        filter(
            lambda product: product.category == category,
            products,
        )
    )
