#Rotating unbalance. Case 2
#
# To run the code in the terminal, use the command:
#       python exercise2_6-skel.py
#

import matplotlib.pyplot as plt
import numpy as np

# given
r = np.linspace(0,3.5,350)
zeta1 = 0.1 
zeta2 = 0.25
zeta3 = 0.707
zeta4 = 1.0

# normalized magnitude
#____your code for amplitudes & plots____

plt.xlabel('r')
plt.ylabel('mX/m0e')
plt.legend()
plt.savefig('unbalance2.png')