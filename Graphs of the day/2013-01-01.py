import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import wbdata

##### Extract data from World Bank API #####

# ISO country codes for all countries and regional aggregates
all_countries = [i['id'] for i in wbdata.get_country('all', display=False)]

# Don't want any regional aggregates
not_countries = ['ARB', 'CSS', 'EAP', 'EAS', 'ECA', 'ECS', 'EMU', 'EUU', 'HIC',
                 'HPC', 'INX', 'LAC', 'LCN', 'LDC', 'LIC', 'LMC', 'LMY', 'MEA',
                 'MEA', 'MIC', 'MNA', 'NOC', 'OEC', 'OED', 'OSS', 'PSS', 'SSA',
                 'SSF', 'SST', 'UMC', 'WLD']

# Keep only valid countries
valid_countries = [iso3 for iso3 in all_countries if iso3 not in not_countries]
                   
# Want to grab two different measures of inflation
indicators = {"FP.CPI.TOTL.ZG": "Inflation, consumer prices (annual %)",
              "NY.GDP.DEFL.KD.ZG": "Inflation, GDP deflator (annual %)"}

# Dump the output into a Pandas DataFrame
df = wbdata.get_dataframe(indicators, valid_countries, convert_date=False)

##### plot FP.CPI.TOTL.ZG ####
fig = plt.figure()
ax = fig.add_subplot(111)

for country in np.unique(df['country'].values):
    # extract subset for given country
    tmp_data = df[df['country'] == country]

    # plot inflation data
    ax.plot(tmp_data['date'].values,
            tmp_data['Inflation, consumer prices (annual %)'].values,
            'r-', alpha = 0.10) 

    if np.isnan(tmp_data['Inflation, consumer prices (annual %)'].values[-1]) == False:
        x = tmp_data['date'].values[-1]
        y = tmp_data['Inflation, consumer prices (annual %)'].values[-1]
        print x
        print y
        #ax.text(x, y, country)
        
# axes, labels, title, legend, etc
ax.set_xlabel('Year')
ax.set_xlim(1960, 2012)
ax.set_ylabel("Inflation, consumer prices (annual %)")

plt.show()
