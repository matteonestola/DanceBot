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
#from naoPlanning import NaoProblem
from naoqi import ALProxy
import m_Sit, m_SitRelax, m_Stand, m_StandInit, m_StandZero, m_Crouch, m_Wipe_Forehead, m_Hello
import i_clap, i_disco, i_macarena, i_blow, i_blow_kisses, i_sprinkler, i_the_robot_2, i_GangamStyle, i_thriller, \
    i_arm_dance, i_hips, i_wave_stand_up
import i_start, i_up_down_hands, i_head_flex, i_ext_clap, i_sit_dance
import i_waving_pos, i_Right_arm, i_Union_arms, i_Move_forward, i_Move_backward, i_Double_movement

'''
import o_Arms_opening, o_Union_arms,o_Right_arm,o_Diagonal_right,o_Diagonal_left,o_Move_forward,o_Move_backward,o_Double_movement,o_Rotation_handgun_object
import testa_indietro ,testa_avanti,floss_0,floss_1,o_clap,dub_2 , dub

'''
robotIP = "127.0.0.1"
port = 36377


# mandatoryPos = [m_StandInit, m_Sit, m_SitRelax, m_Stand, m_StandZero, m_Wipe_Forehead, m_Hello, m_Crouch]
# intermediatePos = [i_clap, i_disco, i_macarena, i_blow, i_blow_kisses, i_sprinkler, i_the_robot_2, i_GangamStyle, i_thriller, i_arm_dance, i_hips, i_wave_stand_up]

def execute_performance(x):
    try:
        motion = ALProxy("ALMotion", "127.0.0.1", port)
        start = time.time()
        motion.angleInterpolation(x.names, x.keys, x.times, True)
        end = time.time()
        print("%.2f seconds" % (end - start))
    except BaseException as err:
        print(err)
    try:
        x.main(robotIP, port)
    except BaseException as err:
        print(err)


def execute_performanceBezier(x):
    try:
        motion = ALProxy("ALMotion", "127.0.0.1", port)
        start = time.time()
        motion.angleInterpolationBezier(x.names, x.times, x.keys)
        end = time.time()
        print("%.2f seconds" % (end - start))
    except BaseException as err:
        print(err)
    try:
        start = time.time()
        x.main(robotIP, port)
        end = time.time()
        print("%.2f seconds" % (end - start))
    except BaseException as err:
        print(err)


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


def sum_time_mandatory():
    sum = 0.0
    sum += initialPos[1][2]
    sum += goalPos[1][2]
    for i in mandatoryPos:
        sum += i[1][2]
    return sum


class Move:
    def __init__(self, preConditions, postConditions, time):
        self.preConditions = preConditions if preConditions is not None else {}
        self.postConditions = postConditions if postConditions is not None else {}
        self.time = time


'''
True if Nao standing
False otherwise
'''
'''
intermediatePos = { 'i_start': Move(True, True, 9.60),
                    'i_up_down_hands': Move(True, True, 5.90),
                    'i_head_flex': Move(True, True, 7.25),
                    'i_front_arms': Move(True, True, 0.05),
                    'i_ext_clap': Move(True, True, 5.63),
                    'i_arm_dance': Move(True, True, 19.90),
                    'i_sit_dance': Move(False, False, 12.04),
                    'i_one_foot_hand_up': Move(None, True, 5.90),
                    'i_shuffle': Move(True, True, 8.83),
                    'i_random_robot': Move(True, True, 6.45),
                    'i_dance_move': Move(True, True, 6.02),
                    'i_finger_face': Move(True, True, 5.63),
                    'i_waving_pos': Move(False, False, 18.55),
                    'i_Right_arm': Move(None, None, 9.05),
                    'i_Union_arms': Move(None, None, 8.80),
                    'i_Move_forward': Move(True, True, 2.70),
                    'i_Move_backward': Move(True, True, 2.70),
                    'i_Double_movement': Move(True, True, 6.55)
                    }
# mandatoryPos = [m_StandInit, m_Sit, m_SitRelax, m_Stand, m_StandZero, m_Wipe_Forehead, m_Hello, m_Crouch]
initialPos = ('m_StandInit', Move(None, True, 0.05))
mandatoryPos = [
                ('m_Sit', Move(True, False, 9.1)),
                ('m_SitRelax', Move(True, False, 11.48)),
                ('m_Stand', Move(False, True, 11.32)),
                ('m_StandZero', Move(True, True, 8.28)),
                ('m_Wipe_Forehead', Move(None, None, 5.13)), # mettere ture al posto di None

                ('m_Hello', Move(False, False, 4.66))
                ]
goalPos = ('m_Crouch', Move(True, None, 3.05))
'''
intermediatePos = {'i_start': [True, True, 9.60],
                   'i_up_down_hands': [True, True, 5.90],
                   'i_head_flex': [True, True, 7.25],
                   'i_front_arms': [True, True, 0.05],
                   'i_ext_clap': [True, True, 5.63],
                   'i_arm_dance': [True, True, 19.90],
                   'i_sit_dance': [False, False, 12.04],
                   'i_one_foot_hand_up': [None, True, 5.90],
                   'i_shuffle': [True, True, 8.83],
                   'i_random_robot': [True, True, 6.45],
                   'i_dance_move': [True, True, 6.02],
                   'i_finger_face': [True, True, 5.63],
                   'i_waving_pos': [False, False, 18.55],
                   'i_Right_arm': [None, None, 9.05],
                   'i_Union_arms': [None, None, 8.80],
                   'i_Move_forward': [True, True, 2.70],
                   'i_Move_backward': [True, True, 2.70],
                   'i_Double_movement': [True, True, 6.55]
                   }
