# Module 10 - Python Lists
#
# Reflection 1:
# The most surprising thing about lists is that I can change
# them by adding, removing, or sorting items. I also learned
# that negative indices make it easy to find items at the end.
#
# Reflection 2:
# In an accounting class, Python lists could help me organize
# sales amounts and calculate totals and averages. This would
# save time compared to entering everything into Excel manually.

# Exercise 1 - Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print("Exercise 1")
print(inventory)
print(len(inventory))

# Exercise 2 - Index practice
print("\nExercise 2")
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3 - Slicing
print("\nExercise 3")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4 - Modify
print("\nExercise 4")
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5 - Tuple comparison
print("\nExercise 5")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed after they are created.")
    print("This is useful for keeping coordinates the same.")

print(coords)

# Exercise 6 - Average sales
print("\nExercise 6")
sales = [100, 250, 75, 480, 200]

print("Total:", sum(sales))
print("Count:", len(sales))
print("Average:", sum(sales) / len(sales))
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7 - Accumulator pattern
print("\nExercise 7")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted.append(new_price)

print("Original:", prices)
print("Discounted:", discounted)

# Exercise 8 - Filter above threshold
print("\nExercise 8")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))
