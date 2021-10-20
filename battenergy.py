#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:44:46 2021

@author: laurenberryman
"""
#### This function called battenergy, will compute the total electrical energy consumed
#### from the rover battery pack over a simulation profile, defines as time-velocity pairs.

### This function assumes all six motors are driven from the same battery pack.


def battenergy(t, v, rover):
    """ 
    Inputs:      t:  1D numpy array       N-element array of time samples from a rover simulation [s]
                 v:  1D numpy array       N-element array of rover velocity data from a simulation [m/s]
             rover:  dict                 Data structure containing rover definition
             
    Outputs:     E:  scalar               Total electrical energy consumed from the rover battery pack
                                          over the input simulation profile. [J]
        
    """
    #check that the first input is a numpy array
    if (type(t) != int) and (type(t) != float) and (not isinstance(t, np.ndarray)):
        raise Exception('First input must be a scalar or a vector. If input is a vector, it should be defined as a numpy array.')
    elif not isinstance(t, np.ndarray):
        t = np.array([t],dtype=float) # make the scalar a numpy array
    elif len(np.shape(t)) != 1:
        raise Exception('First input must be a scalar or a vector. Matrices are not allowed.')
        
        #check that second input is a numpy array
        if (type(v) != int) and (type(v) != float) and (not isinstance(v, np.ndarray)):
            raise Exception('Second input must be a scalar or a vector. If input is a vector, it should be defined as a numpy array.')
    elif not isinstance(v, np.ndarray):
        v = np.array([v],dtype=float) # make the scalar a numpy array
    elif len(np.shape(v)) != 1:
        raise Exception('Second input must be a scalar or a vector. Matrices are not allowed.')
        
    # check that the first two inputs are equal-length vectors
    # MAY NOT BE RIGHT WAY TO SAY THIS (could try if both do not equal 1, then raise exception)
    if len(np.shape(t)) != len(np.shape(v)):
        raise Exception("The first two inputs must be equal-length vectors of numerical values")
        
    # check that the third input is a dictionary
    if type(rover) != dict:
        raise Exception("Third input must be a dictionary")
        
    # MAIN CODE
    
        
    
        
    
            
























# Inserting the functions that are needed to complete the battenergy function

# tau_dcmotor function

import math
import numpy as np

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

# mechpower function


