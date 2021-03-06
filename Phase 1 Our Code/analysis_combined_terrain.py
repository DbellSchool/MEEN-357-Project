#Crete apy-file script called analysis_combined_terrain.pyin which you use a root-finding method (e.g., bisection method, secant method, etc.)to determine the speed of the rover at various values for the coefficient of rolling resistance AND terrain slope. You will plot the results as a surface. Important note: There are a few combinations of slope and rolling resistance for which no terminal speed is reached. This occurs when the slope is negative (rover traveling downhill) and the coefficient of rolling resistance  is  near  zero  (firm  ground).  Physically,  in  these  cases  the  rover  continues  to  accelerate  as  it descends  the  hill.  Practically, your  code  shouldreturn  NAN  when  it  cannot  find  a  root.  Your  code  can continue with the NAN results in a few places. 
# Pythongraphing commands will just leave blanks where the NAN points are in your data.Please follow the steps as outlined belowin order to generate data compatiblewith asurface plotting function:
# 1.Generate rolling resistance coefficients using the following line of code: 
#   •Crr_array= numpy.linspace(0.01,0.4,25);
# 
# 2.Generate an arrayof terrain angles using the following line of code: 
#   •sl         ope_array_deg = numpy.linspace(-10,35,25);
# 
# 3.Surface plotting functionsoftenrequires matrix inputs. Two of these matrices define values for the independent variables (coefficient of rolling resistance and slope). 
#   The other matrix contains therover speed data. To generate the two matrices of independent variable data, use the following line of code:
#   •CRR,SLOPE= numpy.meshgrid(Crr_array, slope_array_deg)
# 
# 4.Create a matrix of zeros called VMAXthat is the same size as the two matrices you created in the previous step. The following command will work:
#   •VMAX= numpy.zeros(numpy.shape(CRR),dtype = float)
# 
# 5.Now all the preliminaries are complete and you can analyze the rover. Create a double loop that iterates through the elements of the Crr and SLOPE matrices. It should look something like the following(you don’t have to use these variable namesor this exact code...this is just illustrative):
# MEEN 357Engineering Analysisfor Mechanical EngineersFall 202111N = numpy.shape(CRR)[0]for iin range(N):for jin range(N):Crr_sample = float(CRR[i,j])slope_sample = float(SLOPES[i,j])VMAX[i,j]= ... #here you put code to find the max speed at Crr_sample and #slope_sample
# 
# 6.Once you complete the double loop, you can call the surface plotting command as follows. Make sure to add axis labels and a descriptive title. Choose an appropriate view for the surface plotin your script.
#   •figure = matplotlib.pyplot.figure()
#   •ax = Axes3D(figure, elev= N1, azim = N2)# where N1 and N2 will control the 3D view•ax.plot_surface(CRR,SLOPE, VMAX)As with the other analysis scripts:Do not display anything to the console.
from subfunctions import  F_net, rover,planet, get_gear_ratio, rover

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar
from mpl_toolkits.mplot3d import Axes3D


Crr=  np.linspace(0.01,0.4,25)  #25 long
slope_deg = np.linspace(-10,35,25) #25 Long

CRR_grid, Deg_grid = np.meshgrid(Crr,slope_deg)
grid = np.zeros(np.shape(CRR_grid),dtype=float)
N=25

L =-100
R = 100

Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])
r =rover['wheel_assembly']['wheel']['radius']


for i in range(N):
    for j in range(N):
        Fwrap = lambda x: F_net( x, [Deg_grid[i,j]], rover, planet, [CRR_grid[i,j]])
        w = root_scalar(Fwrap,method='bisect', bracket=[L,R])
        wWheel = w.root/Ng
        V = wWheel*r
        grid[i,j] = V

N1 = 45
N2 = 45
figure = plt.figure()
ax = Axes3D(figure, elev= N1, azim = N2)# where N1 and N2 will control the 3D view
ax.plot_surface(CRR_grid,Deg_grid, grid)
ax.set_xlabel("Crr")
ax.set_ylabel("Degree")
ax.set_zlabel("VMAX")

plt.show()


