# Project: Dictionary Menu – Final Question
# Comments: Practice solution
# Solved without help: Yes
### Dictionary Mini Project: This mini project implements a simple menu and order system using Python dictionaries.
# It supports adding, updating, and removing menu items, displaying the menu, andcalculating the total cost of an order based on user input.


# -------------------------------------------------
# Menu dictionary
# -------------------------------------------------
menu = {
    "Hamburger": 1500,
    "Pasta": 1390,
    "Steak": 3800,
    "Salmon": 1900,
    "Salad": 1200,
    "Pizza": 2800
}

# -------------------------------------------------
# Add item to menu
# -------------------------------------------------
def add_item(name, price):
    menu[name] = price

# -------------------------------------------------
# Remove item from menu
# -------------------------------------------------
def remove_item(name):
    if name in menu:
        menu.pop(name)
    else:
        print("Item not found on menu")

# -------------------------------------------------
# Update price
# -------------------------------------------------
def update_price(name, new_price):
    if name in menu:
        menu[name] = new_price
    else:
        print("Item not found on menu")

# -------------------------------------------------
# Get price of one item
# -------------------------------------------------
def get_price(name):
    if name in menu:
        print(f"Item: {name}. Price: {menu[name]}")
    else:
        print("Item not found in menu")

# -------------------------------------------------
# Display full menu
# -------------------------------------------------
def display_menu(menu_dict):
    print("\nMenu:")
    for name, price in menu_dict.items():
        print(f"Item: {name}. Price: {price}")

# -------------------------------------------------
# Take order
# -------------------------------------------------
def take_order(menu_dict):
    order = []
    total_price = 0

    while True:
        choice = input(
            "Enter item you want to order, or 'q' to quit: "
        )

        if choice == "q":
            break

        if choice in menu_dict:
            order.append(choice)
            total_price += menu_dict[choice]
        else:
            print("Item not found on menu")

    print("\nOrder:", order)
    print("Total order cost:", total_price)

# -------------------------------------------------
# Main function
# -------------------------------------------------
def main():
    display_menu(menu)

    # Add item
    new_item = input("Enter item name to add to menu: ")
    new_item_price = int(input("Enter item price: "))
    add_item(new_item, new_item_price)

    # Update price
    item_name = input("Enter item name to update price: ")
    new_price = int(input("Enter new price: "))
    update_price(item_name, new_price)

    # Remove item
    item_name = input("Enter item name to remove from menu: ")
    remove_item(item_name)

    display_menu(menu)

    # Take order
    take_order(menu)

# -------------------------------------------------
# Run program
# -------------------------------------------------
main()
