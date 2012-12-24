import pandas as pd
import numpy as np
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt

# load the kerrich data
kerrich_data = pd.read_csv('Kerrich.txt', header=0, index_col=0)
    
# create an object representing a fair coin
fair_coin = stats.distributions.bernoulli(0.5)

##### Difference between observed and expected heads is diverging #####

# create new Figure and Axes objects
fig = plt.figure()
ax = fig.add_subplot(111)

# plot Kerrich's difference
kerrich_data['Difference'].plot(style='r-', label='Kerrich Data')

# axes, labels, title, legend, etc.
ax.set_xscale('log')
ax.set_xlabel('Index')
ax.set_ylabel('Observed heads - expected heads')
ax.set_title('Divergence between observed heads and expected heads?')
ax.legend(loc='best', frameon=False)

# save the figure and display!
plt.savefig('2012-12-24-Kerrich-difference-btw-observed-expected-heads.png')
plt.show()

##### Checking Kerrich (single replication) #####

# simulate 10000 flips of a fair coin
T = 10000
np.random.seed(42)
data = fair_coin.rvs((T,))

# compute the difference between the observed and expected number of heads
difference = np.array([ 2 * np.sum(data[:i + 1]) - (i + 1) for i in range(T) ])

# create new Figure and Axes objects
fig = plt.figure()
ax = fig.add_subplot(111)

# plot the experimental data...
ax.plot(np.arange(1, 10001, 1), difference, 'k-', alpha=0.75)

# plot Kerrich's observed difference
kerrich_data['Difference'].plot(style='r-', label='Kerrich Data')

# axes, labels, title, legend, etc.
ax.set_xscale('log')
ax.set_xlabel('Index')
ax.set_ylabel('Observed heads - expected heads')
ax.set_title("A single replication of Kerrich's experiment!")
ax.legend(loc='best', frameon=False)

# save the figure and display
plt.savefig('2012-12-24-Replication-of-Kerrich-experiment.png')
plt.show()

##### N replications of the Kerrich experiment #####

# N runs, each of length T
N = 100
T = 10000

# generate an array of integers (each of n columns can be interpreted as a run of length T)
data = fair_coin.rvs((T,N))

# create an array in which to store the results
difference = np.zeros(data.shape, dtype=float)

# double for loop conducts the experiment
for j in range(N):
    for i in range(T):
        difference[i, j] = 2 * np.sum(data[:i + 1, j]) - (i + 1)

# create new Figure and Axes objects
fig = plt.figure()
ax = fig.add_subplot(111)

# plot each sample path...
for i in range(N):
    ax.plot(np.arange(1, T + 1, 1), difference[:, i], 'k-', alpha=0.05)

# plot Kerrich's observed difference
kerrich_data['Difference'].plot(style='r-', label='Kerrich Data')

# axes, labels, title, legend, etc.
ax.set_xscale('log')
ax.set_xlabel('Index')
ax.set_ylabel('Observed heads - expected heads')
ax.set_title("Kerrich's result was typical!")
ax.legend(loc='best', frameon=False)

# save the figure and display!
plt.savefig('2012-12-24-Simulation-of-Differences.png')
plt.show()

##### Show that the LLN holds ####

# set params
N = 100
T = 10000

# generate an array of integers (each of n columns can be interpreted as a run of length T)
data = fair_coin.rvs((T,N))

# create an array in which to store our sample averages
sample_averages = np.zeros(data.shape, dtype=float)

for j in range(N):
    for i in range(T):
        sample_averages[i, j] = np.mean(data[:i + 1, j])

# determine the fraction of heads in the kerrich data
kerrich_data['Fraction Heads'] = kerrich_data['Heads'] / kerrich_data.index.values.astype('float')

# create new Figure and Axes objects
fig = plt.figure()
ax = fig.add_subplot(111)

# plot each sample path
for i in range(N):
    ax.plot(np.arange(1, T + 1, 1), sample_averages[:, i], 'k-', alpha=0.05)

# plot Kerrich's fraction of heads
kerrich_data['Fraction Heads'].plot(style='r-', label=r'$\hat{\mu}_{k}$')

# demarcate the true mean
ax.axhline(y=0.5, color='black', linestyle='dashed', label=r'$\mu$')

# axes, labels, title, legend, etc.
ax.set_xscale('log')
ax.set_ylim(0, 1)
ax.set_xlabel('Index')
ax.set_ylabel(r'$\hat{\mu}$', rotation='horizontal', fontsize=15)
ax.set_title(r'Average number of heads converges to $\mu=0.5$!')
ax.legend(loc='best', frameon=False)

# save the figure and display the plot
plt.savefig('2012-12-24-Demonstration-of-LLN.png')
plt.show()
