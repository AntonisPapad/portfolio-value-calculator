
# Cryptocurrency Portfolio Valuation

## Overview
This script calculates the total value of a cryptocurrency portfolio. It reads the amounts of various crypto tokens from a CSV file (`port.csv`), fetches the current prices for those tokens using the CoinMarketCap API, and then computes and stores the portfolio's total value along with the current date and time in a CSV file (`portfolio_value.csv`).

## Features
- **Fetch Token Amounts**: Reads token symbols and their respective amounts from a CSV file.
- **Fetch Current Prices**: Retrieves the latest prices of specified tokens using the CoinMarketCap API.
- **Calculate Portfolio Value**: Computes the total value of the portfolio by multiplying token amounts by their current prices.
- **Store and Display Results**: Outputs the total portfolio value in the console and appends it to a CSV file along with the current date and time.
- **Error Handling**: Tokens not recognized by the CoinMarketCap API are ignored and excluded from the final portfolio value calculation.

## Requirements
- Python 3.x
- `requests` library (for API calls)

## Installation
1. **Clone the repository** or copy the script file to your local machine.

2. **Install the necessary Python packages**:
   ```bash
   pip install requests
   ```

3. **Set up your API key**:
   Create a `config.py` file in the same directory as the script with the following content:
   ```python
   COINMARKETCAP_API_KEY = 'your_api_key_here'
   ```

## Usage
1. **Prepare your `port.csv` file**:
   - The file should contain two columns: the token symbol and its amount. 
   - Example:
     ```
     BTC,0.5
     ETH,2.0
     ```

2. **Run the script**:
   - Execute the script using Python:
     ```bash
     python port_value.py
     ```
   - The script will output the value of each token and the total portfolio value to the console.

3. **Check the results**:
   - The total portfolio value along with the current date and time will be appended to a CSV file named `portfolio_value.csv` in the same directory.

## Example
Here's an example of how the script operates:
- **Input (`port.csv`)**:
  ```
  BTC,0.5
  ETH,2.0
  ```
- **Output (Console)**:
  ```
  BTC:     25000.00
  ETH:      5000.00
  Total Portfolio Value: $30000.00
  ```
- **Output (`portfolio_value.csv`)**:
  ```
  Date and Time,Total Portfolio Value
  2024-08-27 14:55,30000.00
  ```

## Notes
- Ensure that your `port.csv` file is correctly formatted and your API key is valid.
- The program assumes all token prices are in USD.
- If a token is not recognized by the API, it will be excluded from the final portfolio value calculation, and a warning will be printed.
