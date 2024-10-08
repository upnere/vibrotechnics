# Multiple Mass-Spring-Damper Systems Solver for Forced Vibration
# In this example, we will simulate multiple mass-spring-damper systems  
# using the Euler method for numerical integration.
# 
# We will solve several independent systems with different parameters in serial way.
#
# To run this code in the terminal, use the command:
#       python msd_forced.py
#

import numpy as np
import matplotlib.pyplot as plt
import time

# Mass-spring-damper system dynamics
def mass_spring_damper(m, c, k, F, x0, v0, dt, t_end):
    # Initialize arrays for displacement (x) and velocity (v)
    n_steps = int(t_end / dt)
    x = np.zeros(n_steps)
    v = np.zeros(n_steps)
    
    # Set initial conditions
    x[0] = x0
    v[0] = v0

    # Time-stepping loop (Euler's method)
    for i in range(1, n_steps):
        #__ your code for v[i] __
        x[i] = x[i-1] + v[i] * dt

    return x, v

def main():
    # To calculate the execution time define start_time
    start_time = time.time()

    # End time of simulation and dt
    t_end = 100.0
    dt = 0.01

    # Define systems with different parameters (m, c, k, F, x0, v0, dt, t_end)
    systems = [
        (1.0, 0.5, 10.0, 1.0, 0.0, 0.0, dt, t_end),  # System 1
        (1.5, 0.3, 15.0, 1.0, 0.0, 0.0, dt, t_end),  # System 2
        (2.0, 0.2, 20.0, 1.0, 0.0, 0.0, dt, t_end),  # System 3
        (1.2, 0.1, 12.0, 1.0, 0.0, 0.0, dt, t_end),  # System 4
    ]

    # Time vector for plotting
    t = np.arange(0, t_end, dt)  # Time vector

    # Plot the displacement over time for each system
    plt.figure(figsize=(10, 6))

    for i, system in enumerate(systems):
        x, v = mass_spring_damper(*system)
        plt.plot(t, x, label=f'System {i+1}')

    # Print the total execution time
    print(f"Serial execution time: {time.time() - start_time:.4f} seconds")

    # Plot settings
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.title('Mass-Spring-Damper Systems Displacement')
    plt.legend()
    plt.grid()
    plt.savefig('msd_forced.png')

if __name__ == "__main__":
    main()
