# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([-0.162963, 0.157492, -0.0167621, -0.0167621, -0.0167621, 0.196309, -0.17])

names.append("HeadYaw")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([7.28101e-05, 0.0431964, 0.253671, -0.581238, 0.259204, -0.144091, 0.00751492])

names.append("LAnklePitch")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.0847712, 0.0118041, 0.0139817, 0.129815, 0.0274242, 0.0437338, 0.0832693])

names.append("LAnkleRoll")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([-0.12974, 0.0521581, 0.117753, -0.232642, 0.11649, -0.178139, -0.128971])

names.append("LElbowRoll")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([-0.418659, -1.44459, -1.44157, -1.44882, -1.44727, -1.44358, -0.410391])

names.append("LElbowYaw")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([-1.19713, -1.182, -1.06746, -1.07722, -1.07327, -1.00666, -1.18957])

names.append("LHand")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.293758, 0.201565, 1, 1, 1, 0.999237, 0.303855])

names.append("LHipPitch")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.137485, 0.471117, 0.278488, 0.167528, 0.271561, 0.454981, 0.13])

names.append("LHipRoll")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.0969365, -0.0397644, -0.204057, 0.314512, -0.198592, 0.287913, 0.0952513])

names.append("LHipYawPitch")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([-0.170267, -0.357517, -0.251443, -0.241205, -0.241205, -0.354735, -0.171066])

names.append("LKneePitch")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([-0.088772, -0.088772, -0.088772, -0.088772, -0.088772, -0.085691, -0.088772])

names.append("LShoulderPitch")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([1.4687, 1.86291, 1.8634, 1.86286, 1.86338, 1.92941, 1.46871])

names.append("LShoulderRoll")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.177994, 0.0962844, 0.295168, 0.293814, 0.295022, 0.58294, 0.181621])

names.append("LWristYaw")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.0973422, -0.764318, -0.764486, -0.764486, -0.764486, -0.763548, 0.091971])

names.append("RAnklePitch")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.0889807, 0.0879011, 0.0724177, 0.0724177, 0.0724177, 0.0558261, 0.0889807])

names.append("RAnkleRoll")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.130073, 0.184855, 0.299268, -0.0668667, 0.300326, -0.00910154, 0.132032])

names.append("RElbowRoll")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.418757, 1.44665, 1.44519, 1.45011, 1.4499, 1.43466, 0.417568])

names.append("RElbowYaw")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([1.19739, 1.11345, 0.992934, 0.988181, 0.994126, 0.00544038, 1.19607])

names.append("RHand")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.293758, 0.201565, 1, 1, 1, 0.999237, 0.303855])

names.append("RHipPitch")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.13544, 0.382906, 0.207239, 0.228376, 0.207207, 0.420274, 0.138181])

names.append("RHipRoll")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([-0.100255, -0.278684, -0.386826, 0.130432, -0.385699, 0.00784492, -0.101012])

names.append("RHipYawPitch")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([-0.170267, -0.357517, -0.251443, -0.241205, -0.241205, -0.354735, -0.171066])

names.append("RKneePitch")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([-0.0846466, -0.0846466, -0.0846466, -0.0846466, -0.0846466, -0.0856566, -0.0846466])

names.append("RShoulderPitch")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([1.46869, 1.84745, 1.81858, 1.83834, 1.81883, 1.93613, 1.46857])

names.append("RShoulderRoll")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([-0.177966, -0.101775, -0.235333, -0.239939, -0.231813, -0.58294, -0.181469])

names.append("RWristYaw")
times.append([0.2, 0.5, 0.8, 1.1, 1.4, 1.7, 2])
keys.append([0.102956, 1.06063, 1.0616, 1.0616, 1.0616, 0.0371795, 0.108874])