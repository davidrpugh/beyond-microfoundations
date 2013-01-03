import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

# Define the representative agent's single period utility function
def u(C, l):
    """In the standard RBC model utility in each period is a function 
    of consumption per person, C, and leisure per person, 1 - l. Note 
    that the worker's labor endowment has been normalized to 1 for
    simplicity. 

    The parameter, b, determines how the representative agent weights
    uility from leisure relative to utility from consumption.
    
    """
    return np.log(C) + b * np.log(1 - l)

##### Plot of the utility surface #####

# create a new Figure object 
fig = plt.figure(figsize=(8,6))

# create a 3D Axes object
ax = fig.gca(projection='3d', elev=30, azim=310)

# create a grid of (x,y) values which we will pass to function
consumption = np.linspace(0, 10, 200)
labor       = np.linspace(0, 1, 20)
l, C        = np.meshgrid(labor, consumption)

# Choose parameter values
b = 2.5

# we will actually plot output
utility = u(C, l)

# note the use of the new plot command!
utility_surface = ax.plot_surface(l, C, utility, rstride=1, cstride=1,
                                  cmap=mpl.cm.terrain, linewidth=0, 
                                  vmin=-10, vmax=np.max(utility), 
                                  antialiased=False)

# axes, labels, title, colorbar etc.
ax.set_xlim(0, 1)
ax.set_ylim(0, 10)
ax.set_xlabel(r'Labor, $l_{t}$')
ax.set_ylabel(r'Consumption, $C_{t}$')
ax.set_title(r"Agent's utility surface, $u(C,\ l)$ for $b=%.2f$" %b, 
             fontsize=20)
fig.colorbar(utility_surface, shrink=0.75, aspect=10)

# save the figure and display!
plt.savefig('2013-01-03-RBC-Utility-Surface.png')
plt.show()

##### Contour plot of the utility surface #####
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

# Choose parameter values
b = 2.5

# we will actually plot output
utility = u(C, l)

# create the contour plot
im = ax.imshow(utility, interpolation='gaussian', origin='lower', 
               cmap=mpl.cm.terrain, vmin=-10, vmax=np.max(utility), 
               extent=(0, 1, 0, 10), aspect=0.10)

# demarcate the contours...
CS = ax.contour(l, C, utility, np.linspace(-8, np.max(utility), 10), 
                colors=np.repeat('k', 10), linewidths=1, 
                linestyles='solid')
ax.clabel(CS, inline=1, fmt='%1.2f')

# axes, labels, title, colorbar etc.
ax.set_xlim(0, 1)
ax.set_ylim(0, 10)
ax.set_xlabel(r'Labor, $l_{t}$')
ax.set_ylabel(r'Consumption, $C_{t}$')
ax.set_title(r'$u(C,\ l)$ for $b=%.2f$' %b, fontsize=20)
fig.colorbar(utility_surface, shrink=0.75, aspect=10)

# save figure and display
plt.savefig('2013-01-03-RBC-Contour-Plot-Utility-Surface.png')
plt.show()

##### Solving a 2-period model #####

# define parameter values
b, beta = 2.5, 0.99
 
# Specify some prices (i.e., wages and interest rates) all of which 
# households take as given when solving their optimization problem
w0, w1, r1 = 5.0, 9.0, 0.025

# Calculate the household's initial net worth (i.e., the PDV of his 
# labor endowment) given these prices
networth = w0 + (1 / (1 + r1)) * w1
print "PDV of Household's net worth:", networth

# is the non-negativity constraint on l0 satisfied by chosen prices?
print (1 / (1 + r1)) * (w1 / w0) < ((((1 + b) * (1 + beta)) / b) - 1)

# is the non-negativity constraint on l1 satisfied by chosen prices?
print (1 + r1) * (w0 / w1) < (((1 + b) / b) * ((1 + beta) / beta) - 1)

# define system of linear equations in four unknowns: C0, l0, C1, l1
A = np.array([[b, 0, w0, 0], 
              [beta * (1 + r1), -1, 0, 0], 
              [0, b, 0, w1], 
              [1, 1 / (1 + r1), -w0, -(1 / (1 + r1)) * w1]])

d = np.array([[w0], 
              [0], 
              [w1], 
              [0]])

