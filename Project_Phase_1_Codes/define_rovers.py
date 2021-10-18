"""###########################################################################
#   This file initializes a rover structure for testing/grading
#
#   Created by: Jonathan Weaver-Rosen
#   Last Modified: 11 October 2021
###########################################################################"""

from numpy.lib.shape_base import _dstack_dispatcher
from numpy import array


def define_rover_1():
    # Initialize Rover dict for testing
    wheel = {'radius':0.30,
             'mass':1}
    speed_reducer = {'type':'reverted',
                     'diam_pinion':0.04,
                     'diam_gear':0.07,
                     'mass':1.5}
    motor = {'torque_stall':170,
             'torque_noload':0,
             'speed_noload':3.80,
             'mass':5.0}
    
        
    chassis = {'mass':659}
    science_payload = {'mass':75}
    power_subsys = {'mass':90}
    
    wheel_assembly = {'wheel':wheel,
                      'speed_reducer':speed_reducer,
                      'motor':motor}
    
    rover = {'wheel_assembly':wheel_assembly,
             'chassis':chassis,
             'science_payload':science_payload,
             'power_subsys':power_subsys}
    
    planet = {'g':3.72}
    
    # return everything we need
    return rover, planet

def define_rover_2():
    # Initialize Rover dict for testing
    wheel = {'radius':0.30,
             'mass':2} 
    speed_reducer = {'type':'reverted',
                     'diam_pinion':0.04,
                     'diam_gear':0.06,
                     'mass':1.5}
    motor = {'torque_stall':180,
             'torque_noload':0,
             'speed_noload':3.70,
             'mass':5.0}    
    
    chassis = {'mass':659}
    science_payload = {'mass':75}
    power_subsys = {'mass':90}
    
    wheel_assembly = {'wheel':wheel,
                      'speed_reducer':speed_reducer,
                      'motor':motor}
    
    rover = {'wheel_assembly':wheel_assembly,
             'chassis':chassis,
             'science_payload':science_payload,
             'power_subsys':power_subsys}
    
    planet = {'g':3.72}
    
    # return everything we need
    return rover, planet

def define_rover_3():
    # Initialize Rover dict for testing
    wheel = {'radius':0.30,
             'mass':2} 
    speed_reducer = {'type':'standard',
                     'diam_pinion':0.04,
                     'diam_gear':0.06,
                     'mass':1.5}
    motor = {'torque_stall':180,
             'torque_noload':0,
             'speed_noload':3.70,
             'mass':5.0}
    
    chassis = {'mass':659}
    science_payload = {'mass':75}
    power_subsys = {'mass':90}
    
    wheel_assembly = {'wheel':wheel,
                      'speed_reducer':speed_reducer,
                      'motor':motor}
    
    rover = {'wheel_assembly':wheel_assembly,
             'chassis':chassis,
             'science_payload':science_payload,
             'power_subsys':power_subsys}
    
    planet = {'g':3.72}
    
    # return everything we need
    return rover, planet

def define_rover_4():
    # Initialize Rover dict for testing
    wheel = {'radius':0.30,
             'mass':2} 
    speed_reducer = {'type':'reverted',
                     'diam_pinion':0.04,
                     'diam_gear':0.06,
                     'mass':1.5}
    motor = {'torque_stall':180,
             'torque_noload':0,
             'speed_noload':3.70,
             'mass':5.0,
             'effcy_tau': array([0,10,20,40,75,165]),
             'effcy' : array([0,0.6,0.75,0.73,0.55,0.05])}
    
    chassis = {'mass':659}
    science_payload = {'mass':75}
    power_subsys = {'mass':90}
    
    wheel_assembly = {'wheel':wheel,
                      'speed_reducer':speed_reducer,
                      'motor':motor}
    
    rover = {'wheel_assembly':wheel_assembly,
             'chassis':chassis,
             'science_payload':science_payload,
             'power_subsys':power_subsys}

    
    planet = {'g':3.72}
    
    # return everything we need
    return rover, planet
    