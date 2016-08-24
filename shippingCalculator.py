total_price = 0
item_amount = int(input("How many items are you after?"))
if item_amount < 0:
    print("Invalid number of items!")
    item_amount = int(input("How many items are you after?"))
else:
    if item_amount > 0:
        for i in range(item_amount):
            price_of_item = float(input("What is the price of the item?"))
            total_price += price_of_item
            if total_price > 100:
                total_price = total_price * 10 / 100
                print('This is the total price for ', item_amount, "items ", total_price)
            else:
                print("This is the total price for ", item_amount, "items ", total_price)
