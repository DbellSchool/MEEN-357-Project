# Project exicution File
from MEEN_357_Goup_Project_Lib import get_mass, tau_dcmotor, rover

# Moved Dic definitions to other file to make  easier to use in exicution files ---> to access you need to add dic name in the imports ^^

m= get_mass (rover)

w = [4,5,6]
t = tau_dcmotor(w)
print(t)



#x =tau_dcmotor(30,motor)