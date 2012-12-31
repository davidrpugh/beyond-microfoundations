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

# Combine the three Series objects into a single DataFrame
Inflation_Measures = Inflation_CPIAUCNS
Inflation_Measures['CPIAUCSL'] = Inflation_CPIAUCSL
Inflation_Measures['GDPDEF'] = Inflation_GDPDEF

##### plot the data #####

# basic plot in one line of code!
Inflation_Measures.plot(markersize=3, style='o-', alpha=0.75)

# add labels, axes, title, etc
plt.ylabel("Inflation (% Change from a year ago)")
plt.title("Measures of historical inflation in the U.S\nSource: U.S. Department of Labor, BLS (via FRED)",
      weight='bold')
plt.grid()

# load the NBER recession dates
NBER_Dates = pd.read_csv('NBER Dates.txt')

# for loop generates recession band!s
for i in range(NBER_Dates.shape[0]):
    plt.axvspan(NBER_Dates['Peak'][i], NBER_Dates['Trough'][i], facecolor='grey', alpha=0.5)
    
# save the figure and display
plt.savefig('2012-12-28-Mankiw-Figure-1-2.png')
plt.show()
