# Burgers to Go - Midterm Project
# Student Name: Joseph Santos
# Date: 7/19/2026

# 1. Welcome message
print("Welcome to Burgers to Go!")

# Toppings prices
TOPPINGS = {
    "lettuce": 0.50,
    "tomato": 0.50,
    "cheese": 1.00,
    "onion": 0.50,
    "pickles": 0.50,
    "double meat": 5.50,
    "avocado": 1.25
}
# Burger price
BURGER_PRICE = 10.30

# list of toppings names (conversion of dictionary to list)
toppings_list = list(TOPPINGS.keys())

# takes a list and prints each item with a number for customer to view
def display_toppings(toppings):
    for i in range(len(toppings)):
        print(str(i + 1) + ". " + toppings[i])


# ask user to pick a number and return a topping choose
def get_choice(toppings):
    display_toppings(toppings)
    choice = input("Enter a Number: ")

    while choice not in ("1", "2", "3", "4", "5", "6", "7"):
        choice = input("Not valid, please try again: ")

    index = int(choice) - 1
    return toppings[index]


# this adds the cost of one burger at base price then plus all its toppings
def get_burger_cost(burger):
    cost = BURGER_PRICE
    for topping in burger["toppings"]:
        cost = cost + TOPPINGS[topping]
    return cost


# this prints out the whole receipt for all the burgers ordered including toppings
def print_receipt(burgers):
    """ Prints out the receipt for the order of burgers"""
    total = 0
    print("RECEIPT")
    for burger in burgers:
        print()
        print(f"{burger["name"]:<15} ${BURGER_PRICE:.2f}")
        if len(burger["toppings"]) < 1:
            print(f"- {"no toppings":<13} ${0:.2f}")
        else:
            for topping in burger["toppings"]:
                print(f"- {topping:<13} ${TOPPINGS[topping]:.2f}")
        subtotal = get_burger_cost(burger)
        total += subtotal
        print(f"{"subtotal":<15} ${subtotal:.2f}")
    print("------------------------")
    print(f"{"TOTAL":<15} ${total:.2f}")


# ask how many burgers they want first
num_burgers = input("How many burgers would you like? ")
num_burgers = int(num_burgers)

# this is where we store every burger ordered
burgers = []

# loop once for EACH burger the customer wants
for i in range(num_burgers):
    chosen_toppings = []

    print("\nBuilding Hamburger " + str(i + 1))
    adding = input("Do you want to add a topping? (yes/no): ")

    while adding == "yes":
        topping = get_choice(toppings_list)
        chosen_toppings.append(topping)
        adding = input("Do you want to add another topping? (yes/no): ")

    burger = {
        "name": "Hamburger " + str(i + 1),
        "toppings": chosen_toppings
    }
    burgers.append(burger)

# print the final receipt
print_receipt(burgers)
