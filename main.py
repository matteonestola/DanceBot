import sys
import math


import time
import numpy as np
from naoqi import ALProxy
import m_Sit, m_SitRelax, m_Stand, m_StandInit, m_StandZero, m_Crouch
import i_clap
'''
import o_Arms_opening, o_Union_arms,o_Right_arm,o_Diagonal_right,o_Diagonal_left,o_Move_forward,o_Move_backward,o_Double_movement,o_Rotation_handgun_object
import testa_indietro ,testa_avanti,floss_0,floss_1,o_clap,dub_2 , dub

'''
robotIP = "127.0.0.1"
port = 38867

mandatoryPos = [m_StandInit,m_Sit]#[m_StandInit, m_Sit, m_SitRelax, m_Stand, m_StandZero, m_Crouch]
intermediatePos = [i_clap]

def execute_performance(x):
    try:
        motion = ALProxy("ALMotion", "127.0.0.1", port)
        motion.angleInterpolation(x.names, x.keys, x.times, True)
    except BaseException as err:
        print(err)

def execute_performanceBezier(x):
    try:
        motion = ALProxy("ALMotion", "127.0.0.1", port)
        motion.angleInterpolationBezier(x.names, x.times, x.keys)
    except BaseException as err:
        print(err)


# calculates the weight differences
def costDifference(coreValues1, coreValues2, coreValues3):
    return np.sum(np.abs(coreValues3-coreValues2) + np.abs(coreValues1-coreValues2))


def findTheNextNode():
    optimum = 100
    index = 0
    # picks up the most efficient position  & index
    for i in range(len(intermediatePos)):
        print("start")
        cost = costDifference(mandatoryPos[0], intermediatePos[i], mandatoryPos[1])
        print("end")
        if optimum > cost:
            optimum, index = cost, i
    print("Action chosen at index - ", index)
    execute_performance(intermediatePos[index])
    intermediatePos.pop(index)


def mainFunctionToRun():
   # m_StandInit.main("127.0.0.1", port)
    while len(mandatoryPos) != 1:
        #execute_performance(mandatoryPos[0])
        mandatoryPos[0].main(robotIP, port)
        findTheNextNode()
        mandatoryPos.pop(0)


mainFunctionToRun()












"""
# copy paste from here to below and leave the two lists below. This code is used to calculate the values of position which are most important from each action file
import numpy as np
# randomness for the movements
data = list()
data.append(np.std(keys[5]))
data.append(np.std(keys[6]))
data.append(np.std(keys[8]))
data.append(np.std(keys[10]))
data.append(np.std(keys[11]))
data.append(np.std(keys[12]))
data.append(np.std(keys[13]))
print("KeyValue ", data)
keysValue = list()
# ending positions for the moves
tempPositionValue = list()
tempPositionValue.append(keys[5][-1])
tempPositionValue.append(keys[6][-1])
tempPositionValue.append(keys[8][-1])
tempPositionValue.append(keys[10][-1])
tempPositionValue.append(keys[11][-1])
tempPositionValue.append(keys[12][-1])
tempPositionValue.append(keys[13][-1])
print("tempPosition ", tempPositionValue)
finalPositionValue = list()
x = np.hstack(times)
print("time taken", np.sum(times[0]))
# copy paste the printed value and uncomment
# keysValue = []
# finalPositionValue = []
"""