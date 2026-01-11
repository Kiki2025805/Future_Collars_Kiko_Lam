# Starting data
bal = 0.0
stock = {}  # {name: [price, quantity]}
logs = []  # To save every action for review

while True:
    print("\nCommands: balance, sale, purchase, account, list, warehouse, review, end")
    cmd = input("What do you want to do? ").lower()

    if cmd == "end":
        print("Bye!")
        break

    elif cmd == "balance":
        val = float(input("Enter amount (use minus to subtract): "))
        bal = bal + val
        logs.append(f"Balance updated by {val}")

    elif cmd == "sale":
        name = input("Product name: ")
        price = float(input("Selling price: "))
        amount = int(input("Quantity: "))

        # Check if we have enough
        if name in stock and stock[name][1] >= amount:
            stock[name][1] -= amount
            bal += price * amount
            logs.append(f"Sold {amount} of {name}")
        else:
            print("We don't have enough items!")

    elif cmd == "purchase":
        name = input("Product name: ")
        price = float(input("Buying price: "))
        amount = int(input("Quantity: "))
        total_cost = price * amount

        if bal >= total_cost:
            bal -= total_cost
            if name in stock:
                stock[name][1] += amount
                stock[name][0] = price  # update price
            else:
                stock[name] = [price, amount]
            logs.append(f"Bought {amount} of {name}")
        else:
            print("Not enough money in account!")

    elif cmd == "account":
        print("Current money:", bal)

    elif cmd == "list":
        print("Current Inventory:")
        for key in stock:
            print(f"Item: {key}, Price: {stock[key][0]}, Qty: {stock[key][1]}")

    elif cmd == "warehouse":
        check_item = input("Which item? ")
        if check_item in stock:
            print(f"{check_item} - Price: {stock[check_item][0]}, Qty: {stock[check_item][1]}")
        else:
            print("Item not found.")

    elif cmd == "review":
        print(f"Total history entries: {len(logs)}")
        f_idx = input("From (index): ")
        t_idx = input("To (index): ")

        # If user leaves blank, use defaults
        start = int(f_idx) if f_idx != "" else 0
        end = int(t_idx) if t_idx != "" else len(logs)

        if start < 0 or end > len(logs):
            print("Wrong index range!")
        else:
            for i in range(start, end):
                print(f"Step {i}: {logs[i]}")

    else:
        print("Unknown command!")