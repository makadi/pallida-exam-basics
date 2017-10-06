# We run a Candy shop where we sell candies and lollipops
# One lollipop's price is 10$
# And it made from 5gr of sugar
# One candie's price is 20$
# And it made from 10gr of sugar
# we can raise their prices with a given percentage
#
# Create a CandyShop class
# It can store sugar and money as income. The constructor should take the amount of sugar in gramms.
# we can create lollipops and candies store them in the CandyShop's storage
# If we create a candie or lollipop the CandyShop's sugar amount gets reduced by the amount needed to create the sweets
# We can raise the prices of all candies and lollipops with a given percentage
# We can sell candie or lollipop with a given number as amount
# If we sell sweets the income will be increased by the price of the sweets and we delete it from the inventory
# We can buy sugar with a given number as amount. The price of 1000gr sugar is 100$
# If we buy sugar we can raise the CandyShop's amount of sugar and reduce the income by the price of it.
# The CandyShop should be represented as string in this format:
# "Inventory: 3 candies, 2 lollipops, Income: 100, Sugar: 400gr"


class CandyShop():
    def __init__(self, sugar_amount):
        self.sugar_amount = sugar_amount
        self.lollipop_sugar_amount = 5
        self.lollipop_price = 10
        self.candy_sugar_amount = 10
        self.candy_price = 20
        self.income = 0
        self.storage = []

    def create_sweets(self, sweet):
        if sweet is "lollipop":
            self.sugar_amount = self.sugar_amount - self.lollipop_sugar_amount
        if sweet is "candy":
            self.sugar_amount = self.sugar_amount - self.candy_sugar_amount
        self.storage.append(sweet)

    def raise_prices(self, percentage):
        self.lollipop_price += (self.lollipop_price * percentage / 100)
        self.candy_price += (self.candy_price * percentage / 100)

    def sell(self, sweet, number_of_sweets):
        if sweet is str("lollipop"):
            self.storage.remove("lollipop")
            self.income += self.lollipop_price * number_of_sweets
        if sweet is str("candy"):
            self.storage.remove("candy")
            self.income += self.candy_price * number_of_sweets

    def buy_sugar(self, bought_sugar_amount):
        self.sugar_price = bought_sugar_amount / 10
        self.income -= self.sugar_price
        self.sugar_amount += bought_sugar_amount

    def __repr__(self):
        return "Inventory: " + str(self.storage.count("candy")) + " candies, " + str(self.storage.count("lollipop")) + " lollipops, " + "Income: " + str(self.income) + ", Sugar: " + str(self.sugar_amount) + "gr"



candy_shop = CandyShop(300)
candy_shop.create_sweets("candy")
candy_shop.create_sweets("candy")
candy_shop.create_sweets("lollipop")
candy_shop.create_sweets("lollipop")
print(candy_shop)
# Should print out:
# Invetory: 2 candies, 2 lollipops, Income: 0, Sugar: 270gr
candy_shop.sell("candy", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 2 lollipops, Income:20, Sugar: 285gr"
candy_shop.raise_prices(5)
candy_shop.sell("lollipop", 1)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:35, Sugar: 285gr"
candy_shop.buy_sugar(300)
print(candy_shop)
# Should print out:
# "Invetory: 1 candies, 1 lollipops, Income:5, Sugar: 315gr"