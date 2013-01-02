import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import wbdata

##### Extract data from World Bank API #####

# Want to grab measure of inflation (for comparison purposes)
indicators = {"FP.CPI.TOTL.ZG": "value"}

# Low income countries
LIC_countries = [country['id'] for country in wbdata.get_country(incomelevel="LIC", display=False)]
LIC_df = wbdata.get_dataframe(indicators, country=LIC_countries, convert_date=False)

# Lower Middle income countries
LMC_countries = [country['id'] for country in wbdata.get_country(incomelevel="LMC", display=False)]
LMC_df = wbdata.get_dataframe(indicators, country=LMC_countries, convert_date=False)

# Upper Middle income countries
UMC_countries = [country['id'] for country in wbdata.get_country(incomelevel="UMC", display=False)]
UMC_df = wbdata.get_dataframe(indicators, country=UMC_countries, convert_date=False)

# High income countries
HIC_countries = [country['id'] for country in wbdata.get_country(incomelevel="HIC", display=False)]
HIC_df = wbdata.get_dataframe(indicators, country=HIC_countries, convert_date=False)

##### plot FP.CPI.TOTL.ZG ####
fig = plt.figure()
ax = fig.add_subplot(111)

# add LIC inflation data
for country in np.unique(LIC_df['country'].values):
    # extract subset for given country
    mask = (LIC_df['country'] == country)
    tmp_data = LIC_df[mask]

    # plot inflation data
    LIC_plot, = ax.plot(tmp_data['date'].values, tmp_data['value'].values,
                        color=cm.jet(0), alpha = 0.25) 
# Label the LICs
LIC_plot.set_label('Low')
    
# add LMC inflation data
for country in np.unique(LMC_df['country'].values):
    # extract subset for given country
    mask = (LMC_df['country'] == country)
    tmp_data = LMC_df[mask]

    # plot inflation data
    LMC_plot, = ax.plot(tmp_data['date'].values, tmp_data['value'].values,
                        color=cm.jet(85), alpha = 0.25) 
# Label the LMC plot
LMC_plot.set_label('Lower-Middle')

# add UMC inflation data
for country in np.unique(UMC_df['country'].values):
    # extract subset for given country
    mask = (UMC_df['country'] == country)
    tmp_data = UMC_df[mask]

    # plot inflation data
    UMC_plot, = ax.plot(tmp_data['date'].values, tmp_data['value'].values,
                        color=cm.jet(170), alpha = 0.25) 
# Label the UMC plot
UMC_plot.set_label('Upper-Middle')

# add HIC countries    
for country in np.unique(HIC_df['country'].values):
    # extract subset for given country
    mask = (HIC_df['country'] == country)
    tmp_data = HIC_df[mask]

    # plot inflation data
    HIC_plot, = ax.plot(tmp_data['date'].values, tmp_data['value'].values,
                        color=cm.jet(255), alpha = 0.25) 
# Label the HIC plot
HIC_plot.set_label('High')

# axes, labels, title, legend, etc
ax.set_xlabel('Year')
ax.set_xlim(1960, 2012)
ax.set_ylabel("Inflation, consumer prices (annual %)")
ax.set_ylim(-200, 1000)
ax.set_title('Global Inflation by Income Group\nSource: World Bank, WDI',
             weight='bold', fontsize=15)
ax.legend(loc=3, frameon=False, ncol=4, mode="expand")

# save the figure and display...
plt.savefig('2013-01-01-Global-Inflation-by-Income-Groups.png')
plt.show()