# Solve the system of equations and assign the optimal choices for 
# consumption and labor supply
C_star0 = linalg.solve(A, d)[0,0]
C_star1 = linalg.solve(A, d)[1,0] 
l_star0 = linalg.solve(A, d)[2,0]
l_star1 = linalg.solve(A, d)[3,0]
u_star0 = u(C_star0, l_star0)
u_star1 = u(C_star1, l_star1)

print "Optimal C sequence:", (C_star0, C_star1) 
print "Optimal l sequence:", (l_star0, l_star1) 
print "Flow of utility:   ", (u_star0, u_star1)

##### Plotting the optimal bundle in period t=0 ####
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

# we will actually plot output
utility = u(C, l)

# re-create the contour plot
im = ax.imshow(utility, interpolation='gaussian', origin='lower', 
               cmap=mpl.cm.terrain, vmin=-10, vmax=np.max(utility), 
               extent=(0, 1, 0, 10), aspect=0.10)

# plot the budget constraint
labor_supply = np.linspace(0, 1, 100)
ax.plot(labor_supply, w0 * labor_supply + (1 / (1 + r1)) * \
        (w1 * l_star1 - C_star1), color='r', 
        label=r'$C_{0}=w_{0}l_{0} + \frac{1}{1 + r_{1}}(w_{1}l_{1}^* - C_{1}^*)$')

# demarcate the indifference curve...
CS = ax.contour(l, C, utility, np.array([u_star0]), colors='k', 
                linewidths=1, linestyles='solid')
ax.clabel(CS, inline=1, fmt='%1.4f')

# mark the optimal bundle
ax.hlines(C_star0, 0, l_star0, linestyle='dashed')
ax.vlines(l_star0, 0, C_star0, linestyle='dashed')

# axes, labels, title, colorbar etc.
ax.set_xlim(0, 1)
ax.set_ylim(0, 10)
ax.set_ylabel(r'Consumption, $C_{t}$')
ax.set_xlabel(r'Labor, $l_{t}$')
ax.set_title(r'Optimal bundle in period t=0 for $b=%.2f, \beta=%.2f$' 
             %(b, beta), fontsize=15)
ax.legend(loc=4, frameon=False)
fig.colorbar(utility_surface, shrink=0.75, aspect=10)

# Save the figure and display
plt.savefig('2013-01-03-Optimal-Bundle-Period-0.png')
plt.show()

##### Plotting the optimal bundle in period t=1 #####

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

# we will actually plot output
utility = u(C, l)

# re-create the contour plot
im = ax.imshow(utility, interpolation='gaussian', origin='lower', 
               cmap=mpl.cm.terrain, vmin=-10, vmax=np.max(utility), 
               extent=(0, 1, 0, 10), aspect=0.10)

# plot the budget constraint
labor_supply = np.linspace(0, 1, 100)
ax.plot(labor_supply, w0 * labor_supply + (1 / (1 + r1)) * \
        (w1 * l_star1 - C_star1), color='r', alpha=0.25)
ax.plot(labor_supply, w1 * labor_supply + (1 + r1) * \
        (w0 * l_star0 - C_star0), color='r',
        label=r'$C_{1} = w_{1}l_{1} + (1 + r_{1})(w_{0}l_{0}^* - C_{0}^*)$')

# demarcate the indifference curve...
CS_0 = ax.contour(l, C, utility, np.array([u_star0]), colors='k', 
                  linewidths=1, linestyles='solid', alpha=0.25)
CS_1 = ax.contour(l, C, utility, np.array([u_star1]), colors='k', 
                  linewidths=1, linestyles='solid')
ax.clabel(CS_1, inline=1, fmt='%1.4f')

# mark the optimal bundle
ax.hlines(C_star1, 0, l_star1, linestyle='dashed')
ax.vlines(l_star1, 0, C_star1, linestyle='dashed')

# axes, labels, title, colorbar etc.
ax.set_xlim(0, 1)
ax.set_ylim(0, 10)
ax.set_ylabel(r'Consumption, $C_{t}$')
ax.set_xlabel(r'Labor, $l_{t}$')
ax.set_title(r'Optimal bundle in period t=1 for $b=%.2f, \beta=%.2f$' \
             %(b, beta), fontsize=15)
ax.legend(loc=4, frameon=False)
fig.colorbar(utility_surface, shrink=0.75, aspect=10)

# Save the figure and display
plt.savefig('2013-01-03-Optimal-Bundle-Period-1.png')
plt.show()
