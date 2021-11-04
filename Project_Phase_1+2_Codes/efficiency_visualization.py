import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from define_rovers import define_rover_4

rover = define_rover_4()[0]

motor  = rover['wheel_assembly']['motor']


# provided data informaiton added to dictionart 4 --> Comment out an uncomement lines below if changing dictionaries
effcy_tau = rover['wheel_assembly']['motor']['effcy_tau']
effcy = rover['wheel_assembly']['motor']['effcy']

#provided conditions
#effcy_tau = np.array([0,10,20,40,75,165])
#effcy = np.array([0,0.6,0.75,0.73,0.55,0.05])

# intripolated data provided form dict
alpha_f = interp1d(effcy_tau,effcy, kind = 'cubic', fill_value = 'extrapolate')

# finds start and end conditions from rover
max_t = motor["torque_stall"]
min_t = motor["torque_noload"]

x = np.linspace(min_t,max_t,100)

angle = alpha_f(x)

# plots data
plt.plot(effcy_tau,effcy,'*r')
plt.plot(x,angle,'-k')
plt.xlabel('tau [N*m]')
plt.ylabel('Eff [%]')

plt.show()
