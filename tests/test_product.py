def test_product_init(product):
    assert product.name == "Lenovo Legion 5"
    assert product.description == "Ryzen 7, Черный цвет, 1 Tb"
    assert product.price == 140000.0
    assert product.quantity == 3


def test_category_init(category):
    assert category.name == "Ноутбуки"
    assert category.description == "Ноутбуки отлично подходят для работы и досуга и их всегда можно взять с собой"
    assert category.products == ["Lenovo Legion 5"]
    assert category.category_count == 1
    assert category.product_count == 1
