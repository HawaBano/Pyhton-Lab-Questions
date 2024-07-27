original_price = float(input("Enter the original price: "))
discount_price = float(input("Enter the discount percentage: "))


if discount_price < 0 or discount_price > 100:
    print("Invalid discount price")
else:
    a =  discount_price * (original_price / 100)
    b = original_price - a
    print("the price after discount is:",b)
