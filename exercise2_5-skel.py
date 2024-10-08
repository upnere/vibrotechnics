#Unbalanced rotation. Case 1
#
# To run the code in the terminal, use the command:
#       python exercise2_5-skel.py
#

import numpy as np

#given
m = 40 # mass
m0 = 5 # unbalanced mass
e = 0.05 # excentricity
zeta = 0.15 # damping ratio

k = 4*250 # 4 springs in parallel
w1 = 1000*2*np.pi/60 # 1000 rpm
w2 = 60*2*np.pi/60 # 60 rpm

# the natural frequrncy & frequency ratios
wn = np.sqrt(k/m)
r1 = w1/wn
r2 = w2/wn

# amplitudes
r = r1
#____your code for X1____
print('The speed of the motor is 1000 rpm')
print('The amplitude is X_1 =',X1,'m\n')

r = r2
#____your code for X1____
print('The speed of the motor is 60 rpm')
print('The amplitude is X_2 =',X2,'m\n')