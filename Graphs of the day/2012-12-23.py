import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.data import get_data_yahoo, get_data_fred

##### download data #####

# Download the S&P 500
SP500 = get_data_yahoo('^GSPC', start='1950-01-03', end='2012-11-30')

# Download the CPI data
CPIAUCSL = get_data_fred('CPIAUCSL', start='1950-01-01')

##### resample S&P 500 data #####

# Need S&P 500 data to be monthly...note I am taking monthly averages
monthly_avg_SP500 = SP500.resample('MS', how='mean')

# Add the CPI data as a column to the monthly DataFrame
monthly_avg_SP500['CPIAUCSL'] = CPIAUCSL

##### Convert nominal values to real values #####

# express all prices in terms of the price level in Nov. 2012...
monthly_avg_SP500['Price Deflator'] = (monthly_avg_SP500['CPIAUCSL']['2012-11-01'] / monthly_avg_SP500['CPIAUCSL'])
monthly_avg_SP500['Close (Real)'] = monthly_avg_SP500['Close'] * monthly_avg_SP500['Price Deflator']

##### Nominal S&P 500 #####

# new figure
fig = plt.figure()

# plot the nominal S&P 500 index
ax = monthly_avg_SP500['Close'].plot()

# add labels, axes, title, etc
ax.set_ylabel('Close')
ax.set_title('Historical S&P 500 Index (Monthly Avg.)', weight='bold')

# load the NBER recession dates
NBER_Dates = pd.read_csv('NBER Dates.txt')

# for loop generates recession bands!
for i in range(NBER_Dates.shape[0]):
    ax.axvspan(NBER_Dates['Peak'][i], NBER_Dates['Trough'][i], facecolor='grey', alpha=0.5)

# save the figure and display
plt.savefig('2012-12-23-Nominal SP500 (Monthly).png')
plt.show()

##### Nominal S&P 500 (log-scale) #####

# new figure
fig = plt.figure()

# plot the nominal S&P 500 index
ax = monthly_avg_SP500['Close'].plot()

# add labels, axes, title, etc
ax.set_ylabel('Close')
ax.set_yscale('log')
ax.set_title('Historical S&P 500 Index (Monthly Avg.)', weight='bold')

# load the NBER recession dates
NBER_Dates = pd.read_csv('NBER Dates.txt')

# for loop generates recession bands!
for i in range(NBER_Dates.shape[0]):
    ax.axvspan(NBER_Dates['Peak'][i], NBER_Dates['Trough'][i], facecolor='grey', alpha=0.5)

# save the figure and display
plt.savefig('2012-12-23-Nominal SP500 (Monthly, log-scale).png')
plt.show()

##### Real S&P 500 #####

# new figure
fig = plt.figure()

# plot the nominal S&P 500 index
ax = monthly_avg_SP500['Close (Real)'].plot()

# add labels, axes, title, etc
ax.set_ylabel('Close (Nov. 2012 Dollars)')
ax.set_title('Historical S&P 500 Index (Monthly Avg.)', weight='bold')

# load the NBER recession dates
NBER_Dates = pd.read_csv('NBER Dates.txt')

# for loop generates recession bands!
for i in range(NBER_Dates.shape[0]):
    ax.axvspan(NBER_Dates['Peak'][i], NBER_Dates['Trough'][i], facecolor='grey', alpha=0.5)

# save the figure and display
plt.savefig('2012-12-23-Real SP500 (Monthly).png')
plt.show()

##### Real S&P 500 (log-scale) #####

# new figure
fig = plt.figure()

# plot the real S&P 500 index
ax = monthly_avg_SP500['Close (Real)'].plot()

# add labels, axes, title, etc
ax.set_ylabel('Close (Nov. 2012 Dollars)')
ax.set_yscale('log')
ax.set_title('Historical S&P 500 Index (Monthly Avg.)', weight='bold')

# load the NBER recession dates
NBER_Dates = pd.read_csv('NBER Dates.txt')

# for loop generates recession bands!
for i in range(NBER_Dates.shape[0]):
    ax.axvspan(NBER_Dates['Peak'][i], NBER_Dates['Trough'][i], facecolor='grey', alpha=0.5)

# save the figure and display
plt.savefig('2012-12-23-Real SP500 (Monthly, log-scale).png')
plt.show()
