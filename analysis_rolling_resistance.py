#
#Create apy-file script called analysis_rolling_resistance.pyin which you use a root-finding method (e.g., bisection method, secant method, etc.)to determine the speed of the rover at various values for the coefficient of rolling resistance. 
# This analysis is very similar to what you must do for the terrain slope.

# •Assume a terrain slope of 0 degrees (horizontal terrain)
# •Generate rolling resistance coefficients to test with the following line of code: oCrr_array = numpy.linspace(0.01,0.4,25);
# •Store the maximum velocity [m/s] at each angle in a vector called v_max.
# •Plot v_maxversus Crr_array. Make sure to label the axes and indicate their units.
# •Do not display anything to the console•The  for the previous problem apply here as well.
#
import numpy # for formatting
import matplotlib.pyplot as plt # for plotting
from subfunctions import F_net, rover,planet, get_gear_ratio # getsing funciton and constants
from scipy.optimize import root_scalar # for finsing zero 


terrain_angle = 0 # angle of incline 
CRR = numpy.linspace(0.01,0.4,25)

L =-100
R = 100

Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])
r =rover['wheel_assembly']['wheel']['radius']
VMAX = []
for i in range(len(CRR)):
    Fwrap = lambda x: F_net( x, [0], rover, planet, [CRR[i]])
    w = root_scalar(Fwrap,method='bisect', bracket=[L,R])
    wWheel = w.root/Ng
    V = wWheel*r
    VMAX.append(V)


# graph data
plt.plot(VMAX,CRR, '-b')
plt.xlabel("omega [rad/s]")
plt.ylabel("CRR")
plt.grid("on")
plt.show()
