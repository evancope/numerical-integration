import numpy as np
from function_file import optimal_integrator

n = 2000
t = np.linspace(0,200,n)
v = np.e ** (-0.6 * t) * np.cos(t)
initial_position = 5

final_position = optimal_integrator(v,n,v[0],v[n-1]) + initial_position

print(final_position)
