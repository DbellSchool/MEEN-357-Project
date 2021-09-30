# Project exicution File
from MEEN_357_Goup_Project_Lib import get_mass, tau_dcmotor
#wheel_rad = 0.3 # meters
#Wheel_mass = 1.0 # kg one drive wheel
#T_s = 170 #N*m
#T_nl = 0 #N*m
#w_nl = 3.80 # rad/s
#Motor_mass = 5.0 # kg ( one motor )
#Payload = 75 # kg ( one motor )
#RTG_mass = 90 # kg
#Chassis_mass = 659 # kg
#d1 = 0.04     #m Speed_reducer_minions
#d2 = 0.07     #m Speed reudcer gear diamiter
#SR_mass = 1.5 #kg
#g_mars = 3.72 # m/s



wheel = {"radius":0.3, "mass": 1.0 }  #Radius in [m]  one drive wheel [kg]
speed_reducer = {"type": "reverted", "diam_pinion": 0.04 ,"diam_gear":0.07, "mass":1.5} # diam in [m] mass in [kg]
motor = {"torque_stall": 170, "torque_noload": 0, "speed_noload": 3.80, "mass": 5.0} #torque [N*m] speed [rad/s] mass [kg]


chassis = {"mass": 659} #kg
science_payload = {"mass":75 } #kg
power_subsys = {"mass": 90} #kg
planet = {"g":3.72} #m/s^2


wheel_assembly = {"wheel": wheel, "speed_reducer": speed_reducer, "motor": motor}
rover = {"wheel_assembly": wheel_assembly,"chassis":chassis, "science_payload":science_payload,"power_subsys":power_subsys }

m= get_mass (rover)

w = [4,5,6]
t = tau_dcmotor(w)
print(t)



#x =tau_dcmotor(30,motor)