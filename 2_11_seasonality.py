from GLOBALS import *

start_date = '2001-01-01'
end_date = '2018-01-01'
SRC_DATA_FILENAME = 'data/goog_data_large.csv'
try:
    goog_data = pd.read_csv(SRC_DATA_FILENAME)
    print('File data found...reading GOOG data')
except FileNotFoundError:
    print('File not found...downloading the GOOG data')
    goog_data = data.DataReader('GOOG', 'yahoo', start_date, end_date)
    goog_data.to_csv(SRC_DATA_FILENAME)

# goog_monthly_return = goog_data['Adj Close'].pct_change().groupby(
#     [goog_data['Adj Close'].index.year, goog_data['Adj Close'].index.month]
# ).mean()
goog_monthly_return = goog_data['Adj Close'].pct_change().groupby(
    [pd.DatetimeIndex(goog_data['Date']).year, pd.DatetimeIndex(goog_data['Date']).month]
).mean()

goog_monthly_return_list = []
for i in range(len(goog_monthly_return)):
    goog_monthly_return_list.append(
        {'month': goog_monthly_return.index[i][1], 'monthly_return': goog_monthly_return.values[i]})
goog_montly_return_list = pd.DataFrame(goog_monthly_return_list, columns=('month', 'monthly_return'))
goog_montly_return_list.boxplot(column='monthly_return', by='month')
ax = plt.gca()
# labels = [item.get_text() for item in ax.get_xticklabels()]
labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
ax.set_xticklabels(labels)
ax.set_ylabel('GOOG return')
plt.tick_params(axis='both', which='major', labelsize=7)
plt.title("GOOG Monthly return 2001-2018")
plt.suptitle("")
plt.show()


# Displaying rolling statistics
def plot_rolling_statistics_ts(ts, titletext, ytext, window_size=12):
    ts.plot(color='red', label='Original', lw=0.5)
    ts.rolling(window_size).mean().plot(color='blue', label='Rolling Mean')
    ts.rolling(window_size).std().plot(color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.ylabel(ytext)
    plt.title(titletext)
    plt.show()


# plot_rolling_statistics_ts(goog_monthly_return[1:], 'GOOG prices rolling mean and standard deviation', 'Monthly return')
# plot_rolling_statistics_ts(goog_data['Adj Close'], 'GOOG prices rolling mean and standard deviation', 'Daily prices',
#                            365)

# plt.figure()
# plt.subplot(211)
# plot_acf(goog_monthly_return[1:], ax=plt.gca(),lags=10)
# plt.subplot(212)
# plot_pacf(goog_monthly_return[1:], ax=plt.gca(),lags=10)
# plt.show()

model = ARIMA(goog_monthly_return[1:], order=(2, 0, 2))
fitted_results = model.fit()
goog_monthly_return[1:].plot()
fitted_results.fittedvalues.plot(color='red')
plt.legend()
plt.show()