stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300,
    "AMZN": 200
}

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))
price = stock_prices[stock_name]
investment = price * quantity

print("Total investment:", investment)