import csv
import requests
from datetime import datetime
from config import COINMARKETCAP_API_KEY

def fetch_token_amounts(csv_file_path):
    """Fetches amounts of crypto tokens from a CSV file."""
    token_amounts = {}
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            token_symbol, amount = row
            token_amounts[token_symbol] = float(amount)
    return token_amounts

def fetch_token_prices(api_key, tokens):
    """Fetches current prices for specified tokens using the CoinMarketCap API."""
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    parameters = {'symbol': ','.join(tokens)}
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    
    token_prices = {}
    for token in tokens:
        if token in data['data']:
            token_prices[token] = data['data'][token]['quote']['USD']['price']
        else:
            print(f"Warning: {token} not recognized by CoinMarketCap API and will be excluded from the portfolio value calculation.")
    
    return token_prices

def calculate_portfolio_value(token_amounts, token_prices):
    """Calculates the total value of the portfolio."""
    return sum(amount * token_prices[token] for token, amount in token_amounts.items() if token in token_prices)

def print_token_values(token_amounts, token_prices):
    """Prints each token's value in the portfolio."""
    for token, amount in token_amounts.items():
        if token in token_prices:
            value = amount * token_prices[token]
            print(f"{token}: {value:10.2f}")

def store_portfolio_value(file_path, portfolio_value):
    """Stores the total portfolio value and the date in a CSV file."""
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M'), portfolio_value])
        

def main():
    input_csv_file_path = 'port.csv'
    output_csv_file_path = 'portfolio_value.csv'
    
    # Fetch token amounts
    token_amounts = fetch_token_amounts(input_csv_file_path)
    
    # Fetch token prices
    token_prices = fetch_token_prices(COINMARKETCAP_API_KEY, list(token_amounts.keys()))
    
    # Print each token's value
    print_token_values(token_amounts, token_prices)
    
    # Calculate portfolio value
    portfolio_value = calculate_portfolio_value(token_amounts, token_prices)
    
    # Print and store the total portfolio value
    print(f"Total Portfolio Value: ${portfolio_value:.2f}")
    store_portfolio_value(output_csv_file_path, portfolio_value)

if __name__ == "__main__":
    main()