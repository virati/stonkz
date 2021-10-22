import numpy as np
import pandas as pd

import yfinance as yf

import plotly.graph_objs as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

comp1 = yf.download(tickers='FB', period='5d',interval='5m')
comp2 = yf.download(tickers='AMZN', period='5d', interval='5m')
comp3 = yf.download(tickers='TSLA',period='5d',interval='5m')

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(comp1,comp2,comp3)
plt.show()
