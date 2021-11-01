"""###########################################################################
#   This file contains subfunctions for Phase 1 of the TAMU MEEN 357 project
#
#   Created by: Jonathan Weaver-Rosen
#   Last Modified: 24 June 2021
###########################################################################"""

import math
import numpy as np
from numpy.core.defchararray import array
from define_experiment import experiment1 

def get_mass(rover):    
# Check that the input is a dict
    if type(rover) != dict:
        raise Exception('Input must be a dict')
    
    # add up mass of chassis, power subsystem, science payload, 
    # and components from all six wheel assemblies
    m = rover['chassis']['mass'] \
        + rover['power_subsys']['mass'] \
        + rover['science_payload']['mass'] \
        + 6*rover['wheel_assembly']['motor']['mass'] \
        + 6*rover['wheel_assembly']['speed_reducer']['mass'] \
        + 6*rover['wheel_assembly']['wheel']['mass'] \
    
    return m


def get_gear_ratio(speed_reducer):
    """
    Inputs:  speed_reducer:  dict      Data dictionary specifying speed
                                        reducer parameters
    Outputs:            Ng:  scalar    Speed ratio from input pinion shaft
                                        to output gear shaft. Unitless.
    """
    
    # Check that 1 input has been given.
    #   IS THIS NECESSARY ANYMORE????
    
    # Check that the input is a dict
    if type(speed_reducer) != dict:
        raise Exception('Input must be a dict')
    
    # Check 'type' field (not case sensitive)
    if speed_reducer['type'].lower() != 'reverted':
        raise Exception('The speed reducer type is not recognized.')
    
    # Main code
    d1 = speed_reducer['diam_pinion']
    d2 = speed_reducer['diam_gear']
    
    Ng = (d2/d1)**2
    
    return Ng


def tau_dcmotor(omega, motor):
    """
    Inputs:  omega:  numpy array      Motor shaft speed [rad/s]
             motor:  dict             Data dictionary specifying motor parameters
    Outputs:   tau:  numpy array      Torque at motor shaft [Nm].  Return argument
                                      is same size as first input argument.
    """
    
    # Check that 2 inputs have been given
    #   IS THIS NECESSARY ANYMORE????
    
    # Check that the first input is a scalar or a vector
    if (type(omega) != int) and (type(omega) != float) and (not isinstance(omega, np.ndarray)):
        raise Exception('First input must be a scalar or a vector. If input is a vector, it should be defined as a numpy array.')
    elif not isinstance(omega, np.ndarray):
        omega = np.array([omega],dtype=float) # make the scalar a numpy array
    elif len(np.shape(omega)) != 1:
        raise Exception('First input must be a scalar or a vector. Matrices are not allowed.')

    # Check that the second input is a dict
    if type(motor) != dict:
        raise Exception('Second input must be a dict')
        
    # Main code
    tau_s    = motor['torque_stall']
    tau_nl   = motor['torque_noload']
    omega_nl = motor['speed_noload']
    
    # initialize
    tau = np.zeros(len(omega),dtype = float)
    for ii in range(len(omega)):
        if omega[ii] >= 0 and omega[ii] <= omega_nl:
            tau[ii] = tau_s - (tau_s-tau_nl)/omega_nl *omega[ii]
        elif omega[ii] < 0:
            tau[ii] = tau_s
        elif omega[ii] > omega_nl:
            tau[ii] = 0
        
    return tau
    
    


