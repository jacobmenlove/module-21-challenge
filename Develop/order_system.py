def place_order(menu, predefined_inputs=None):
    """
    Displays a restaurant menu, asks customers for their order, then returns
    their receipt and total price.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their 
                       prices.
    predefined_inputs (list): A list of inputs to simulate user input for testing.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                  and quantity ordered.
    order_total (float): The total price of the order.
    """
    order = []
    menu_items = get_menu_items_dict(menu)
    print("Welcome to the Generic Take Out Restaurant.")
    
    input_iterator = iter(predefined_inputs) if predefined_inputs else iter([])

    while True:
        print_menu_heading()
        i = 1
        
        for food_category, options in menu.items():
            for meal, price in options.items():
                print_menu_line(i, food_category, meal, price)
                i += 1

        # Use predefined inputs or standard input
        try:
            menu_selection = next(input_iterator, "") if predefined_inputs else input("Please enter the number of the item you want to order: ").strip()
        except StopIteration:
            print("No more predefined inputs available.")
            break

        if menu_selection == "":
            print("Input cannot be empty. Please try again.")
            continue

        # Update the order list using the update_order function
        order = update_order(order, menu_selection, menu_items)

        if order:  # Only ask to continue if the order was updated
            continue_ordering = next(input_iterator, "n") if predefined_inputs else input("Would you like to order anything else? (y/n): ").strip()
            if continue_ordering.lower() == 'n':
                print("Thank you for your order!")
                prices_list = [item["Price"] * item["Quantity"] for item in order]
                order_total = round(sum(prices_list), 2)
                return order, order_total
        else:
            print("Order was not updated. Please try again.")

def update_order(order, menu_selection, menu_items):
    """
    Checks if the customer menu selection is valid, then updates the order.

    Parameters:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    menu_selection (str): The customer's menu selection.
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.

    Returns:
    order (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered (updated as needed).
    """
    if menu_selection.isdigit():
        menu_selection = int(menu_selection)
        if menu_selection in menu_items:
            item_name = menu_items[menu_selection]["Item name"]
            item_price = menu_items[menu_selection]["Price"]
            quantity = input(f"How many of {item_name} would you like to order? ")

            if quantity.isdigit():
                quantity = int(quantity)
            else:
                print("Invalid quantity input, defaulting to 1.")
                quantity = 1

            order.append({
                "Item name": item_name,
                "Price": item_price,
                "Quantity": quantity
            })
            return order
        else:
            print("That menu selection is not valid.")
            return order
    else:
        print("Please enter a valid menu item number.")
        return order

def print_itemized_receipt(receipt):
    """
    Prints an itemized receipt for the customer.

    Parameters:
    receipt (list): A list of dictionaries containing the menu item name, price,
                    and quantity ordered.
    """
    for item in receipt:
        item_name = item["Item name"]
        price = item["Price"]
        quantity = item["Quantity"]
        print_receipt_line(item_name, price, quantity)

##################################################
#  STARTER CODE
#  Do not modify any of the code below this line:
##################################################

def print_receipt_line(item_name, price, quantity):
    """
    Prints a line of the receipt.

    Parameters:
    item_name (str): The name of the meal item.
    price (float): The price of the meal item.
    quantity (int): The quantity of the meal item.
    """
    num_item_spaces = 32 - len(item_name)
    num_price_spaces = 6 - len(str(price))
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

def print_receipt_heading():
    """
    Prints the receipt heading.
    """
    print("----------------------------------------------------")
    print("Item name                       | Price  | Quantity")
    print("--------------------------------|--------|----------")

def print_receipt_footer(total_price):
    """
    Prints the receipt footer with the total price of the order.

    Parameters:
    total_price (float): The total price of the order.
    """
    print("----------------------------------------------------")
    print(f"Total price: ${total_price:.2f}")
    print("----------------------------------------------------")

def print_menu_heading():
    """
    Prints the menu heading.
    """
    print("--------------------------------------------------")
    print("Item # | Item name                        | Price")
    print("-------|----------------------------------|-------")

def print_menu_line(index, food_category, meal, price):
    """
    Prints a line of the menu.

    Parameters:
    index (int): The menu item number.
    food_category (str): The category of the food item.
    meal (str): The name of the meal item.
    price (float): The price of the meal item.
    """
    num_item_spaces = 32 - len(food_category + meal) - 3
    item_spaces = " " * num_item_spaces
    if index < 10:
        i_spaces = " " * 6
    else:
        i_spaces = " " * 5
    print(f"{index}{i_spaces}| {food_category} - {meal}{item_spaces} | ${price}")

def get_menu_items_dict(menu):
    """
    Creates a dictionary of menu items and their prices mapped to their menu 
    number.

    Parameters:
    menu (dictionary): A nested dictionary containing the menu items and their
                        prices.

    Returns:
    menu_items (dictionary): A dictionary containing the menu items and their
                            prices.
    """
    menu_items = {}
    i = 1

    for food_category, options in menu.items():
        for meal, price in options.items():
            menu_items[i] = {
                "Item name": food_category + " - " + meal,
                "Price": price
            }
            i += 1

    return menu_items

def get_menu_dictionary():
    """
    Returns a dictionary of menu items and their prices.

    Returns:
    meals (dictionary): A nested dictionary containing the menu items and their
                        prices in the following format:
                        {
                            "Food category": {
                                "Meal": price
                            }
                        }
    """
    meals = {
        "Burrito": {
            "Chicken": 4.49,
            "Beef": 5.49,
            "Vegetarian": 3.99
        },
        "Rice Bowl": {
            "Teriyaki Chicken": 9.99,
            "Sweet and Sour Pork": 8.99
        },
        "Sushi": {
            "California Roll": 7.49,
            "Spicy Tuna Roll": 8.49
        },
        "Noodles": {
            "Pad Thai": 6.99,
            "Lo Mein": 7.99,
            "Mee Goreng": 8.99
        },
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    }
    return meals

# Run the program
if __name__ == "__main__":
    # Get the menu dictionary
    meals = get_menu_dictionary()

    # Example predefined inputs for testing
    predefined_inputs = [
        "1",  # Select the first menu item
        "2",  # Select the second menu item
        "n"   # Indicate no more orders
    ]

    receipt, total_price = place_order(meals, predefined_inputs)

    print("This is what we are preparing for you.\n")
    print_receipt_heading()
    print_itemized_receipt(receipt)
    print_receipt_footer(total_price)
