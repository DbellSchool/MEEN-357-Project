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
from MEEN_357_Goup_Project_Lib import F_net, rover,planet, F_rolling # getsing funciton and constants
from scipy.optimize import root_scalar # for finsing zero 

#rom analysis_combined_terrain import Crr

terrain_angle = 0 # angle of incline 
CRR = numpy.linspace(0.01,0.4,25)

#for i in range(len(CRR)):
#F_net( 1, terrain_angle, rover, planet, CRR[1])


#fsolve (F_net( 'null', terrain_angle, rover, planet, CRR[1]),0)


def temp(x,n):
    return n+3*x

def fix(x):
    return temp(x,12)

def FuncWrap(x):
    

    return F_net( x, [0], rover, planet, [0.01])

L =-100
R = 100

val = root_scalar(FuncWrap,method='bisect', bracket=[L,R])
print("w is : ", val)



#F_rolling([1],[0], rover, planet, [0.1])

#w = fsolve(FuncWrap,3)

#print(w)

#plt.plot(w,CRR, '-b')

# plt.xlabel("omega [rad/s]")
# plt.ylabel("CRR")
# plt.grid("on")
# #plt.xlim(0,5)
# plt.show()