def F_rolling(omega, terrain_angle, rover, planet, Crr):
    """
    Inputs:           omega:  numpy array     Motor shaft speed [rad/s]
              terrain_angle:  numpy array     Array of terrain angles [deg]
                      rover:  dict            Data structure specifying rover 
                                              parameters
                    planet:  dict            Data dictionary specifying planetary 
                                              parameters
                        Crr:  scalar          Value of rolling resistance coefficient
                                              [-]
    
    Outputs:           Frr:  numpy array     Array of forces [N]
    """
    
    # Check that the first input is a scalar or a vector
    if (type(omega) != int) and (type(omega) != float) and (not isinstance(omega, np.ndarray)):
        raise Exception('First input must be a scalar or a vector. If input is a vector, it should be defined as a numpy array.')
    elif not isinstance(omega, np.ndarray):
        omega = np.array([omega],dtype=float) # make the scalar a numpy array
    elif len(np.shape(omega)) != 1:
        raise Exception('First input must be a scalar or a vector. Matrices are not allowed.')
        
    # Check that the second input is a scalar or a vector
    if (type(terrain_angle) != int) and (type(terrain_angle) != float) and (not isinstance(terrain_angle, np.ndarray)):
        raise Exception('Second input must be a scalar or a vector. If input is a vector, it should be defined as a numpy array.')
    elif not isinstance(terrain_angle, np.ndarray):
        terrain_angle = np.array([terrain_angle],dtype=float) # make the scalar a numpy array
    elif len(np.shape(terrain_angle)) != 1:
        raise Exception('Second input must be a scalar or a vector. Matrices are not allowed.')
        
    # Check that the first two inputs are of the same size
    if len(omega) != len(terrain_angle):
        raise Exception('First two inputs must be the same size')
    
    # Check that values of the second input are within the feasible range  
    if max([abs(x) for x in terrain_angle]) > 75:    
        raise Exception('All elements of the second input must be between -75 degrees and +75 degrees')
        
    # Check that the third input is a dict
    if type(rover) != dict:
        raise Exception('Third input must be a dict')
        
    # Check that the fourth input is a dict
    if type(planet) != dict:
        raise Exception('Fourth input must be a dict')
        
    # Check that the fifth input is a scalar and positive
    if (type(Crr) != int) and (type(Crr) != float):
        raise Exception('Fifth input must be a scalar')
    if Crr <= 0:
        raise Exception('Fifth input must be a positive number')
        
    # Main Code
    m = get_mass(rover)
    g = planet['g']
    r = rover['wheel_assembly']['wheel']['radius']
    Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])#['type'])
    
    v_rover = r*omega/Ng
    
    Fn = np.array([m*g*math.cos(math.radians(x)) for x in terrain_angle],dtype=float) # normal force
    Frr_simple = -Crr*Fn # simple rolling resistance
    
    Frr = np.array([math.erf(40*v_rover[ii]) * Frr_simple[ii] for ii in range(len(v_rover))], dtype = float)
    
    return Frr


def F_gravity(terrain_angle, rover, planet):
    """
    Inputs:  terrain_angle:  numpy array   Array of terrain angles [deg]
                     rover:  dict          Data structure specifying rover 
                                            parameters
                    planet:  dict          Data dictionary specifying planetary 
                                            parameters
    
    Outputs:           Fgt:  numpy array   Array of forces [N]
    """
    
    # Check that the first input is a scalar or a vector
    if (type(terrain_angle) != int) and (type(terrain_angle) != float) and (not isinstance(terrain_angle, np.ndarray)):
        raise Exception('First input must be a scalar or a vector. If input is a vector, it should be defined as a numpy array.')
    elif not isinstance(terrain_angle, np.ndarray):
        terrain_angle = np.array([terrain_angle],dtype=float) # make the scalar a numpy array
    elif len(np.shape(terrain_angle)) != 1:
        raise Exception('First input must be a scalar or a vector. Matrices are not allowed.')
        
    # Check that values of the first input are within the feasible range  
    if max([abs(x) for x in terrain_angle]) > 75:    
        raise Exception('All elements of the first input must be between -75 degrees and +75 degrees')

    # Check that the second input is a dict
    if type(rover) != dict:
        raise Exception('Second input must be a dict')
    
    # Check that the third input is a dict
    if type(planet) != dict:
        raise Exception('Third input must be a dict')
        
    # Main Code
    m = get_mass(rover)
    g = planet['g']
    
    Fgt = np.array([-m*g*math.sin(math.radians(x)) for x in terrain_angle], dtype = float)
        
    return Fgt


def F_drive(omega, rover):
    """
    Inputs:  omega:  numpy array   Array of motor shaft speeds [rad/s]
             rover:  dict          Data dictionary specifying rover parameters
    
    Outputs:    Fd:  numpy array   Array of drive forces [N]
    """
    
    # Check that 2 inputs have been given.
    #   IS THIS NECESSARY ANYMORE????
    
    # Check that the first input is a scalar or a vector
    if (type(omega) != int) and (type(omega) != float) and (not isinstance(omega, np.ndarray)):
        raise Exception('First input must be a scalar or a vector. If input is a vector, it should be defined as a numpy array.')
    elif not isinstance(omega, np.ndarray):
        omega = np.array([omega],dtype=float) # make the scalar a numpy array
    elif len(np.shape(omega)) != 1:
        raise Exception('First input must be a scalar or a vector. Matrices are not allowed.')

    # Check that the second input is a dict
    if type(rover) != dict:
        raise Exception('Second input must be a dict')
    
    # Main code
    Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])
    
    tau = tau_dcmotor(omega, rover['wheel_assembly']['motor'])
    tau_out = tau*Ng
    
    r = rover['wheel_assembly']['wheel']['radius']
    
    # Drive force for one wheel
    Fd_wheel = tau_out/r 
    
    # Drive force for all six wheels
    Fd = 6*Fd_wheel
    
    return Fd


