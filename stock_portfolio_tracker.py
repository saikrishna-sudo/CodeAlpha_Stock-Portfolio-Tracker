import yfinance as yf
import pandas as pd

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        if ticker in self.portfolio:
            self.portfolio[ticker] += shares
        else:
            self.portfolio[ticker] = shares
        print(f"Added {shares} shares of {ticker} to the portfolio.")

    def remove_stock(self, ticker, shares):
        if ticker in self.portfolio:
            if self.portfolio[ticker] > shares:
                self.portfolio[ticker] -= shares
                print(f"Removed {shares} shares of {ticker} from the portfolio.")
            elif self.portfolio[ticker] == shares:
                del self.portfolio[ticker]
                print(f"Removed all shares of {ticker} from the portfolio.")
            else:
                print(f"Cannot remove {shares} shares of {ticker} as you only have {self.portfolio[ticker]} shares.")
        else:
            print(f"{ticker} is not in the portfolio.")

    def fetch_real_time_data(self):
        if not self.portfolio:
            print("Portfolio is empty.")
            return

        print("\nFetching real-time data...")
        data = yf.download(list(self.portfolio.keys()), period="1d")
        current_prices = data['Close'].iloc[-1]

        print("\nPortfolio Performance:")
        for ticker, shares in self.portfolio.items():
            current_price = current_prices[ticker]
            total_value = current_price * shares
            print(f"{ticker}: {shares} shares at ${current_price:.2f} each, total value = ${total_value:.2f}")

    def show_portfolio(self):
        if not self.portfolio:
            print("Portfolio is empty.")
            return

        print("\nCurrent Portfolio:")
        for ticker, shares in self.portfolio.items():
            print(f"{ticker}: {shares} shares")

def main():
    portfolio = StockPortfolio()
    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Show Portfolio")
        print("4. Fetch Real-Time Data")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            ticker = input("Enter the stock ticker: ").upper()
            shares = int(input("Enter the number of shares: "))
            portfolio.add_stock(ticker, shares)
        elif choice == '2':
            ticker = input("Enter the stock ticker: ").upper()
            shares = int(input("Enter the number of shares: "))
            portfolio.remove_stock(ticker, shares)
        elif choice == '3':
            portfolio.show_portfolio()
        elif choice == '4':
            portfolio.fetch_real_time_data()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
