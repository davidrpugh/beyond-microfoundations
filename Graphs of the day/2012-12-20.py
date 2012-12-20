import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define the Cobb-Douglas production function
def F(K, L, A=1):
    """
    
    Classic Cobb-Douglas production function.  Output is a function of the capital 
    stock, K, and labor, L.  Note that technology, A, is assumed to be labor-
    augmenting.
    
    Parameters, which are assumed to be already defined, are capital's share, 
    alpha, and labor's share beta. Typically, one assumes constant returns to scale 
    in which case beta = 1 - alpha.
    
    """
    return K**alpha * (A * L)**beta

# create a grid of (x,y) values which we will pass to function
capital = np.linspace(0, 50, 100)
labor = np.linspace(0, 50, 100)
K, L = np.meshgrid(capital, labor)

# Choose parameter values
alpha = 1 / 3.
beta = 1 - alpha
A = 1

# we will actually plot output
output = F(K, L, A)

##### Static snapshot using matplotlib #####

# create a new Figure object 
fig = plt.figure(figsize=(12,6))

# create a 3D Axes object for the first subplot
ax = fig.add_subplot(121, projection='3d', elev=30, azim=310)

# note the use of the new plot command!
production_frontier = ax.plot_surface(K, L, output, rstride=1, cstride=1, cmap=mpl.cm.hot, 
                                      linewidth=0, vmin=0, vmax=np.max(output), 
                                      antialiased=False)

# axes, labels, title, colorbar etc.
ax.set_xlim(0, 50)
ax.set_ylim(0, 50)
ax.set_xlabel(r'Capital ($K_{t}$)')
ax.set_ylabel(r'Labor ($L_{t}$)')

# create the contour plot for the second subplot
ax2 = fig.add_subplot(122)
im = ax2.imshow(output, interpolation='gaussian', origin='lower', cmap=mpl.cm.hot, 
                vmin=0, vmax=np.max(output), extent=(0, 50, 0, 50))

# demarcate the contours
CS = ax2.contour(K, L, output, np.linspace(0, np.max(output), 10), colors=np.repeat('k', 10), 
                 linewidths=1, linestyles='solid')
ax2.clabel(CS, inline=1, fmt='%1.2f')

# axes, labels, title, colorbar etc.
ax2.set_xlim(0, 50)
ax2.set_ylim(0, 50)
ax2.set_xlabel(r'Capital, $K_{t}$')
ax2.set_ylabel(r'Labor, $L_{t}$')

# add a color bar to the figure
fig.colorbar(production_frontier, shrink=0.75, aspect=10)

# add a title to the figure
fig.text(0.5, 0.95, r'$F(K,\ L)$ for $\alpha=%.2f, A=%.2f$' %(alpha, A), fontsize=20, \
         ha='center')

# save the plot!
plt.savefig('2012-12-20-CRTS-production-frontier.png')

# display the plot!
plt.show()

"""
##### Interactive production frontier using Mayavi #####
from mayavi import mlab

# plot the data using mayavi
production_frontier = mlab.mesh(K, L, output, colormap='hot')

# add axes 
axes = mlab.axes(xlabel=r'Capital, K', ylabel=r'Labor, L', zlabel=r'Output, Y')

# display the interactive plot
mlab.show()

"""
