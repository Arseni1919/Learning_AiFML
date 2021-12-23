from GLOBALS import *

time_period = 20
K = 2 / (time_period + 1)
ema_p = 0
history = []
ema_values = []
close = goog_data2['Close']

for close_price in close:
    if ema_p == 0:
        ema_p = close_price
    else:
        ema_p = (close_price - ema_p) * K + ema_p
    ema_values.append(ema_p)


history = []
sma_values = []

close = goog_data2['Close']

for close_price in close:
    history.append(close_price)
    if len(history) > time_period:
        del(history[0])

    sma_values.append(stats.mean(history))

plt.plot(close, color='g', lw=2., label='close')
plt.plot(ema_values, color='r', lw=1., label='ema_values')
plt.plot(sma_values, color='b', lw=1., label='sma_values')
plt.legend()
plt.show()





