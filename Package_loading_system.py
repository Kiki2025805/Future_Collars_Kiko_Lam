# Part 1: Get user input for max items
max_items = int(input("Enter the maximum number of items to be shipped: "))

# Initialize tracking variables
packages_sent = 0
total_weight_all = 0
current_pkg_weight = 0
items_processed = 0

# Variables for unused capacity
max_unused = -1
worst_package_num = 0

# Part 2 & 3: Loop for adding items
while items_processed < max_items:
    user_input = input("Enter item weight (1-10 kg, or 0 to exit): ")
    weight = int(user_input)

    # Part 4: Termination if weight is 0
    if weight == 0:
        print("System stopped by user.")
        break

    # Error handling for weight range
    if weight < 1 or weight > 10:
        print("Invalid weight! Please enter between 1 and 10.")
        continue

    # Part 3: Check if adding weight exceeds 20kg
    if current_pkg_weight + weight > 20:
        # Send the current package
        packages_sent += 1
        total_weight_all += current_pkg_weight

        # Calculate unused capacity for the package just sent
        unused = 20 - current_pkg_weight
        if unused > max_unused:
            max_unused = unused
            worst_package_num = packages_sent

        # Current item starts a new package
        current_pkg_weight = weight
    else:
        # Keep adding to the current package
        current_pkg_weight += weight

    items_processed += 1

# Handle the very last package if it's not empty
if current_pkg_weight > 0:
    packages_sent += 1
    total_weight_all += current_pkg_weight
    unused = 20 - current_pkg_weight
    if unused > max_unused:
        max_unused = unused
        worst_package_num = packages_sent

# Part 5: Display Results
total_unused_capacity = (packages_sent * 20) - total_weight_all

print("\n--- RESULTS ---")
print("Number of packages sent:", packages_sent)
print("Total weight of packages sent:", total_weight_all, "kg")
print("Total unused capacity:", total_unused_capacity, "kg")
print("Package with most unused capacity: Package #", worst_package_num)
print("Unused capacity in that package:", max_unused, "kg")