def F_net(omega, terrain_angle, rover, planet, Crr):
    """
    Inputs:           omega:  list     Motor shaft speed [rad/s]
              terrain_angle:  list     Array of terrain angles [deg]
                      rover:  dict     Data structure specifying rover 
                                      parameters
                     planet:  dict     Data dictionary specifying planetary 
                                      parameters
                        Crr:  scalar   Value of rolling resistance coefficient
                                      [-]
    
    Outputs:           Fnet:  list     Array of forces [N]
    """
    
    # Check that the first input is a scalar or a vector
    if (type(omega) != int) and (type(omega) != float) and (not isinstance(omega, np.ndarray)):
        raise Exception('First input must be a scalar or a vector. If input is a vector, it should be defined as a numpy array.')
    elif not isinstance(omega, np.ndarray):
        omega = np.array([omega],dtype=float) # make the scalar a numpy array
    elif len(np.shape(omega)) != 1:
        raise Exception('First input must be a scalar or a vector. Matrices are not allowed.')
        
    # Check that the second input is a scalar or a vector
    if (type(terrain_angle) != int) and (type(terrain_angle) != float) and (not isinstance(terrain_angle, np.ndarray)):
        #raise Exception('Second input must be a scalar or a vector. If input is a vector, it should be defined as a numpy array.')
        print('the angle is', type(terrain_angle))
    elif not isinstance(terrain_angle, np.ndarray):
        terrain_angle = np.array([terrain_angle],dtype=float) # make the scalar a numpy array
    elif len(np.shape(terrain_angle)) != 1:
        raise Exception('Second input must be a scalar or a vector. Matrices are not allowed.')
        
    # Check that the first two inputs are of the same size
    if len(omega) != len(terrain_angle):
        raise Exception('First two inputs must be the same size')
        
    
    # Check that values of the second input are within the feasible range  
    if max([abs(x) for x in terrain_angle]) > 75:    
        raise Exception('All elements of the second input must be between -75 degrees and +75 degrees')
        
    # Check that the third input is a dict
    if type(rover) != dict:
        raise Exception('Third input must be a dict')
        
    # Check that the fourth input is a dict
    if type(planet) != dict:
        raise Exception('Fourth input must be a dict')
        
    # Check that the fifth input is a scalar and positive
    if (type(Crr) != int) and (type(Crr) != float):
        raise Exception('Fifth input must be a scalar')
    if Crr <= 0:
        raise Exception('Fifth input must be a positive number')
    
    # Main Code
    Fd = F_drive(omega, rover)
    Frr = F_rolling(omega, terrain_angle, rover, planet, Crr)
    Fg = F_gravity(terrain_angle, rover, planet)
    
    Fnet = Fd + Frr + Fg # signs are handled in individual functions
    
    return Fnet



def motorW(omega, rover):
    #Compute the rotational speed of the motor shaft [rad/s]
    # given the translational velocity of the rover and the roverdictionary.
    # 
    #This function should be “vectorized” such that if given a vector of rover velocities
    # it returns a vector the same size containing the corresponding motor speeds. 

    #if (type(omega) != int) and (type(omega) != float) and (not isinstance(omega, np.ndarray)):
    #    raise Exception('First input must be a scalar or a vector. If input is a vector, it should be defined as a numpy array.')
    if not isinstance(omega, np.ndarray):
        omega = np.array([omega],dtype=float) # make the scalar a numpy array
    elif len(np.shape(omega)) != 1:
        raise Exception('First input must be a scalar or a vector. Matrices are not allowed.')
    
    if type(rover) != dict:
        raise Exception('Third input must be a dict')
    omega_nl = rover['wheel_assembly']['motor']['speed_noload']
    Ng = get_gear_ratio(rover['wheel_assembly']['speed_reducer'])

    r_wheel = rover['wheel_assembly']['wheel']['radius'] # raius in meters
    
    w = np.zeros(len(omega),dtype = float)
    for ii in range(len(omega)):
        if omega[ii]/r_wheel *Ng >= 0 and omega[ii] <= omega_nl:  # compares maximum no load motor conidion to given motor condition
            w[ii] = omega[ii]/r_wheel *Ng
            # is this math right? 

        elif omega[ii] < 0: # ensures givn v is positive
            raise Exception('given v should be positive')
        elif omega[ii]/r_wheel *Ng > omega_nl: # sets v to 0 if it is too large
            w[ii] = 0
            # Is this an ok interprestaiton ^
    return w
    

