#Harmonic excitations
#
# To run the code in the terminal, use the command:
#       python exercise2_3-skel.py
#

import matplotlib.pyplot as plt
import numpy as np

# given
t = np.linspace(0,50,1000)
#____your code for constants____

# the response
#____your code for w1____
#____your code for w2____


# plots
plt.plot(t,x1,label='w_1')
plt.plot(t,x2,label='w_2')
plt.xlabel('t [s]')
plt.ylabel('displacement [m]')
plt.grid()
plt.legend()
plt.savefig('harmonic.png')