#
# Mass-spring-damper system dynamics for free vibrations
#
# To solve the system of ordinary differential equations (ODEs) for free vibrations 
# of a mass-spring-damper system, we will use the Euler's method. 
# 
# We also define three systems with different damping coefficients 
# (undamped, underdamped, and overdamped) and plot the displacement over time for each system.
#
# To run this code in the terminal, use the command:
#       python msd_free.py
#


import numpy as np
import matplotlib.pyplot as plt
import time

# Mass-spring-damper system dynamics for free vibrations
def free_vibration(m, c, k, x0, v0, dt, t_end):
    # Initialize arrays for displacement (x) and velocity (v)
    n_steps = int(t_end / dt)
    x = np.zeros(n_steps)
    v = np.zeros(n_steps)
    
    # Set initial conditions
    x[0] = x0
    v[0] = v0

    # Time-stepping loop (Euler's method)
    for i in range(1, n_steps):
        v[i] = v[i-1] + (-c * v[i-1] - k * x[i-1]) / m * dt
        x[i] = x[i-1] + v[i] * dt

    return x, v

def main():
    # To calculate the execution time define start_time
    start_time = time.time()

    # End time of simulation and dt
    t_end = 50.0
    dt = 0.01

    # Define systems for free vibration cases (m, c, k, x0, v0, dt, t_end)
    ## In Python, we can use a list of tuples to store the parameters of each system
    systems = [
        (1.0, 0.0, 10.0, 1.0, 0.0, dt, t_end),  # Undamped system
        (1.0, 1.0, 10.0, 1.0, 0.0, dt, t_end),  # Underdamped system
        (1.0, 15.0, 10.0, 1.0, 0.0, dt, t_end),  # Overdamped system
    ]

    labels = ['Undamped', 'Underdamped', 'Overdamped']

    # Time vector for plotting
    t = np.arange(0, t_end, dt)

    # Plot the displacement over time for each system
    plt.figure(figsize=(10, 6))

    for i, system in enumerate(systems):
        x, v = free_vibration(*system)
        plt.plot(t, x, label=f'{labels[i]} system')

    # Print the total execution time
    print(f"Execution time: {time.time() - start_time:.4f} seconds")

    # Plot settings
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.title('Free Vibrations of Mass-Spring-Damper Systems')
    plt.legend()
    plt.grid()
    plt.savefig('msd_free.png')

if __name__ == "__main__":
    main()
