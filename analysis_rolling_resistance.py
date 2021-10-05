#
#Create apy-file script called analysis_rolling_resistance.pyin which you use a root-finding method (e.g., bisection method, secant method, etc.)to determine the speed of the rover at various values for the coefficient of rolling resistance. 
# This analysis is very similar to what you must do for the terrain slope.

# •Assume a terrain slope of 0 degrees (horizontal terrain)
# •Generate rolling resistance coefficients to test with the following line of code: oCrr_array = numpy.linspace(0.01,0.4,25);
# •Store the maximum velocity [m/s] at each angle in a vector called v_max.
# •Plot v_maxversus Crr_array. Make sure to label the axes and indicate their units.
# •Do not display anything to the console•The hints for the previous problem apply here as well.
#
import numpy
import matplotlib.pyplot as plt

theda = 0 # angle of incline 
Crr_array = numpy.linspace(0.01,0.4,25)

w = Crr_array*2

plt.plot(w,Crr_array, '-b')

plt.xlabel("omega [rad/s]")
plt.ylabel("CRR")
plt.grid("on")
#plt.xlim(0,5)
plt.show()

#############Graphing with SubplotsL
# import matplotlib.pyplot as plt
#     print("Starting Task 3")
#     N = 20

#     x1 = linspace(-5,5,num = N)
#     y1 = 0.5 *x1**2

#     x2 = linspace(0,100,num = N)
#     y2 = -x2

#     fig, (ax1, ax2) = plt.subplots(2)
#     fig.tight_layout(pad=3)
#     fig.suptitle('Task 3')

#     ax1.plot(x1, y1)
#     ax1.set_title("Exhibit 1")
#     ax1.set_xlabel("x")
#     ax1.set_ylabel("y")

#     ax2.plot(x2, y2)
#     ax2.set_title("Exhibit 2")
#     ax2.set_xlabel("Work")
#     ax2.set_ylabel("Play")
#     plt.show()

