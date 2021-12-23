from GLOBALS import *

close = goog_data2['Close']

time_period = 20  # how far to look back to find reference price to compute momentum
history = []  # history of observed prices to use in momentum calculation
mom_values = []  # track momentum values for visualization purposes

for close_price in close:
    history.append(close_price)
    if len(history) > time_period:  # history is at most 'time_period' number of observations
        del (history[0])
    mom = close_price - history[0]
    mom_values.append(mom)

fig = plt.figure()
lw = 1.
ax1 = fig.add_subplot(211, ylabel='Google price in $')
ax1.plot(close, color='k', lw=lw, label='close')
ax2 = fig.add_subplot(212, ylabel='Momentum in $')
ax2.plot(mom_values, color='b', lw=lw, label='mom_values')
ax1.legend()
ax2.legend()
plt.show()
