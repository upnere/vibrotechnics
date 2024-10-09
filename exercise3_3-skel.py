# Mass-spring-damper system
#
# To run the code in the terminal, use the command:
#       python exercise3_3-skel.py
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# constants
g = 9.81
k = 40
m = 1
c = 1

# initial conditions
x0 = 0
xdot0 = 0
y0 = (x0,xdot0)

# y[0] = x, y[1] = xdot
def mass_spring_friction_sys(t,y):
    #____your code for ODE____

solution = solve_ivp(mass_spring_friction_sys,[0, 5],y0,
                     t_eval = np.linspace(0,5,5*30))

# results
x, x_dot = solution.y
t = solution.t

# plots
plt.subplot(1,2,1)
plt.plot(t, x, 'r', lw=2, label=r'$x$')
plt.plot(t, x_dot, 'g', lw=2, label=r'$\dot x$')
plt.title('Mass-Spring System')
plt.legend()
plt.xlabel('t (s)')
plt.ylabel(r'$x$ (m), $\dot x$ (m/s)')
plt.grid()

plt.subplot(1,2,2)
plt.plot(x, x_dot, 'b', lw=2)
plt.xlabel('$x$ (m)')
plt.ylabel(r'$\dot x$ (m/s)')
plt.title('Phase Plot')
plt.savefig('msd.png')