# module-21-challenge

# Overview
The Restaurant Order System is a Python-based application designed to streamline the process of placing orders at a takeout restaurant. This system allows customers to view a menu, place their orders, and receive an itemized receipt without the need for direct interaction with staff, making it a perfect fit for customers with hearing and vocal impairments.

# Features
Menu Display: Dynamically displays all menu items along with their categories, names, and prices.
Order Placement: Allows customers to select menu items, specify quantities, and view a summary of their orders.
Itemized Receipt: Provides an itemized receipt with the total order price at the end of the transaction.
Error Handling: Gracefully handles invalid inputs and provides user-friendly feedback.

# Technologies Used
Python: The primary programming language used to implement the application.
Console Input/Output: Utilizes terminal input and output for user interaction.
Getting Started
Prerequisites
Python 3.x installed on your local machine.

# Installation
- Clone the repository:

bash
git clone https://github.com/jacobmenlove/module-21-challenge
cd Develop

# Run the application: 

- You can run the program by executing the following command in the terminal:

bash
python order_system.py

# Usage

- Upon launching the application, the user is welcomed and presented with the restaurant's menu.
- The user can input the number corresponding to the menu item they wish to order.
- After selecting an item, the user will be prompted to specify the quantity.
- The user can continue adding items or choose to finalize their order.
- Once the order is complete, an itemized receipt is displayed, showing each item, its price, and the total cost.

- Example Inputs
Selecting a menu item:

Please enter the number of the item you want to order: 

Specifying a quantity:

How many of Burrito - Chicken would you like to order? 

Choosing to finish ordering:

Would you like to order anything else? (y/n): n

# Testing
The application can be tested using predefined inputs to simulate user interaction. This is useful for unit tests or continuous integration environments.

# Running Tests

- Ensure to set up the testing framework (e.g., unittest) as needed. Run the tests using the following command:

bash
python -m unittest test_order_system.py

# Contributing
Contributions are welcome! Please submit a pull request or open an issue if you have suggestions for improvements or encounter any bugs.