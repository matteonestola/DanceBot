import sys
import math


import time
import numpy as np

import i_dance_move
import i_finger_face
import i_front_arms
import i_one_foot_hand_up
import i_random_robot
import i_shuffle
import i_start_2
from naoqi import ALProxy
import m_Sit, m_SitRelax, m_Stand, m_StandInit, m_StandZero, m_Crouch, m_Wipe_Forehead, m_Hello
import i_clap, i_disco, i_macarena, i_blow, i_blow_kisses, i_sprinkler, i_the_robot_2, i_GangamStyle, i_thriller, i_arm_dance, i_hips, i_wave_stand_up
import i_start, i_up_down_hands, i_head_flex, i_ext_clap, i_sit_dance
import i_waving_pos, i_Right_arm, o_Diagonal_right, o_Diagonal_left,i_Union_arms, o_Arms_opening, i_Move_forward, i_Move_backward, i_Double_movement, o_Rotation_handgun_object, o_Rotation_foot_LLeg, o_Rotation_foot_RLeg
'''
import o_Arms_opening, o_Union_arms,o_Right_arm,o_Diagonal_right,o_Diagonal_left,o_Move_forward,o_Move_backward,o_Double_movement,o_Rotation_handgun_object
import testa_indietro ,testa_avanti,floss_0,floss_1,o_clap,dub_2 , dub

'''
robotIP = "127.0.0.1"
port = 36377

mandatoryPos = [m_StandInit, m_Sit, m_SitRelax, m_Stand, m_StandZero, m_Wipe_Forehead, m_Hello, m_Crouch]
intermediatePos = [i_clap, i_disco, i_macarena, i_blow, i_blow_kisses, i_sprinkler, i_the_robot_2, i_GangamStyle, i_thriller, i_arm_dance, i_hips, i_wave_stand_up]

def execute_performance(x):
    try:
        motion = ALProxy("ALMotion", "127.0.0.1", port)
        motion.angleInterpolation(x.names, x.keys, x.times, True)
    except BaseException as err:
        print(err)
    try:
        x.main(robotIP, port)
    except BaseException as err:
        print(err)

def execute_performanceBezier(x):
    try:
        motion = ALProxy("ALMotion", "127.0.0.1", port)
        motion.angleInterpolationBezier(x.names, x.times, x.keys)
    except BaseException as err:
        print(err)
    try:
        x.main(robotIP, port)
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

def Nao_say(message):
    try:
        ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e
    ttsProxy.say(message)
    time.sleep(2)

def name_pos(s):
    return s.split('positions/')[1].split('.pyc')[0]

def t_def(start, n_value, step):
    x = start
    L = list()
    L.append(x)
    for i in range(0, n_value):
        x = round(x + step, 2)
        L.append(x)

    return L

def mainFunctionToRun():
    for i in intermediatePos:

        #Nao_say(name_pos(str(i)))
        execute_performance(i)
        #execute_performance(mandatoryPos[0])


#mainFunctionToRun()


'''
#SEQUENZA BALLO
execute_performance(mandatoryPos[0]) # m_StandInit M
execute_performanceBezier(i_start) #pos_1
execute_performanceBezier(i_up_down_hands) # pos 2
execute_performanceBezier(i_head_flex) #pos 3
execute_performanceBezier(i_front_arms) # pos front_arms
execute_performanceBezier(i_ext_clap) # pos 4
execute_performanceBezier(i_arm_dance) # balla con le mani
execute_performanceBezier(mandatoryPos[1]) #m_Sit M
execute_performanceBezier(i_sit_dance) #pos_5
execute_performanceBezier(mandatoryPos[3]) # m_Stand M
execute_performanceBezier(i_one_foot_hand_up) # pos_6
execute_performanceBezier(i_shuffle) # pos_7
execute_performanceBezier(i_random_robot) # the robot
execute_performanceBezier(i_dance_move) # dance move
execute_performanceBezier(i_finger_face) # pos_8
execute_performanceBezier(mandatoryPos[2]) # sitRelax M
execute_performanceBezier(i_waving_pos) # pos_9
execute_performanceBezier(i_Right_arm) # pos_9
execute_performanceBezier(mandatoryPos[4]) # m_StandZero M
execute_performanceBezier(i_Union_arms) # pos_10
execute_performanceBezier(i_Move_forward) # pos_11
execute_performanceBezier(i_Move_backward) # pos_12
execute_performanceBezier(i_Double_movement) # pos_13
execute_performanceBezier(mandatoryPos[5]) # m_Wipe_ForeHead M
execute_performanceBezier(mandatoryPos[6]) # m_Hello M
execute_performanceBezier(mandatoryPos[7]) # m_Crouch M
'''
execute_performanceBezier(mandatoryPos[3])
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