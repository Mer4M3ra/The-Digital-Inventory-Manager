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
    


class inventory:
    def __init__(self):
        self.products = {}