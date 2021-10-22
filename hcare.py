import numpy as np
import pandas as pd

import yfinance as yf

import plotly.graph_objs as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

hcare_idxs = ['VHT','JNJ','MDT','PFE','UNH']

tsers = []
for ii in hcare_idxs:
	hcare = yf.Ticker(ii)
	tsers.append(hcare.history(period='5y'))

plt.figure()
[plt.plot(ts) for ts in tsers]

plt.figure()
plt.plot(tsers[0],tsers[1])

plt.show()