# mandatoryPos = [m_StandInit, m_Sit, m_SitRelax, m_Stand, m_StandZero, m_Wipe_Forehead, m_Hello, m_Crouch]
initialPos = ('m_StandInit', [None, True, 0.05])
mandatoryPos = [
    ('m_Sit', [True, False, 9.1]),
    ('m_Stand', [False, True, 11.32]),
    ('m_SitRelax', [True, False, 11.48]),
    ('m_StandZero', [True, True, 8.28]),
    ('m_Wipe_Forehead', [None, None, 5.13]),  # mettere ture al posto di None
    ('m_Hello', [False, False, 4.66])
]
goalPos = ('m_Crouch', [True, None, 3.05])

totalMandatory = [('m_StandInit', [None, True, 0.05]),
                  ('m_Sit', [True, False, 9.1]),
                  ('m_Stand', [False, True, 11.32]),
                  ('m_SitRelax', [True, False, 11.48]),
                  ('m_StandZero', [True, True, 8.28]),
                  ('m_Wipe_Forehead', [None, None, 5.13]),  # mettere ture al posto di None
                  ('m_Hello', [False, False, 4.66]),
                  ('m_Crouch', [True, None, 3.05])
                  ]

remaining_time = 180.0 - sum_time_mandatory()  # tempo che resta per eseguire le intermediate positions
print "remaining time fo the execution of intermediate positions:", remaining_time
intermediate_time = remaining_time / 7
print(intermediate_time)
# START PLANNING
solution = list()

for i in range(1, len(totalMandatory)):
    # mossa in cui mi trovo
    startPos = (('namePos', totalMandatory[i - 1][0]),
                ('preconditions', totalMandatory[i - 1][1][0]),
                ('postconditions', totalMandatory[i - 1][1][1]),
                ('intermediate_time', intermediate_time),
                ('move_time', totalMandatory[i - 1][1][2])
                )

    # mossa da raggiungere
    endPos = (('namePos', totalMandatory[i][0]),
              ('preconditions', totalMandatory[i][1][0]),
              ('postconditions', totalMandatory[i][1][1]),
              ('intermediate_time', 0),
              ('move_time', totalMandatory[i][1][2])
              )

    moveProblem = NaoProblem(startPos, endPos, intermediatePos, solution)



def mainFunctionToRun():
    # SEQUENZA BALLO
    execute_performance(m_StandInit)  # m_StandInit M
    execute_performanceBezier(i_start)  # pos_1
    execute_performanceBezier(i_up_down_hands)  # pos 2
    execute_performanceBezier(i_head_flex)  # pos 3
    execute_performanceBezier(i_front_arms)  # pos front_arms
    execute_performanceBezier(i_ext_clap)  # pos 4
    execute_performanceBezier(i_arm_dance)  # balla con le mani
    execute_performanceBezier(m_Sit)  # m_Sit M
    execute_performanceBezier(i_sit_dance)  # pos_5
    execute_performanceBezier(m_Stand)  # m_Stand M
    execute_performanceBezier(i_one_foot_hand_up)  # pos_6
    execute_performanceBezier(i_shuffle)  # pos_7
    execute_performanceBezier(i_random_robot)  # the robot
    execute_performanceBezier(i_dance_move)  # dance move
    execute_performanceBezier(i_finger_face)  # pos_8
    execute_performanceBezier(m_SitRelax)  # sitRelax M
    execute_performanceBezier(i_waving_pos)  # pos_9
    execute_performanceBezier(i_Right_arm)  # pos_9
    execute_performanceBezier(m_StandZero)  # m_StandZero M
    execute_performanceBezier(i_Union_arms)  # pos_10
    execute_performanceBezier(i_Move_forward)  # pos_11
    execute_performanceBezier(i_Move_backward)  # pos_12
    execute_performanceBezier(i_Double_movement)  # pos_13
    execute_performanceBezier(m_Wipe_Forehead)  # m_Wipe_ForeHead M
    execute_performanceBezier(m_Hello)  # m_Hello M
    execute_performanceBezier(m_Crouch)  # m_Crouch M

# mainFunctionToRun()

# execute_performanceBezier(m_Crouch)
