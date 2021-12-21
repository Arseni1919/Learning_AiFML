import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
# loading the class data from the package pandas_datareader
from pandas_datareader import data


# First day
start_date = '2017-01-01'
# Last day
end_date = '2021-01-01'
# Call the function DataReader from the class data
goog_data = data.DataReader('GOOG', 'yahoo', start_date, end_date)

goog_data_signal = pd.DataFrame(index=goog_data.index)

# fig = px.line(goog_data, y=['Close', 'Open', 'High', 'Low'])
# fig.show()
print(goog_data.head())
# plt.plot(goog_data['Close'], label='close')
plt.plot(goog_data['Adj Close'], label='Adj Close')
# plt.plot(goog_data['Open'], label='Open')
# plt.plot(goog_data['High'], label='High')
# plt.plot(goog_data['Low'], label='Low')
plt.legend()
plt.show()