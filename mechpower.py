#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:23:07 2021

@author: laurenberryman
"""

#### This function computes the instantaneous mechanical power output by a single DC motor
#### at each point in a given velocity profile.
import numpy as np
import math

def mechpower(v, rover):
    """ 
    Inputs:        v:   1D numpy array OR scalar float/int       Rover velocity data obtained from a simulation [m/s]
               rover:   dict                                     Data structure containing rover definition
   
    Outputs:      P:    1D numpy array OR scalar float/int       Instantaneous power output of a single motor
                                                                corresponding to each element in v [W]. Return
                                                                argument should be the same size as input v.
    
    """
    # check that the first input is a numpy array OR a scalar float/int
    if (type(v) != int) and (type(v) != float) and (not isinstance(v, np.ndarray)):
        raise Exception('First input must be a scalar or a vector. If input is a vector, it should be defined as a numpy array.')
    elif not isinstance(v, np.ndarray):
        v = np.array([v],dtype=float) # make the scalar a numpy array
    elif len(np.shape(v)) != 1:
        raise Exception('First input must be a scalar or a vector. Matrices are not allowed.')
        
    # check that the second input is a dictionary
    if type(rover) != dict:
        raise Exception("Third input must be a dictionary")
        
        
    #MAIN CODE
    
    