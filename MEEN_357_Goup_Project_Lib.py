import numpy as np

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


def F_gravity(terrain_angle, rover, planet):
    import numpy as np
    terrain_angle = np.array([])
    # need the mass of the entire rover
    m = get_mass(rover)
    mass = rover
    rover("mass") 

    return
