import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.data import get_data_fred

def NBER_Shade():
    """Function adds National Bureau of Economic Research (NBER) recession
    bands to a Matplotlib Figure object.

    """
      
    # load the NBER recession dates
    NBER_Dates = pd.read_csv('NBER Dates.txt')

    # for loop generates recession bands!
    for i in range(NBER_Dates.shape[0]):
        plt.axvspan(NBER_Dates['Peak'][i], NBER_Dates['Trough'][i],
                    facecolor='grey', alpha=0.5)

##### download data from FRED #####

# Civilian unemployment rate (monthly, SA)
UNRATE_monthly = get_data_fred('UNRATE', start='1948-01-01')

# Convert to annual frequency by averaging across months
UNRATE_annual = UNRATE_monthly.resample('A', how='mean')

##### plot the historical unemployment rate #####

# basic plot in one line of code!
UNRATE_annual.plot()

# add labels, axes, title, etc
plt.xlabel("Year")
plt.ylabel("Percent")
plt.ylim(0, 10)
plt.title("Civilian unemployment rate (UNRATE), Seasonally adjusted\n" +\
          "Source: U.S. Department of Labor, BLS (via FRED)",
          weight='bold')
plt.grid()

# add NBER recession bands
NBER_Shade()
    
# save the figure and display
plt.savefig('2013-01-02-Mankiw-Fig-1-3.png')
plt.show()
