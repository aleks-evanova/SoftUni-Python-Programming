commands = input().split()
bakery_shop_dict = {}
sold_items_quantity = 0

while True:

    if commands[0] == "Complete":
        break

    if commands[0] == "Receive":
        quantity = int(commands[1])
        food = commands[2]
        if quantity <= 0:
            break
        else:
            if food not in bakery_shop_dict.keys():
                bakery_shop_dict[food] = quantity
            else:
                bakery_shop_dict[food] += quantity
    elif commands[0] == "Sell":
        quantity_given = int(commands[1])
        food_given = commands[2]
        if quantity_given <= 0:
            break
        if food_given not in bakery_shop_dict.keys():
            print(f'You do not have any {food_given}.')
        else:
            quantity_in_dict = bakery_shop_dict.get(food_given)
            if quantity_in_dict < quantity_given:
                bakery_shop_dict[food_given] -= quantity_in_dict
                sold_items_quantity += quantity_in_dict
                bakery_shop_dict.pop(food_given)
                print(f"There aren't enough {food_given}. You sold the last {quantity_in_dict} of them.")
            else:
                bakery_shop_dict[food_given] -= quantity_given
                sold_items_quantity += quantity_given
                quantity_in_dict = bakery_shop_dict.get(food_given)
                print(f"You sold {quantity_given} {food_given}.")
                if quantity_in_dict == 0:
                    bakery_shop_dict.pop(food_given)

    commands = input().split()

for key, value in bakery_shop_dict.items():
    print(f'{key}: {value}')
print(f'All sold: {sold_items_quantity} goods')
