def apply_discount(price, discount_percent):
    """ Apply discount and return final price """
    discount_amount = price * (discount_percennt / 100)
    final_price = price - discount_amount
    return round(final_price, 2)

print("=== Product Discounts ===")
price1 = apply_discount(100, 10)
print(f"Product 1 final price: ${price1}")

price2 = apply_discount(250, 20)
print(f"Product 2 final price: ${price2}")

price3 = apply_discount(75, 15)
print(f"Prodect 3 final price: ${price3}")