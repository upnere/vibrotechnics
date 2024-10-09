#Harmonic excitations. Case 2
#
# To run the code in the terminal, use the command:
#       python exercise2_4-skel.py
#

import matplotlib.pyplot as plt
import numpy as np

# given
t = np.linspace(0,10,500)
#____your code for constants____

# the natural frequency
#____your code for wn____
print('wn = ',wn)

# the response
#____your code for theta____

print('Max displacement: ',np.max(theta),'rad')

# the plot
plt.plot(t,theta)
plt.xlabel('Time [s]')
plt.ylabel('The angular displacement [rad]')
plt.savefig('harmonic2.png')