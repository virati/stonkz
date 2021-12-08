import yfinance as yf
import matplotlib.pyplot as plt

msft = yf.Ticker("MSFT")

msft_rechist = msft.history(period="5d")
msft_bighist = msft.history(period="30d")

plt.figure()
plt.plot(msft_rechist["Close"])

plt.figure()
plt.plot(msft_bighist["Close"])

plt.show()
