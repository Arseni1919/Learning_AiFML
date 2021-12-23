import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
from pandas_datareader import data
import statistics as stats
import math as math


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




