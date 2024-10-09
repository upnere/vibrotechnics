# Multiple Mass-Spring-Damper Systems Solver
# In this example, we will simulate multiple mass-spring-damper systems  
# using the Euler method for numerical integration.
# 
# We will solve several independent systems with different parameters in serial way.
#
# User can set the number of systems to simulate using the -num argument:
#       python msd_rand-skel.py -num 5



import numpy as np
import matplotlib.pyplot as plt
import argparse
import random
import time

# Function for simulating mass-spring-damper system dynamics
def mass_spring_damper(m, c, k, F, x0, v0, dt, t_end):
    n_steps = int(t_end / dt)  # Number of time steps
    x = np.zeros(n_steps)  # Displacement array
    v = np.zeros(n_steps)  # Velocity array
    
    # Initial conditions
    x[0] = x0
    v[0] = v0

    # Time-stepping loop (Euler's method)
    for i in range(1, n_steps):
        v[i] = v[i-1] + (F - c * v[i-1] - k * x[i-1]) / m * dt
        x[i] = x[i-1] + v[i] * dt

    return x, v

# Main function to run the simulation
def main():
    # Argument parser to allow users to input the number of systems
    parser = argparse.ArgumentParser(description="Simulate a number of random mass-spring-damper systems")
    parser.add_argument(
        "-num", "--num_systems", type=int, default=4,
        help="Number of systems to simulate (between 3 and 30)"
    )
    args = parser.parse_args()

    # Ensure number of systems is between 3 and 30
    if args.num_systems < 3 or args.num_systems > 30:
        print("Number of systems must be between 3 and 30.")
        return

    num_systems = args.num_systems
    print(f"Simulating {num_systems} mass-spring-damper systems...")

    start_time = time.time()
    # Fixed parameters
    x0 = 0.0   # Initial displacement
    v0 = 0.0   # Initial velocity
    dt = 0.01  # Time step size
    t_end = 100.0  # End time of simulation

    # Randomly generate system parameters within the given ranges
    systems = []
    for i in range(num_systems):
        m = random.uniform(1.0, 3.0)     # Mass in range [1, 3]
        c = random.uniform(0.0, 2.5)    # Damping coefficient in range [0, 2.5]
        k = random.uniform(10.0, 30.0)   # Spring constant in range [10, 30]
        F = random.uniform(0.5, 2.0)     # External force in range [0.5, 2.0]
        systems.append((m, c, k, F, x0, v0, dt, t_end))

    # Time vector for plotting
    t = np.arange(0, t_end, dt)

    # Plot the displacement over time for each system
    plt.figure(figsize=(10, 6))

    for i, system in enumerate(systems):
        x, v = mass_spring_damper(*system)
        plt.plot(t, x, label=f'System {i+1}: m={system[0]:.2f}, c={system[1]:.2f}, k={system[2]:.2f}, F={system[3]:.2f}')
        #__ your code for v(t) plots __

    # Print the total execution time
    print(f"Random system parameters generated in {time.time() - start_time:.4f} seconds.")

    # Plot settings
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.title('Mass-Spring-Damper Systems Displacement')
    plt.legend(loc='upper right', fontsize='small')
    plt.savefig('msd_rand.png')

if __name__ == "__main__":
    main()
