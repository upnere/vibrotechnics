#Beat phenomenon. Case 2
#
# To run the code in the terminal, use the command:
#       python exercise2_2-skel.py
#

import matplotlib.pyplot as plt
import numpy as np

# given
t = np.linspace(0,0.3,1000)

# two waves
#____ your code ____

# a superposition of waves
y = y1+y2

# plots
plt.subplot(2,1,1)
plt.plot(t,y1,label='1st wave')
plt.plot(t,y2,label='2nd wave')
plt.legend()
plt.subplot(2,1,2)
plt.plot(t,y)
plt.ylabel('Superposition of waves')
plt.xlabel('t')
plt.savefig('beat2.png')