import sys
!{sys.executable} -m pip install yfinance
!{sys.executable} -m pip install prophet
!{sys.executable} -m pip install tensorflow

import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import re
import csv
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import datetime
import warnings
warnings.filterwarnings('ignore')

%matplotlib inline

from pandas import DataFrame

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV

from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

#from pmdarima import auto_arima
from prophet import Prophet
from prophet.plot import add_changepoints_to_plot

from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.graphics.gofplots import qqplot
#from statsmodels.tsa.arima.model import ARIMA
#from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.stats.diagnostic import acorr_ljungbox
from itertools import product
from tqdm.notebook import tqdm
from datetime import date, timedelta

msft_df = yf.download("MSFT", start="2010-01-01", end="2023-01-10")[['Adj Close','Open', 'High', 'Low', 'Close', 'Volume']].round(2)
msft_df.to_csv("microsoft_data.csv")

msft_df

msft_df['Adj Close'].plot(grid = True)
sns.set(rc={'figure.figsize':(15, 9)})
plt.title('Giá đóng cửa điều chỉnh của Microsoft', color = 'black', fontsize = 20)
plt.xlabel('Năm', color = 'black', fontsize = 15)
plt.ylabel('Giá cổ phiếu', color = 'black', fontsize = 15)
msft_adj = msft_df[['Adj Close']]
msft_adj 
# Tạo split tỉ lệ 80%/20%

split = int(0.8*len(msft_adj))
# Chia thành train và test set

train, test = msft_adj[:split], msft_adj[split:]

msft_adj.shape, train.shape, test.shape
train.index.min(), train.index.max(), test.index.min(), test.index.max()

# Tạo dự đoán
preds = []
for i in range(0,656):
    a = train[len(train)-656+i:].sum() + sum(preds)
    b = a/656
    preds.append(b)






