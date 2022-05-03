import alpaca_trade_api as tradeapi
import numpy as np
import time
SEC_KEY = 'CKHS4IFN8T007XT0BCL5'
PUB_KEY = '4ZT2pibTA9T9RUTWq9sOYVYgkIM0tJ7skfdI5map'
BASE_URL = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key_id = PUB_KEY, secret_key = SEC_KEY, base_url = BASE_URL)


#buy stock
api.submit_order(
    symbol='SPY',
    qty=1,
    side='buy',
    type='market',
    time_in_force='gtc'
)

#sell stock
api.submit_order(
    symbol='SPY',
    qty=1,
    side='sell',
    type='market',
    time_in_force='gtc'
)