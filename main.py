class product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
    def update_stock(self, amount):
        self.amount = amount
        if amount < 0:
            amount = 1
        Stock = int(input("Are you going to add or remove stock count?(1 for add and 2 for remove)"))
        if Stock == 1:
            AddAmount = int(input("How much stock are you going to add"))
            if AddAmount >= 0:
                amount = amount + AddAmount
        elif Stock == 2:
            ReduceAmount = int(input("How much stock are you going to remove"))
            if ReduceAmount >= 0:
                amount = amount - ReduceAmount
        else:
            print("Please enter 1 or 2")

    def get_total_value(self, quantity, price):
        TotalValue = quantity * price
        return TotalValue




    def __str__(self):
        return f"{self.product_id} | {self.name} | ${self.price} | {self.quantity}"
    


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    def display_all(self):
        return f"{self.products}"

def Start():
    print("Welcome to the inventory manager")
    while True:
        print("/n 1. Add new product")
        print("/n 2. View stock")
        print("/n 3. Update stock")
        print("/n 4. Exit")
        Choice = input("What option woulod you like to choose")
        if Choice == 1:
            Inventory.add_product()

if __name__ == "__main__":
# runs the main file
    Start()