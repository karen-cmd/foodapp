class Budget():
    def __init__(self,food,clothing,entertainment):
        self.food=food
        self.clothing=clothing
        self.entertainment=entertainment

food = Budget("food")
food.deposit(400, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "mocktails and cocktails")
print(food.get_balance())
clothing = Budget("Clothing")
food.transfer(20, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
entertainment= Budget("entertainment")
entertainment.deposit(500, "initial deposit")
entertainment.withdraw(15)

print(food)
print(clothing)
print(entertainment)