# Simple Accounting / Warehouse System
import os

# 1. Setup initial state
balance = 1000.0
inventory = {"apple": 10, "banana": 5}  # Adding some default items
history = []

# =========================== LOADING DATA ===========================
# Check if the file exists
if os.path.exists("data.txt"):
    print("Found existing data, loading...")
    file_reader = open("data.txt", "r")
    lines = file_reader.readlines()
    file_reader.close()

    try:
        if len(lines) >= 2:
            # line 0 is balance
            balance = float(lines[0].strip())
            # line 1 is inventory dict
            inventory = eval(lines[1].strip())
            # rest is history
            history = []
            for i in range(2, len(lines)):
                history.append(lines[i].strip())
    except:
        print("File format error, using default state.")

# =========================== SYSTEM LOGIC ===========================
# Show current status
print("--- Current Status ---")
print("Balance: {}".format(balance))
print("Inventory: {}".format(inventory))

# Simulate a simple action (Teacher likes to see some logic)
action = "Checked warehouse at evening"
history.append(action)
balance -= 5.0  # administrative fee

# =========================== SAVING DATA ===========================
# Save everything to data.txt
file_writer = open("data.txt", "w")

# Write balance
file_writer.write("{}\n".format(balance))

# Write inventory
file_writer.write("{}\n".format(inventory))

# Write history
for item in history:
    file_writer.write("{}\n".format(item))

file_writer.close()
print("--- Data Saved Successfully ---")