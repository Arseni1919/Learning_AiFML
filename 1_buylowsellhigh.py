from GLOBALS import *

# GETTING THE DATA
# First day
start_date = '2014-01-01'
# Last day
end_date = '2018-01-01'
# Call the function DataReader from the class data
goog_data = data.DataReader('GOOG', 'yahoo', start_date, end_date)

# BUILDING SIGNALS
goog_data_signal = pd.DataFrame(index=goog_data.index)
goog_data_signal['price'] = goog_data['Adj Close']
goog_data_signal['daily_difference'] = goog_data_signal['price'].diff()
goog_data_signal['signal'] = 0.0
goog_data_signal['signal'] = np.where(goog_data_signal['daily_difference'] > 0, 1.0, 0.0)
goog_data_signal['positions'] = goog_data_signal['signal'].diff()
print(goog_data_signal)
# print(goog_data_signal['signal'])
# plt.plot(goog_data_signal['daily_difference'], label='daily_difference')
plt.plot(goog_data_signal['price'], label='price', color='k', lw=2.)
plt.plot(goog_data_signal.loc[goog_data_signal.positions == 1.0].index,
         goog_data_signal.price[goog_data_signal.positions == 1.0], '^', markersize=5, color='g', label='buy')
plt.plot(goog_data_signal.loc[goog_data_signal.positions == -1.0].index,
         goog_data_signal.price[goog_data_signal.positions == -1.0], 'v', markersize=5, color='r', label='sell')
plt.legend()
plt.show()

# BACKTESTING
initial_capital = float(1000.0)
positions = pd.DataFrame(index=goog_data_signal.index).fillna(0.0)
portfolio = pd.DataFrame(index=goog_data_signal.index).fillna(0.0)
positions['GOOG'] = goog_data_signal['signal']
portfolio['positions'] = (positions.multiply(goog_data_signal['price'], axis=0))
portfolio['cash'] = initial_capital - (positions.diff().multiply(goog_data_signal['price'], axis=0)).cumsum()
portfolio['total'] = portfolio['positions'] + portfolio['cash']

plt.plot(portfolio['total'], label='total')
plt.legend()
plt.show()






