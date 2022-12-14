import numpy as np
import pandas as pd

import yfinance as yf

import plotly.graph_objs as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

comp1 = yf.download(tickers='FB', period='10d',interval='15m')
comp2 = yf.download(tickers='AMZN', period='10d', interval='15m')
comp3 = yf.download(tickers='TSLA',period='10d',interval='15m')

healthcare = yf.download(tickers='VHT', period='10d', interval='15m')

chealthcare = yf.Ticker('VHT')
vht_df = chealthcare.history(period='5y')

plt.figure()
plt.plot(vht_df)

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(comp1,comp2,comp3)
plt.show()
