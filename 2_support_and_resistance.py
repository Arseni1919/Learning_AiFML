import matplotlib.pyplot as plt

from GLOBALS import *

# First day
start_date = '2014-01-01'
# Last day
end_date = '2018-01-01'
SRC_DATA_FILENAME = 'data/goog_data.csv'

try:
    goog_data2 = pd.read_csv(SRC_DATA_FILENAME)
    print('loaded')
except FileNotFoundError:
    goog_data2 = data.DataReader('GOOG', 'yahoo', start_date, end_date)
    goog_data2.to_csv(SRC_DATA_FILENAME)

goog_data = goog_data2.tail(620)
lows = goog_data['Low']
highs = goog_data['High']
dates = goog_data['Date']

plt.plot(highs, color='c', lw=2., label='high')
plt.plot(lows, color='y', lw=2., label='low')
plt.hlines(highs.head(200).max(), lows.index.values[0], lows.index.values[-1], lw=2, color='g', label='resistance')
plt.hlines(lows.head(200).min(), lows.index.values[0], lows.index.values[-1], lw=2, color='r', label='support')
plt.axvline(x=lows.index.values[200], lw=2., color='b', linestyle=':')
plt.title('Google price')
plt.xlabel('Date')
# plt.xticks(dates.values)
plt.ylabel('$')
plt.legend()
plt.show()


