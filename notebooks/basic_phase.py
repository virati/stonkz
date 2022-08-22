# %%
import yfinance as yf

nasdq = yf.Ticker("NDX").history(period="1y", interval="1d", actions=False)
sp = yf.Ticker("^GSPC").history(period="1y", interval="1d", action=False)


import matplotlib.pyplot as plt

plt.plot(nasdq["Close"])
plt.plot(sp["Close"])

plt.show()
