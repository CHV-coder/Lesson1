def discounted(price, discount, max_discount = 10):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError("Максимальная скидка не должна быть больше 100")
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return(price_with_discount)
    
    
product = {'name': 'Sumsung', 'price': 2000, 'discount': 5}
product['with_discount'] = discounted(product['price'], product['discount'])

print(discounted(100, 9))
