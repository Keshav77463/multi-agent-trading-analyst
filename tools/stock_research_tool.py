import yfinance as yf
from crewai.tools import tool

def get_stock_price(stock_symbol: str)->str:
    stock=yf.Ticker(stock_symbol)
    info=stock.info
    current_price=info.get('regularMarketPrice')
    change=info.get('regularMarketChange')
    change_percent=info.get('regularMarketChangePercent')
    currency=info.get('currency','USD')
    if current_price==None:
        return f"could not fetch {stock_symbol}.please check the symbol"
    return(
        f"stock: {stock_symbol}\n"
        f"current price: {current_price}\n"
        f"change: {change}\n"

    )

