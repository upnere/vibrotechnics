# Animation of Mass-spring system
#
# To run the code in the terminal, use the command:
#       python exercise3_2.py
#

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import matplotlib.animation as animation

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

# animate x & x_dot vs time
fig, ax = plt.subplots()

x_curve, = ax.plot(t[0], x[0], 'r', lw=2, label=r'$x$')
x_dot_curve, = ax.plot(t[0], x_dot[0], 'g', lw=2, label=r'$\dot x$')

# formats the plot
ax.set_title(f'Mass-Spring System')
ax.legend(loc='lower left')
ax.set_xlabel('t (s)')
ax.set_ylabel(r'$x$ (m), $\dot x$ (m/s)')
ax.grid()
ax.set_xlim(0,5)
ax.set_ylim(-2,2)

def animate(i):
    x_curve.set_data(t[:i+1], x[:i+1])
    x_dot_curve.set_data(t[:i+1], x_dot[:i+1])

# save video at 30 fps
anim = animation.FuncAnimation(fig, animate, frames=len(t))
ffmpeg_writer = animation.FFMpegWriter(fps=30)
plt.show()