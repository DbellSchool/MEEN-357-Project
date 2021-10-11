import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

A_dist = np.array([0,20,60,80,100])
A_deg = np.array([0,0,10,-5,0])
alpha_f = interp1d(A_dist,A_deg, kind = 'cubic', fill_value = 'extrapolate')

x = np.linspace(0,100,50)

angle = alpha_f(x)

plt.plot(A_dist,A_deg,'^r')
plt.plot(x,angle,'-k')
plt.xlabel('x[m')
plt.ylabel('angle [deg]')

plt.show()

