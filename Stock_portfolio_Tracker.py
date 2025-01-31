portfolio = {
    "AAPL": {"quantity": 10, "purchase_price": 150},
    "TSLA": {"quantity": 5, "purchase_price": 700},
}
import yfinance as yf

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    return data['Close'][0]
def add_stock_to_portfolio(portfolio, symbol, quantity, purchase_price):
    if symbol in portfolio:
        portfolio[symbol]['quantity'] += quantity
    else:
        portfolio[symbol] = {'quantity': quantity, 'purchase_price': purchase_price}
    print(f"Added {quantity} shares of {symbol} to the portfolio.")
def remove_stock_from_portfolio(portfolio, symbol, quantity):
    if symbol in portfolio:
        if portfolio[symbol]['quantity'] >= quantity:
            portfolio[symbol]['quantity'] -= quantity
            if portfolio[symbol]['quantity'] == 0:
                del portfolio[symbol]
            print(f"Removed {quantity} shares of {symbol} from the portfolio.")
        else:
            print(f"Not enough shares of {symbol} to remove.")
    else:
        print(f"Stock {symbol} not found in portfolio.")
def track_portfolio_performance(portfolio):
    total_investment = 0
    current_value = 0
    for symbol, data in portfolio.items():
        current_price = get_stock_price(symbol)
        current_value += current_price * data['quantity']
        total_investment += data['purchase_price'] * data['quantity']
        print(f"{symbol}: Purchased at ${data['purchase_price']}, Current price: ${current_price}, Shares: {data['quantity']}")
    
    print(f"Total investment: ${total_investment:.2f}")
    print(f"Current value of portfolio: ${current_value:.2f}")
    print(f"Overall portfolio gain/loss: ${current_value - total_investment:.2f}")
import yfinance as yf

# Define the portfolio
portfolio = {}

# Function to get stock price
def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="1d")
    return data['Close'][0]

# Function to add stock to portfolio
def add_stock_to_portfolio(portfolio, symbol, quantity, purchase_price):
    if symbol in portfolio:
        portfolio[symbol]['quantity'] += quantity
    else:
        portfolio[symbol] = {'quantity': quantity, 'purchase_price': purchase_price}
    print(f"Added {quantity} shares of {symbol} to the portfolio.")

# Function to remove stock from portfolio
def remove_stock_from_portfolio(portfolio, symbol, quantity):
    if symbol in portfolio:
        if portfolio[symbol]['quantity'] >= quantity:
            portfolio[symbol]['quantity'] -= quantity
            if portfolio[symbol]['quantity'] == 0:
                del portfolio[symbol]
            print(f"Removed {quantity} shares of {symbol} from the portfolio.")
        else:
            print(f"Not enough shares of {symbol} to remove.")
    else:
        print(f"Stock {symbol} not found in portfolio.")

# Function to track portfolio performance
def track_portfolio_performance(portfolio):
    total_investment = 0
    current_value = 0
    for symbol, data in portfolio.items():
        current_price = get_stock_price(symbol)
        current_value += current_price * data['quantity']
        total_investment += data['purchase_price'] * data['quantity']
        print(f"{symbol}: Purchased at ${data['purchase_price']}, Current price: ${current_price}, Shares: {data['quantity']}")
    
    print(f"Total investment: ${total_investment:.2f}")
    print(f"Current value of portfolio: ${current_value:.2f}")
    print(f"Overall portfolio gain/loss: ${current_value - total_investment:.2f}")

# Example usage
add_stock_to_portfolio(portfolio, "AAPL", 10, 150)
add_stock_to_portfolio(portfolio, "TSLA", 5, 700)
remove_stock_from_portfolio(portfolio, "TSLA", 2)
track_portfolio_performance(portfolio)
