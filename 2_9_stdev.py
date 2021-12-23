from GLOBALS import *

close = goog_data2['Close']

time_period = 20  # look back period
history = []  # history of prices
sma_values = []  # to track moving average values for visualization purposes
stddev_values = []  # history of computed stdev values

for close_price in close:
    history.append(close_price)
    if len(history) > time_period:  # we track at most 'time_period' number of prices
        del (history[0])
    sma = stats.mean(history)
    sma_values.append(sma)
    variance = 0  # variance is square of standard deviation
    for hist_price in history:
        variance = variance + ((hist_price - sma) ** 2)
    stdev = math.sqrt(variance / len(history))
    stddev_values.append(stdev)

fig = plt.figure()
lw = 1.
ax1 = fig.add_subplot(211, ylabel='Google price in $')
ax1.plot(close, color='k', lw=lw, label='close')
ax2 = fig.add_subplot(212, ylabel='std in $')
# ax2.plot(sma_values, color='b', lw=lw, label='sma_values')
ax2.plot(stddev_values, color='r', lw=lw, label='stddev_values')

ax1.legend()
ax2.legend()
plt.show()
