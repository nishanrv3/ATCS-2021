# Nishan Rajavasireddy
# trading bot
# May 10, 2022

import alpaca_trade_api as tradeapi
import numpy as np
import time

api = tradeapi.REST(key_id='4ZT2pibTA9T9RUTWq9sOYVYgkIM0tJ7skfdI5map', secret_key='CKHS4IFN8T007XT0BCL5',
                    base_url='https://paper-api.alpaca.markets')

# buy stock
api.submit_order(
    symbol='TSLA',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc'
)

# sell stock
api.submit_order(
    symbol='TSLA',
    qty=1,
    side='sell',
    type='market',
    time_in_force='gtc'
)

symbol = "SPY"
position_held = False

# trading strategy
while True:
    print("")
    print("Checking Price")

    market_data = api.get_barset(symbol, 'minute', limit=5)

    closing_prices = []
    for bar in market_data[symbol]:
        closing_prices.append(bar.c)

    closing_prices = np.array(closing_prices, dtype=np.float64)
    mean = np.mean(closing_prices)
    last_price = closing_prices[4]
    print("Mean: " + str(mean))
    print("Last Price: " + str(last_price))

    if mean + 0.1 < last_price and not position_held:
        print("Buy")
        api.submit_order(
            symbol= 'TSLA',
            qty=1,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
        position_held = True
    elif mean - 0.1 > last_price and position_held:
        print("Sell")
        api.submit_order(
            symbol= 'TSLA',
            qty=1,
            side='sell',
            type='market',
            time_in_force='gtc'
        )
        position_held = False

    time.sleep(60)
