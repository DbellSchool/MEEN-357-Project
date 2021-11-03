import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from define_rovers import define_rover_4

rover = define_rover_4()[0]
#print(rover)

effcy_tau = rover['wheel_assembly']['motor']['effcy_tau']
effcy = rover['wheel_assembly']['motor']['effcy']
#effcy_tau = np.array([0,10,20,40,75,165])
#effcy = np.array([0,0.6,0.75,0.73,0.55,0.05])



alpha_f = interp1d(effcy_tau,effcy, kind = 'cubic', fill_value = 'extrapolate')

x = np.linspace(0,100,50)

angle = alpha_f(x)

plt.plot(effcy_tau,effcy,'^r')
plt.plot(x,angle,'-k')
plt.xlabel('tau [N*m]')
plt.ylabel('Efff [%]')

plt.show()
