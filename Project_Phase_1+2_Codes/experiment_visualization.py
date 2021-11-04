import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from define_experiment import experiment1
experiment = experiment1()[0]

# provided data points
A_dist = np.array([0,20,60,80,100])
A_deg = np.array([0,0,10,-5,0])

# intripolates data
alpha_f = interp1d(A_dist,A_deg, kind = 'cubic', fill_value = 'extrapolate')

# finds min and max info from provided data
start_dist = min(experiment["alpha_dist"] )
end_dist = max(experiment["alpha_dist"] )

# provided 100 data points spaced evenly between range provided above
x = np.linspace(start_dist,end_dist,100)

angle = alpha_f(x)

#plots data
plt.plot(A_dist,A_deg,'*r')
plt.plot(x,angle,'-k')
plt.xlabel('x[m]')
plt.ylabel('angle [deg]')

plt.show()

