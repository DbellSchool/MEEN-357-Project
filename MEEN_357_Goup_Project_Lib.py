import numpy as np
import math

#############
##Functions##
#############

##########################################
def get_mass(rov):
    #Computes the total mass of the rover. Uses information in the rover dict

    #print(rov)
    wheels = rov['wheel_assembly']['wheel']['mass']*6
    sRed = rov['wheel_assembly']['speed_reducer']['mass']*6
    WheelMotor = rov['wheel_assembly']['motor']['mass']*6
    chassis = rov['chassis']['mass']
    science_pay = rov['science_payload']['mass']
    power_sub = rov['power_subsys']['mass']

    rov_mass = wheels+ sRed+chassis+science_pay+power_sub+WheelMotor

    return rov_mass

def get_gear_ratio(dic):
    #returns the speed reduction ratio for the speed reducer based on speed_reducer dict.
    d1= dic["diam_pinion"]
    d2 = dic["diam_gear"]
    Ng = (d2/d1)**2

    return Ng

def tau_dcmotor(w,Motor = {"torque_stall": 170, "torque_noload": 0, "speed_noload": 3.80, "mass": 5.0} ):
    #Returns the motor shaft torque when given motor shaft speed and a dictionary containing important specifications for the motor. 

    t =[]
    try:

        for i in w:
            Ts = Motor["torque_stall"]
            TN = Motor["torque_noload"]
            wN = Motor["speed_noload"]
            T = Ts - ((Ts-TN)/wN)*i # equaiton on sheet five
            t.append(T)
    except:
        Ts = Motor["torque_stall"]
        TN = Motor["torque_noload"]
        wN = Motor["speed_noload"]
        T = Ts - ((Ts-TN)/wN)*w # equaiton on sheet five
        t.append(T)
    

    #P = T*w # power 

    return t

def F_drive(w, rover):
    #given motor shaft speeds from tau_motor, returns a vector of the same size consisting of the corresponding forces
    
    dic = rover['wheel_assembly']['speed_reducer']
    

    d1= dic["diam_pinion"]
    d2 = dic["diam_gear"]
    Ng = (d2/d1)**2
    #print("rover['wheel_assembly']['speed_reducer']")
    wS = []

    try:
        for i in w:
            wS.append(i/Ng)
    except:
       #print(type(w), type(Ng))
        var = w/Ng
        wS.append(var)
        


   
    
    radius = rover['wheel_assembly']['wheel']['radius']
    #motor = rover['wheel_assembly']['motor'] # [David Changed] Is this ok ? --> check chang at group meeting
    #t = tau_dcmotor(w,motor)
    t = tau_dcmotor(w)
    Fd = []
    for i in t:
        F = (i / radius)*6
        Fd.append(F)
    
    
    return Fd


def F_gravity(terrain_angle, rover, planet):
    #terrain_angle = np.array([])
    m = get_mass(rover) # [kg]
    g_mars = planet["g"] # [m/s^2]
    Fgt = []#[2, 3, 4]
    for i in terrain_angle:
        Fg = m * g_mars * np.sin(i*math.pi/180) #[N]  # does this need to be negetive ??
        Fgt.append(-Fg)
    return np.array(Fgt)


def F_rolling(w, terrain_angle, rover, planet, Crr):
    #solving for velocity of rover
    radius = rover['wheel_assembly']['wheel']['radius']
    v_rover = []
    try:
        for i in w:
            v_r = radius * i
            v_rover.append(v_r)

    except:
        v_r = radius * w
        v_rover.append(v_r)
        
    #solving for Constant force (Frr)
    g = planet['g']
    r_mass = get_mass(rover)
    Fn = []
    for i in terrain_angle:
        F = r_mass * g * (math.cos(i*math.pi/180))
        Fn.append(F)
    
    Frr_simp = []
 
    for i in Fn:
        Frr = Crr[0] * i
        Frr_simp.append(Frr)
    
    #solving for Frr
    Frr = []
    for i in v_rover:
        for j in Frr_simp:
            Fr = math.erf(40 * i) *j ###### What is going on here ??
            Frr.append(-Fr)
    
    return np.array(Frr)

# DAVID I NEED YOUR HELP ON THE FUNCTION BELOW 
# (thank you)

# Finding the net force on the rover
def F_net(w, terrain_angle, rover, planet, Crr):

    F1 = F_drive(w, rover)
    F2 = F_gravity(terrain_angle, rover, planet)
    F3 = F_rolling(w, terrain_angle, rover, planet, Crr)
    Fnet = []
    for i in range(len(F1)):
        F_net = F1[i] + F2[i] + F3[i]
        Fnet.append(F_net)
    # f1_f2 = []
    # for i in F1:
    #     for j in F2:
    #         f1_f2.append(j+i)
            
    
    #Fn = (F3 + f1_f2)
    #print('Fn =', Fnet)
    return np.array(Fnet)
#################################################################

###################
# Main Dictionary #
###################


wheel = {"radius":0.3, "mass": 1.0 }  #Radius in [m]  one drive wheel [kg]
speed_reducer = {"type": "reverted", "diam_pinion": 0.04 ,"diam_gear":0.07, "mass":1.5} # diam in [m] mass in [kg]
motor = {"torque_stall": 170, "torque_noload": 0, "speed_noload": 3.80, "mass": 5.0} #torque [N*m] speed [rad/s] mass [kg]


chassis = {"mass": 659} #kg
science_payload = {"mass":75 } #kg
power_subsys = {"mass": 90} #kg
planet = {"g":3.72} #m/s^2


wheel_assembly = {"wheel": wheel, "speed_reducer": speed_reducer, "motor": motor}
rover = {"wheel_assembly": wheel_assembly,"chassis":chassis, "science_payload":science_payload,"power_subsys":power_subsys }

#####################################



# Analysis of DC Motor

# graphs_motor.py 

# DAVID, do not know how to use the already defined functions in the graphs 
    # to call funiotn -> Funciton Name then needed paramiders => Name(c,y,z) <= depending on num of var
def func():

    import matplotlib.pyplot as plt
    import numpy as np

    # Create a python script that outputs a graph of the DC motor
    # doesn't display anything to the console
    # plots the following three graphs in a 3x1 array using matplot.lib
    # graph 1 : motor shaft speed vs. motor shaft torque (x-axis = torque)
    # graph 2: motor power vs. motor shaft torque (x-axis = torque)
    # graph 3: motor power vs. motor shaft speed (x-axis = speed)
    # label the axes of the graphs
    # use the functions we created to generate the graphs



    fig, (ax1, ax2, ax3) = plt.subplots(3)
    # motor shaft speed(w) is input by the user


    x1 = np.linspace(0, )
    y1 = 1

    fig.subtitle ("graphs_motor.py")
    ax1.plot(x1,y1)


#print(rover['wheel_assembly']['motor'])