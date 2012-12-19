import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.data import get_data_fred

##### download data from FRED #####

# Real GDP per capita (2010 Dollars, annual, NSA)
USARGDPC = get_data_fred('USARGDPC', start='1960-01-01')

##### plot the data #####

# basic plot in one line of code!
ax = USARGDPC.plot(legend=False)

# add labels, axes, title, etc
ax.set_ylabel("2010 U.S. Dollars")
ax.set_yscale('log')
ax.set_ylim(8000, 64000)
ax.set_yticks([8000, 16000, 32000, 64000])
ax.set_yticklabels([8000, 16000, 32000, 64000])
ax.set_title("Real GDP per Capita in the United States (USARGDPC)\nSource: U.S. Department of Labor, BLS (via FRED)", weight='bold')
ax.grid()

# load the NBER recession dates
NBER_Dates = pd.read_csv('NBER Dates.txt')

for i in range(NBER_Dates.shape[0]):
    ax.axvspan(NBER_Dates['Peak'][i], NBER_Dates['Trough'][i], facecolor='grey', alpha=0.5)
    
# save the figure and display
plt.savefig('2012-12-19-Mankiw-Figure-1-1.png')
plt.show()