def alpha_fun(y):
    experiment = experiment1()[0]
    alpha_dist = experiment['alpha_dist']
    alpha_deg = experiment['alpha_deg']
    alpha_fun = interp1d(alpha_dist, alpha_deg, kind = 'cubic', fill_value= "extrapolate") # fit the cubic spline

    return alpha_fun 



def rover_dynamics(t, y, rover, planet, experiment):
    # if not isinstance(omega, np.ndarray):
    #     omega = np.array([omega],dtype=float) # make the scalar a numpy array
    # elif len(np.shape(omega)) != 1:
    #     raise Exception('First input must be a scalar or a vector. Matrices are not allowed.')
    #print(type(t)) 
    #print(len(t))
    #print("this is a numpy floatS",not(isinstance(t,np.float64)))
    
    
    
    
    #ASK PROFESSOR
    # if (type(t) != isinstance(t,float) and not(isinstance(t,np.float64)) and not(0.0)):
    #     #raise Exception('First input must be a scalar')
    #     print("\n\nit not a float", type(t),t)
   
    
   
    if not isinstance(y, np.ndarray):
        y= np.array([y],dtype=float) # make the scalar a numpy array
    elif len(np.shape(y)) != 1:
        raise Exception('Second input must be a scalar or a vector. Matrices are not allowed.')
        
    if type(rover) != dict:
        raise Exception('Third input must be a dict')
        
    if type(planet) != dict:
        raise Exception('Fourth input must be a dict')
        
    if type(experiment) != dict:
        raise Exception('Fifth input mustt be a dict')
    
    
    alpha_dist = experiment['alpha_dist']
    alpha_deg = experiment['alpha_deg']
    alpha_fun = interp1d(alpha_dist, alpha_deg, kind = 'cubic') # fit the cubic spline
    terrain_angle = alpha_fun(y[1])
    terrain_angle = terrain_angle.tolist()
    
    w = motorW(y[0],rover) #y[0] is velocity, dx/dt
    Fnet = F_net(w, terrain_angle, rover, planet, Crr)
    m = get_mass(rover)
    
    dy1dt = y[0] #y[0] is velocity dy/dx
    dy2dt = Fnet / m
    dydt = np.array([dy2dt, dy1dt], dtype=object)
    return dydt
    



    
    
#############
# Test Code #
#############
from scipy.interpolate import interp1d
from scipy.integrate import solve_ivp
from define_rovers import define_rover_4
from define_experiment import experiment1
from end_of_mission_event import end_of_mission_event
import numpy as np
#from Project_Phase_1_Codes.subfunctions import get_mass(), F_net(), motorW()


experiment = experiment1()[0]
t0 = experiment['time_range'][0] #initial time [s]
te = experiment['time_range'][1] #final time [s]
Crr = experiment['Crr']
planet= define_rover_4()[1]

y0 = experiment1()[0]['initial_conditions']
rover = define_rover_4()[0]
speed_reducer = define_rover_4()[0]['wheel_assembly']['speed_reducer']


V = np.array([1,0]) #get from experiment rover['telementry']['velocity']
X = np.array([0,2]) # get form experm rover['telementry']['position']
y = np.array([V,X])

#y = [[rover['telementry']['velocity']], [rover['telementry']['position']]] #2D velocity/position array
y1 = y[0] #v
y2 = y[1] #x
m = get_mass(rover)


fun = lambda t, y: rover_dynamics(t, y, rover, planet, experiment)
tspan = np.array([t0, te])
end_event = experiment1()[1]
events = end_of_mission_event(end_event)


sol = solve_ivp(fun, tspan, y0, method= 'RK45', events=events)
print(sol)
