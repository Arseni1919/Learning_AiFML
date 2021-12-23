# moving avr conv diverg
from GLOBALS import *

close = goog_data2['Close']

num_periods_fast = 10  # fast EMA time period
K_fast = 2 / (num_periods_fast + 1)  # fast EMA smoothing factor
ema_fast = 0

num_periods_slow = 40  # slow EMA time period
K_slow = 2 / (num_periods_slow + 1)  # slow EMA smoothing factor
ema_slow = 0

num_periods_macd = 20  # MACD EMA time period
K_macd = 2 / (num_periods_macd + 1)  # MACD EMA smoothing factor
ema_macd = 0

ema_fast_values = []  # track fast EMA values for visualization purposes
ema_slow_values = []  # track slow EMA values for visualization purposes
macd_values = []  # track MACD values for visualization purposes
macd_signal_values = []  # MACD EMA values tracker
macd_histogram_values = []  # MACD - MACD-EMA

for close_price in close:
    if ema_fast == 0: # first observation
        ema_fast = close_price
        ema_slow = close_price
    else:
        ema_fast = (close_price - ema_fast) * K_fast + ema_fast
        ema_slow = (close_price - ema_slow) * K_slow + ema_slow
        ema_fast_values.append(ema_fast)
        ema_slow_values.append(ema_slow)
        macd = ema_fast - ema_slow  # MACD is fast_MA - slow_EMA
        if ema_macd == 0:
            ema_macd = macd
        else:
            ema_macd = (macd - ema_macd) * K_macd + ema_macd  # signal is EMA of MACD values
        macd_values.append(macd)
        macd_signal_values.append(ema_macd)
        macd_histogram_values.append(macd - ema_macd)

fig = plt.figure()
lw = 1.
ax1 = fig.add_subplot(311, ylabel='Google price in $')
ax1.plot(close, color='g', lw=lw, label='close')
ax1.plot(ema_fast_values, color='b', lw=lw, label='ema_fast')
ax1.plot(ema_slow_values, color='r', lw=lw, label='ema_slow')
ax2 = fig.add_subplot(312, ylabel='MACD')
ax2.plot(macd_values, color='black', lw=lw, label='macd_values')
ax2.plot(macd_signal_values, color='g', lw=lw, label='macd_signal_values')
ax3 = fig.add_subplot(313, ylabel='MACD')
ax3.bar(range(len(macd_histogram_values)), macd_histogram_values, color='r', label='macd_histogram_values')
ax1.legend()
ax2.legend()
ax3.legend()
plt.show()
