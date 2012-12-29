import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.data import get_data_fred

##### download data from FRED #####

# Consumer Price Index for All Urban Consumers: All Items (Monthly, SA)
CPIAUCSL = get_data_fred('CPIAUCSL', start='1947-01-01')

# Consumer Price Index for All Urban Consumers: All Items (Monthly, NSA)
CPIAUCNS = get_data_fred('CPIAUCNS', start='1913-01-01')

# Gross Domestic Product: Implicit Price Deflator (Quarterly, SA)
GDPDEF = get_data_fred('GDPDEF', start='1947-01-01')

##### Construct measures of inflation #####

# Inflation is measured as percentage change from one year ago
Inflation_CPIAUCSL = CPIAUCSL.pct_change(periods=12)
Inflation_CPIAUCNS = CPIAUCNS.pct_change(periods=12)
Inflation_GDPDEF = GDPDEF.pct_change(periods=4)

##### plot the data #####

# basic plot in one line of code!
fig = plt.figure()
ax = Inflation_CPIAUCSL.plot(legend=False, label='SA')
#CPIAUCNS.plot(legend=False, label='NSA')

# add labels, axes, title, etc
ax.set_ylabel("Inflation (% Change from a year ago)")
ax.set_title("Measure of historical inflation inthe U.S\nSource: U.S. Department of Labor, BLS (via FRED)",
             weight='bold')
ax.grid()

# load the NBER recession dates
NBER_Dates = pd.read_csv('NBER Dates.txt')

# for loop generates recession bands!
for i in range(NBER_Dates.shape[0]):
    ax.axvspan(NBER_Dates['Peak'][i], NBER_Dates['Trough'][i], facecolor='grey', alpha=0.5)
    
# save the figure and display
#plt.savefig('2012-12-28-Mankiw-Figure-1-2.png')
plt.show()
