from GLOBALS import *

close = goog_data2['Close']

time_period = 20  # history length for Simple Moving Average for middle band
stdev_factor = 2  # Standard Deviation Scaling factor for the upper and lower bands
history = []  # price history for computing simple moving average
sma_values = []  # moving average of prices for visualization purposes
upper_band = []  # upper band values
lower_band = []  # lower band values

for close_price in close:
    history.append(close_price)
    if len(history) > time_period:  # we only want to maintain at most 'time_period' number of price observations
        del (history[0])

    sma = stats.mean(history)
    sma_values.append(sma)  # simple moving average or middle band
    variance = 0  # variance is the square of standard deviation
    for hist_price in history:
        variance = variance + ((hist_price - sma) ** 2)
    stdev = math.sqrt(variance / len(history))  # use square root to get standard deviation

    upper_band.append(sma + stdev_factor * stdev)
    lower_band.append(sma - stdev_factor * stdev)

fig = plt.figure()
lw = 1.
ax1 = fig.add_subplot(111, ylabel='Google price in $')
ax1.plot(close, color='g', lw=lw, label='close')
ax1.plot(sma_values, color='b', lw=lw, label='sma_values')
ax1.plot(upper_band, color='r', lw=lw, label='upper_band')
ax1.plot(lower_band, color='k', lw=lw, label='lower_band')
ax1.legend()
plt.show()
