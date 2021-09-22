fruits = ["Banana", "Strawberry", "Apple", "Grape"]
wanted_fruit = "Watermelon"

for index in range(2):
    if wanted_fruit in fruits:
        print(f"Found '{wanted_fruit}' in the position {fruits.index(wanted_fruit)} of the fruits list")
    else:
        print(f"Sorry, '{wanted_fruit}' is not in the fruits list")
    wanted_fruit = "Apple"