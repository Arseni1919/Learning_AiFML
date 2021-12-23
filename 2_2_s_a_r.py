import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from GLOBALS import *


goog_data_signal = pd.DataFrame(index=goog_data2.index)
goog_data_signal['price'] = goog_data2['Adj Close']


def trading_support_resistance(curr_data, bin_width=20):
    len_data = len(curr_data)
    curr_data['sup_tolerance'] = pd.Series(np.zeros(len_data))
    curr_data['res_tolerance'] = pd.Series(np.zeros(len_data))
    curr_data['sup_count'] = pd.Series(np.zeros(len_data))
    curr_data['res_count'] = pd.Series(np.zeros(len_data))
    curr_data['sup'] = pd.Series(np.zeros(len_data))
    curr_data['res'] = pd.Series(np.zeros(len_data))
    curr_data['positions'] = pd.Series(np.zeros(len_data))
    curr_data['signal'] = pd.Series(np.zeros(len_data))
    in_support = 0
    in_resistance = 0
    margin = 0.2

    for x in range((bin_width - 1) + bin_width, len_data):
        data_section = curr_data[x-bin_width:x+1]
        support_level = min(data_section['price'])
        resistance_level = max(data_section['price'])
        range_level = resistance_level - support_level
        curr_data['res'][x] = resistance_level
        curr_data['sup'][x] = support_level
        curr_data['sup_tolerance'][x] = support_level + margin * range_level
        curr_data['res_tolerance'][x] = resistance_level - margin * range_level

        if curr_data['res_tolerance'][x] <= curr_data['price'][x] <= curr_data['res'][x]:
            in_resistance += 1
            curr_data['res_count'][x] = in_resistance
        elif curr_data['sup'][x] <= curr_data['price'][x] <= curr_data['sup_tolerance'][x]:
            in_support += 1
            curr_data['sup_count'][x] = in_support
        else:
            in_support, in_resistance = 0, 0

        if in_resistance > 2:
            curr_data['signal'][x] = 1
        elif in_support > 2:
            curr_data['signal'][x] = 0
        else:
            curr_data['signal'][x] = curr_data['signal'][x-1]

    curr_data['positions'] = curr_data['signal'].diff()


trading_support_resistance(goog_data_signal)

# plot
fig = plt.figure()
ax_1 = fig.add_subplot(111, ylabel='Google price')
goog_data_signal['sup'].plot(ax=ax_1, color='g', lw=2.)
goog_data_signal['res'].plot(ax=ax_1, color='b', lw=2.)
goog_data_signal['price'].plot(ax=ax_1, color='r', lw=2.)
ax_1.plot(goog_data_signal.loc[goog_data_signal['positions'] == 1.].index,
          goog_data_signal.price[goog_data_signal.positions == 1.],
          '^', markersize=7, color='k', label='buy')
ax_1.plot(goog_data_signal.loc[goog_data_signal['positions'] == -1.].index,
          goog_data_signal.price[goog_data_signal.positions == -1.],
          'v', markersize=7, color='k', label='sell')
plt.legend()
plt.show()





