import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.data import get_data_yahoo

##### download data from Yahoo #####

# Download the S&P 500
SP500 = get_data_yahoo('^GSPC', start='1950-01-03')

##### plot the data #####

# plot the S&P 500 index
ax1 = SP500['Close'].plot()

# add labels, axes, title, etc
ax1.set_ylabel('Close')
ax1.set_yscale('log')
ax1.set_title('Historical S&P 500 Index', weight='bold')

# load the NBER recession dates
NBER_Dates = pd.read_csv('NBER Dates.txt')

# for loop generates recession bands!
for i in range(NBER_Dates.shape[0]):
    ax1.axvspan(NBER_Dates['Peak'][i], NBER_Dates['Trough'][i], facecolor='grey', alpha=0.5)

# save the figure and display

plt.savefig('2012-12-21-SP500.png')
plt.show()
