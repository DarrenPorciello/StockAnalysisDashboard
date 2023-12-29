# Stock Dashboard using Streamlit

This is a stock dashboard web application created using Python and Streamlit. The dashboard allows users to visualize stock price movements, explore fundamental data, and read the top news related to a specified stock.

## Getting Started

Make sure you have the required Python packages installed. You can install them using the following command:

```bash
pip install streamlit pandas yfinance plotly alpha_vantage numpy python-dotenv stocknews
```

Additionally, create a `.env` file in the project's root directory and add your Alpha Vantage API key:

```env
API_KEY=your_alpha_vantage_api_key_here
```

## Running the Dashboard

Run the Streamlit app using the following command:

```bash
streamlit run your_script_name.py
```

Replace `your_script_name.py` with the name of the Python script containing the provided code.

## Features

### Stock Price Visualization

- Enter a stock ticker in the sidebar to visualize its adjusted close price over a specified date range.
- Use the date picker to set the start and end dates for the stock price data.

### Pricing Data

- View price movements, percentage change, annual return, standard deviation, and risk-adjusted return.

### Fundamental Data

- Explore fundamental data including balance sheet, income statement, and cash flow statement.

### Top News

- Read the top 10 news articles related to the specified stock.
- Each article includes the publication date, title, summary, title sentiment, and news sentiment.

## Note

- Ensure your Alpha Vantage API key is stored securely in the `.env` file to access fundamental data.
- The `.env` file is included in the `.gitignore` file to prevent accidental exposure of sensitive information.

Feel free to customize and extend the code according to your needs. Happy exploring!
