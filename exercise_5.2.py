def discounted(price, discount, max_discount=20):
    try:
        price = float(abs(price))
        discount = float(abs(discount))
        max_discount = float(abs(max_discount))
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except (ValueError, TypeError):
        print ('Ошибка в формате ввода')
print(discounted(100, 50, 'sd'))     