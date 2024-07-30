from ib_insync import *
import pandas as pd
import matplotlib.pyplot as plt

ib = IB()
ib.connect('92.154.106.15', 7496, clientId=26)

tickers = ['ADP']
for ticker in tickers:
    contract = Stock(ticker, 'SMART', 'USD')

    ib.reqMktData(contract)
    ib.sleep(1)
    market_data = ib.reqMktData(contract)
    print(market_data.last)
    bars = ib.reqHistoricalData(
        contract,
        endDateTime='',
        durationStr='5 D',
        barSizeSetting='30 mins',
        whatToShow='MIDPOINT',
        useRTH=True,
        formatDate=1
    )


    df = util.df(bars)
    print(df)
    fig = plt.figure(figsize=(10, 7))
    plt.plot([], [], ' ')
    plt.title(
       f'IETE : {ticker} {market_data.last}',
       fontweight="bold", color='black')
    df['close'].plot(color=['blue'], label='Clotures')
    plt.show()

ib.disconnect()
