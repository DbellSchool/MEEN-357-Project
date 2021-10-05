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

theda = 0 # angle of incline 
Crr_array = numpy.linspace(0.01,0.4,25)

