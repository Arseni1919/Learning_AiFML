import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
from pandas_datareader import data
import statistics as stats
import math as math
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

# First day
start_date = '2014-01-01'
# Last day
end_date = '2018-01-01'
SRC_DATA_FILENAME = 'data/goog_data.csv'

try:
    goog_data2 = pd.read_csv(SRC_DATA_FILENAME)
    print('loaded')
except FileNotFoundError:
    print('loading...')
    goog_data2 = data.DataReader('GOOG', 'yahoo', start_date, end_date)
    goog_data2.to_csv(SRC_DATA_FILENAME)




