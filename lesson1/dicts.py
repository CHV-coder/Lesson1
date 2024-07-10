from pprint import pprint

stock = [
    {'name': 'iPhone', 'price': 2000},
    {'name': 'Samsung', 'price': 1500, 'discount': 5},
    {'name': 'Xiami', 'price': 3000}
]

stock[0]["price"] = stock[0]["price"] - 200
pprint(stock)