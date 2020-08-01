def discounted(price, discount, max_discount = 80):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount >= 99:
        raise ValueError("Максимальная скидка не может быть больше 99%")
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount


discounted (100, 50, max_discount = 100)