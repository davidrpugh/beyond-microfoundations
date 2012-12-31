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

# National Income: Compensation of Employees, Paid
COE = get_data_fred('COE', start='1947-01-01')

# Gross Domestic Product, 1 Decimal
GDP = get_data_fred('GDP', start='1947-01-01')

# combine into a DataFrame
data = pd.concat([COE, GDP], axis=1)

##### Construct measure of labor's share #####

# Divide COE by GDP
COE_share = data['COE'] / data['GDP']

##### plot the data with auto-ajusted ylim #####

# basic plot in one line of code!
COE_share.plot()

# add labels, axes, title, etc
plt.ylabel("COE Share")
plt.title("Employee compensation share of U.S. GDP\n" +\
          "Source: U.S. Department of Commerce, BEA (via FRED)",
          weight='bold')
plt.grid()

# add NBER recession bands
NBER_Shade()
    
# save the figure and display
plt.savefig('2012-12-31-Declining-COE-Share-of-GDP.png')
plt.show()

##### plot the data with auto-ajusted ylim #####

# basic plot in one line of code! (Krugman plots only data after 1973)
COE_share['1973-01-01':].plot()

# add labels, axes, title, etc
plt.ylabel("COE Share")
plt.title("Employee compensation share of U.S. GDP\n" +\
          "Source: U.S. Department of Commerce, BEA (via FRED)",
          weight='bold')
plt.grid()

# add the NBER recession bands
NBER_Shade()

# save the figure and display
plt.savefig('2012-12-31-Krugmans-Plot.png')
plt.show()

##### plot the data with auto-ajusted ylim #####

# basic plot in one line of code!
labors_share.plot()

# add labels, axes, title, etc
plt.ylabel(r"COE Share")
plt.ylim(0, 1)
plt.title("Employee compensation share of U.S. GDP\n" +\
          "Source: U.S. Department of Commerce, BEA (via FRED)",
          weight='bold')
plt.grid()

# add the NBER recession bands!
NBER_Shade()

# save the figure and display
plt.savefig('2012-12-31-Constant-COE-Share-of-GDP.png')
plt.show()
