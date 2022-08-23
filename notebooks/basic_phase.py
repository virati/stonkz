# %%
import yfinance as yf
from scipy.stats import zscore
import pandas as pd
import numpy as np


nasdq = yf.Ticker("NDX").history(period="1y", interval="1d", actions=False)
sp = yf.Ticker("^GSPC").history(period="1y", interval="1d", action=False)


import matplotlib.pyplot as plt

plt.plot(nasdq["Close"])
plt.plot(sp["Close"])

plt.show()


#%%

nasdq_sig = zscore(nasdq["Close"])
sp_sig = zscore(sp["Close"])

plt.plot(nasdq_sig, sp_sig)


#%%
sectors = {
    "IAK",
    "FCG",
    "XME",
    "XAR",
    "PEJ",
    "FTXG",
    "SMH",
    "PPH",
    "REZ",
    "EWCO",
    "JHMU",
}
timeseries = {key: [] for key in sectors}

for key in sectors:
    timeseries[key] = yf.Ticker(key).history(period="1y", interval="1d", actions=False)[
        "Close"
    ]
#%%
design_matrix = np.array([timeseries[key] for key in sectors])


#%%
nas_dif = np.diff(nasdq_sig)
sp_dif = np.diff(sp_sig)

plt.plot(nas_dif, sp_dif)

#%%
