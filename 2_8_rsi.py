from GLOBALS import *

close = goog_data2['Close']

time_period = 20  # look back period to compute gains & losses
gain_history = []  # history of gains over look back period (0 if no gain, magnitude of gain if gain)
loss_history = []  # history of losses over look back period (0 if no loss, magnitude of loss if loss)
avg_gain_values = []  # track avg gains for visualization purposes
avg_loss_values = []  # track avg losses for visualization purposes
rsi_values = []  # track computed RSI values
last_price = 0  # current_price - last_price > 0 => gain. current_price - last_price < 0 => loss.

for close_price in close:
    if last_price == 0:
        last_price = close_price

    gain_history.append(max(0, close_price - last_price))
    loss_history.append(max(0, last_price - close_price))
    last_price = close_price

    if len(gain_history) > time_period:  # maximum observations is equal to lookback period
        del (gain_history[0])
        del (loss_history[0])

    avg_gain = stats.mean(gain_history)  # average gain over lookback period
    avg_loss = stats.mean(loss_history)  # average loss over lookback period
    avg_gain_values.append(avg_gain)
    avg_loss_values.append(avg_loss)
    rs = 0
    if avg_loss > 0:  # to avoid division by 0, which is undefined
        rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    rsi_values.append(rsi)

fig = plt.figure()
lw = 1.
ax1 = fig.add_subplot(311, ylabel='Google price in $')
ax1.plot(close, color='k', lw=lw, label='close')
ax2 = fig.add_subplot(312, ylabel='RS')
ax2.plot(avg_gain_values, color='b', lw=lw, label='avg_gain_values')
ax2.plot(avg_loss_values, color='r', lw=lw, label='avg_loss_values')
ax3 = fig.add_subplot(313, ylabel='RSI')
ax3.plot(rsi_values, color='k', lw=lw, label='rsi_values')
ax3.hlines(50, 0, len(rsi_values), lw=lw, color='g', label='zero line')

ax1.legend()
ax2.legend()
ax3.legend()
plt.show()
