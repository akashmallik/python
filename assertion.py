def apply_discount (product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price

shoes = {'name': 'Fancy Shoes', 'price': 2000}
price = apply_discount(shoes, 2)
print(price)