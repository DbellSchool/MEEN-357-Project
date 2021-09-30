import numpy as np
import math

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
    for i in w:
        Ts = Motor["torque_stall"]
        TN = Motor["torque_noload"]
        wN = Motor["speed_noload"]
        T = Ts - ((Ts-TN)/wN)*i # equaiton on sheet five
        t.append(T)
    

    #P = T*w # power 

    return t

def F_drive(w, rover):
    #given motor shaft speeds from tau_motor, returns a vector of the same size consisting of the corresponding forces
    
    
    gear_ratio = get_gear_ratio()
   
    radius = rover['wheel_assembly']['wheel']['radius']
    t = tau_dcmotor(w,motor)
    Fd = []
    for i in t:
        Fd = (i / radius)*6
        Fd.append(Fd)
    print('Fd =', Fd)
    
    return Fd


def F_gravity(terrain_angle, rover, planet):
    import numpy as np
    terrain_angle = np.array([])
    # need the mass of the entire rover
    m = get_mass(rover)
    mass = rover
    rover("mass") 

    return


def F_rolling(omega, terrain_angle, rover, planet, Crr):
    #solving for velocity of rover
    radius = rover['wheel_assembly']['wheel']['radius']
    v_rover = []
    for i in w:
        v_rover = radius * i
        v_rover.append(v_rover)
        
    #solving for Constant force (Frr)
    g = planet['g']
    r_mass = get_mass(rover)
    Fn = []
    for i in terrain_angle:
        Fn = r_mass * g * (math.cos(i))
        Fn.append(Fn)
    
    Frr_simp = []
    Crr = 1 #i dont know where we get crr from... user input??
    for i in Fn:
        Frr_simp = Crr * i
        Frr_simp.append(Frr_simp)
    
    #solving for Frr
    Frr = []
    for i in v_rover, Frr_simp:
        for j in Frr_simp:
            Frr = erf*(40 * i) *j
            Frr.append(Frr)
    
    return np.array(Frr)
