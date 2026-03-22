class Manager:
    def __init__(self):
        self.balance = 0
        self.operations = {}

    # Decorator to register operations
    def operation(self, name):
        def decorator(func):
            self.operations[name] = func
            return func
        return decorator

    # Assign method
    def assign(self, task, *args):
        if task not in self.operations:
            print(f"Error: Unknown task '{task}'")
            return
        return self.operations[task](self, *args)


# Create manager instance
manager = Manager()


# Define operations using decorators
@manager.operation("sale")
def sale(self, amount):
    self.balance += amount
    print(f"Sale: +{amount}, Balance: {self.balance}")


@manager.operation("purchase")
def purchase(self, amount):
    self.balance -= amount
    print(f"Purchase: -{amount}, Balance: {self.balance}")


@manager.operation("balance")
def check_balance(self):
    print(f"Current balance: {self.balance}")
    return self.balance


@manager.operation("history")
def history(self):
    print("Operations available:", list(self.operations.keys()))