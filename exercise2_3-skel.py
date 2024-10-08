#Harmonic excitations
#
# To run the code in the terminal, use the command:
#       python exercise2_3-skel.py
#

import matplotlib.pyplot as plt
import numpy as np

# given
t = np.linspace(0,50,1000)
wn = 0.75
x0 = 0.03
v0 = 0.01
f0 = 0.2
w1 = 2
w2 = 4

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