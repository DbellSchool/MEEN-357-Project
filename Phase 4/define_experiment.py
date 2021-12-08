"""###########################################################################
#   This file initializes the experiment and end_event structures for 
#   MEEN 357 project phase 4.
#
#   Created by: MARVIN TERRAIN ANALYSIS TEAM
#   Last Modified: 19 November 2021
###########################################################################"""

import numpy as np
import random as rand

from scipy.sparse.construct import random

def experiment1():
    
    experiment = {'time_range' : np.array([0,20000]),
                  'initial_conditions' : np.array([0.3125,0]),
                  'alpha_dist' : np.array([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]),
                  'alpha_deg' : np.array([11.509, 2.032, 7.182, 2.478, \
                                        5.511, 10.981, 5.601, -0.184, \
                                        0.714, 4.151, 4.042]),
                  'Crr' : 0.1}
    
    end_event = {'max_distance' : 1000,
                 'max_time' : 5000,
                 'min_velocity' : 0.01}
    
    return experiment, end_event

def experiment2():
    
    experiment = {'time_range' : np.array([0,20000]),
                  'initial_conditions' : np.array([0.3125,0]),
                  'alpha_dist' : np.array([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]),
                  'alpha_deg' : np.array(rand.sample(range(-10, 15),11)),
                  'Crr' : 0.1}
    
    end_event = {'max_distance' : 1000,
                 'max_time' : 5000,
                 'min_velocity' : 0.01}
    
    return experiment, end_event

def experiment3():
    
    experiment = {'time_range' : np.array([0,20000]),
                  'initial_conditions' : np.array([0.3125,0]),
                  'alpha_dist' : np.array([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]),
                  'alpha_deg' : np.array( [-8, -6 ,-5 , 3 , 2 ,-7 ,-2 ,14 , 0 , 1 ,10]),
                  'Crr' : 0.1}
    
    end_event = {'max_distance' : 1000,
                 'max_time' : 5000,
                 'min_velocity' : 0.01}
    
    return experiment, end_event


def experiment4():
    
    experiment = {'time_range' : np.array([0,20000]),
                  'initial_conditions' : np.array([0.3125,0]),
                  'alpha_dist' : np.array([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]),
                  'alpha_deg' : np.array( [ 7,  2, 13,  8, -2 ,10, -5 , 3,  6,  9, 12]),
                  'Crr' : 0.1}
    
    end_event = {'max_distance' : 1000,
                 'max_time' : 5000,
                 'min_velocity' : 0.01}
    
    return experiment, end_event


