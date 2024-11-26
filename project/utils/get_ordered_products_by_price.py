from models.product import Product


def get_ordered_products_by_price(products: list[Product], order="desc"):
    return sorted(
        [product for product in products],
        key=lambda product: product.get_price(),
        reverse=(order=="desc"),
    )
