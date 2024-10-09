# Mass-spring system
#
# To run the code in the terminal, use the command:
#       python exercise3_1.py
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# constants
g = 9.81
k = 40
m = 1

# initial conditions
x0 = 0
xdot0 = 0
y0 = (x0,xdot0)

# y[0] = x, y[1] = xdot
def mass_spring_sys(t,y):
    return (y[1], g-k*y[0]/m)

solution = solve_ivp(mass_spring_sys,[0, 5],y0,
                     t_eval = np.linspace(0,5,5*30))

# results
x, x_dot = solution.y
t = solution.t

# plots
plt.plot(t, x, 'r', lw=2, label=r'$x$')
plt.plot(t, x_dot, 'g', lw=2, label=r'$\dot x$')
plt.title('Mass-Spring System')
plt.legend()
plt.xlabel('t (s)')
plt.ylabel(r'$x$ (m), $\dot x$ (m/s)')
plt.grid()
plt.savefig('ms.png')