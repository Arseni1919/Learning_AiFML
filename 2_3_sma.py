from GLOBALS import *

time_period = 20
history = []
sma_values = []

close = goog_data2['Close']

for close_price in close:
    history.append(close_price)
    if len(history) > time_period:
        del(history[0])

    sma_values.append(stats.mean(history))

plt.plot(close, color='g', lw=2., label='close')
plt.plot(sma_values, color='r', lw=2., label='sma')
plt.legend()
plt.show()





