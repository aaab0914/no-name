def apply_discount(price, discount_percent):
    # New logic: $10 off for orders over $100
    if price >= 100:
        final_price = price - 10
    else:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
    return round(final_price, 2)
# All calls automatically use new rules!