import yfinance as yf
from crewai.tools import tool


@tool("live stock research tool")
def get_stock_price(stock_symbol: str) -> str:
    """Fetch the current stock price and market change for a given stock symbol."""

    stock = yf.Ticker(stock_symbol)
    info = stock.info

    current_price = info.get("regularMarketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency = info.get("currency", "USD")

    if current_price is None:
        return f"Could not fetch {stock_symbol}. Please check the symbol."

    return (
        f"Stock: {stock_symbol}\n"
        f"Current Price: {current_price} {currency}\n"
        f"Change: {change}\n"
        f"Change Percent: {change_percent}%"
    )
