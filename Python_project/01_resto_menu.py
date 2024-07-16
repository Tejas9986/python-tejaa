menu = {
    "Pizza": 40,
    "Pasta": 50,
    "Hot Chocalate": 49,
    "Coffie": 40,
    "Cheese Burger": 69,
    "Maggie": 35,
}

print("Welcome to i20Cafe\n")
print("Pizza = Rs40\nPasta = Rs50\nHot Chocalate = Rs49\nCoffie = Rs40\nCheese Burger = Rs69\nMaggie = Rs35")
order_total = 0

item_1 = input("Enter your first order please: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} added to your order")

else:
    print(f"Your item {item_1} is not available, please order according to menu")

item_2 = input("You have added one order, you want to order more (Yes/No) ")

if item_2 == "Yes":
    item_2 = input("Enter your order please: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} added to your order")
    else:
        print(f"Your item {item_2} is not available, please order according to menu")

print(f"Your total order is {order_total}")
