# absolute price oscillator
import matplotlib.pyplot as plt

from GLOBALS import *

close = goog_data2['Close']

num_periods_fast = 10
K_fast = 2 / (num_periods_fast + 1)
ema_fast = 0

num_periods_slow = 40
K_slow = 2 / (num_periods_slow + 1)
ema_slow = 0

ema_fast_values = []
ema_slow_values = []
apo_values = []  # track computed absolute price oscillator values

for close_price in close:
    if ema_fast == 0:  # first observation
        ema_fast = close_price
        ema_slow = close_price
    else:
        ema_fast = (close_price - ema_fast) * K_fast + ema_fast
        ema_slow = (close_price - ema_slow) * K_slow + ema_slow
    ema_fast_values.append(ema_fast)
    ema_slow_values.append(ema_slow)
    apo_values.append(ema_fast - ema_slow)


fig = plt.figure()
lw = 1.
ax1 = fig.add_subplot(211, ylabel='Google price in $')
ax1.plot(close, color='g', lw=lw, label='close')
ax1.plot(ema_fast_values, color='b', lw=lw, label='ema_fast_values')
ax1.plot(ema_slow_values, color='r', lw=lw, label='ema_slow_values')
ax2 = fig.add_subplot(212, ylabel='APO')
ax2.plot(apo_values, color='black', lw=lw, label='apo')
ax2.hlines(0, 0, len(apo_values), lw=lw, color='g', label='zero line')
# ax2.xticks(goog_data2.index, goog_data2['Date'])
ax2.set_xticklabels(goog_data2['Date'])
ax1.legend()
ax2.legend()
plt.show()





