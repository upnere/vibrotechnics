#Beat phenomenon. Case 1

import matplotlib.pyplot as plt
import numpy as np

# given
t = np.linspace(0,40*np.pi,1000)
w_n = 1000
f0 = 0.1

# the excitation frequency from the end-user
#___ your code ____

# calculate the response
#___ your code ____

# plot the function 
plt.plot(t,x)
plt.xlabel('time, t [s]')
plt.ylabel('x(t)')
plt.title('Beating, w = ${0}$ rad/s'.format(w))
plt.savefig('msd_forced.png')