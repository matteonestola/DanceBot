# Choregraphe simplified export in Python.

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.96, 1.32, 1.76, 2, 2.24, 2.48, 2.72, 2.96, 3.2, 3.44, 3.68, 3.92, 4.16, 4.4, 4.64, 4.88, 5.12, 5.36, 5.6, 5.84, 6.08, 6.32, 6.56, 6.8, 7.04, 7.28, 7.52, 7.76, 8, 8.52, 8.76, 9, 9.24, 9.48, 9.72, 9.96, 10.2, 10.44, 10.68, 10.92, 11.16, 11.4, 11.64, 11.88, 12.12, 12.36, 12.72, 13.04, 13.28, 13.52, 13.76, 14, 14.24, 14.48, 14.72, 14.96, 15.2, 15.44, 15.68, 15.92, 16.24, 16.64])
keys.append([-0.392746, -0.392746, -0.392746, -0.105767, -0.392746, -0.105767, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.105777, -0.392746, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.155334, -0.392746, -0.0808051, -0.0139626, -0.392746, -0.0139626, -0.392746, -0.0139626, -0.392746, -0.0139626, -0.392746, -0.0139626, -0.392746, -0.0139626, -0.392746, -0.0139626, -0.375714, -0.434587])

names.append("HeadYaw")
times.append([0.96, 1.32, 1.76, 2, 2.24, 2.48, 2.72, 2.96, 3.2, 3.44, 3.68, 3.92, 4.16, 4.4, 4.64, 4.88, 5.12, 5.36, 5.6, 5.84, 6.08, 6.32, 6.56, 6.8, 7.04, 7.28, 7.52, 7.76, 8, 8.52, 9, 9.48, 9.96, 10.44, 10.92, 11.4, 11.88, 12.36, 13.28, 14.24, 14.72, 15.68, 16.24, 16.64])
keys.append([0.00455999, 0.00455999, 0.00455999, -0.00157595, 0.00455999, -0.00157595, 0.00455999, -0.00157595, 0.00455999, -0.00157595, 0.00455999, -0.00157595, 0.00455999, -0.00157595, 0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, 0.00157595, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, -0.00455999, 0.638352, 0.638352, -0.639567, -0.639567, -0.0592826, -0.0153821])

names.append("LAnklePitch")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([0.091998, 0.091998, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.144154, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, -0.14364, -0.119694])

names.append("LAnkleRoll")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([-0.118076, -0.118076, -0.118076, -0.116542, -0.118076, -0.116542, -0.118076, -0.116542, -0.118076, -0.116542, -0.118076, -0.116542, -0.118076, -0.116542, -0.118076, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.075208, -0.073674, -0.112081, -0.116542])

names.append("LElbowRoll")
times.append([0.96, 1.32, 1.72, 1.96, 2.2, 2.44, 2.68, 2.92, 3.16, 3.4, 3.64, 3.88, 4.12, 4.36, 4.84, 5.08, 5.32, 5.56, 5.8, 6.04, 6.28, 6.52, 6.76, 7, 7.24, 7.48, 7.72, 7.96, 8.4, 8.64, 8.88, 9.12, 9.36, 9.6, 9.84, 10.08, 10.32, 10.56, 10.8, 11.04, 11.28, 11.52, 11.76, 12, 12.24, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([-1.52782, -1.52782, -1.52782, -1.52169, -1.52782, -1.52169, -1.52782, -1.52169, -1.52782, -1.52169, -1.52782, -1.52169, -1.52782, -1.52169, -0.550747, -0.349794, -0.550747, -0.349794, -0.550747, -0.349794, -0.550747, -0.349794, -0.550747, -0.349794, -0.550747, -0.349794, -0.550747, -0.349794, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -0.401426, -1.33657, -1.54462, -1.33657, -1.54462, -1.33657, -1.54462, -1.33657, -1.54462, -1.33657, -1.54462, -1.33657, -1.54462, -1.33657, -0.15575, -0.0349068])

names.append("LElbowYaw")
times.append([0.96, 1.32, 1.72, 1.96, 2.2, 2.44, 2.68, 2.92, 3.16, 3.4, 3.64, 3.88, 4.12, 4.36, 4.84, 5.08, 5.32, 5.56, 5.8, 6.04, 6.28, 6.52, 6.76, 7, 7.24, 7.48, 7.72, 7.96, 8.48, 8.72, 8.96, 9.2, 9.44, 9.68, 9.92, 10.16, 10.4, 10.64, 10.88, 11.12, 11.36, 11.6, 11.84, 12.08, 12.32, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([-0.236277, -0.236277, -0.236277, -0.145772, -0.236277, -0.145772, -0.236277, -0.145772, -0.236277, -0.145772, -0.236277, -0.145772, -0.236277, -0.145772, 0.380475, -1.06302, 0.380475, -1.06302, 0.380475, -1.06302, 0.380475, -1.06302, 0.380475, -1.06302, 0.380475, -1.06302, 0.380475, -1.06302, -0.644027, -0.0801321, -0.644027, -0.0801321, -0.644027, -0.0801321, -0.644027, -0.0801321, -0.644027, -0.0801319, -0.644027, -0.0801321, -0.644027, -0.0801321, -0.644027, -0.0801321, -0.644027, 0.038455, 0.0383972, 0.038455, 0.0383972, 0.038455, 0.0383972, 0.038455, 0.0383972, 0.038455, 0.0383972, 0.038455, 0.0383972, 0.038455, -1.59015, -1.82551])

names.append("LHand")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.4, 8.64, 8.88, 9.12, 9.36, 9.6, 9.84, 10.08, 10.32, 10.56, 10.8, 11.04, 11.28, 11.52, 11.76, 12, 12.24, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0, 0.00479996, 0, 0.00479996, 0, 0.00479996, 0, 0.00479996, 0, 0.00479996, 0, 0.00479996, 0.875715, 0.9996])

names.append("LHipPitch")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([0.0123138, 0.0123138, 0.0123138, -0.358915, 0.0123138, -0.358915, 0.0123138, -0.358915, 0.0123138, -0.358915, 0.0123138, -0.358915, 0.0123138, -0.358915, 0.0521979, -0.318285, 0.0194225, -0.334564, 0.0106959, -0.334564, 0.0106959, -0.334564, 0.0106959, -0.334564, 0.0106959, -0.334564, 0.0106959, -0.334564, 0.0106959, -0.334564, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.28663, 0.129154, -0.31281, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.397396, 0.481718])

names.append("LHipRoll")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([0.112024, 0.112024, 0.112024, 0.115092, 0.112024, 0.115092, 0.112024, 0.115092, 0.112024, 0.115092, 0.112024, 0.115092, 0.112024, 0.115092, 0.112024, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.061318, 0.0643861, 0.113546, 0.11816])

names.append("LHipYawPitch")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([-0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733])

names.append("LKneePitch")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([-0.090548, -0.090548, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.000676226, -0.090548])

names.append("LShoulderPitch")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.4, 8.64, 8.88, 9.12, 9.36, 9.6, 9.84, 10.08, 10.32, 10.56, 10.8, 11.04, 11.28, 11.52, 11.76, 12, 12.24, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([0.226991, 0.226991, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, -0.730907, -1.44345, -1.03006, -1.44345, -1.03006, -1.44345, -1.03006, -1.44345, -1.03006, -1.44345, -1.03006, -1.44345, -1.03006, -1.44345, -0.331613, 0.00878002, -0.331613, 0.00878005, -0.331613, 0.00878005, -0.331613, 0.00878005, -0.331613, 0.00878, -0.331613, 0.00878, -0.331613, 0.00878, -0.331613, 0.00878, -0.331613, 1.53865, 1.53938, 1.53865, 1.53938, 1.53865, 1.53938, 1.53865, 1.53938, 1.53865, 1.53938, 1.53865, 1.53938, 1.53865, 1.73828, 1.76713])

names.append("LShoulderRoll")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.4, 8.64, 8.88, 9.12, 9.36, 9.6, 9.84, 10.08, 10.32, 10.56, 10.8, 11.04, 11.28, 11.52, 11.76, 12, 12.24, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([0.121144, 0.121144, 0.121144, 0.12728, 0.121144, 0.12728, 0.121144, 0.12728, 0.121144, 0.12728, 0.121144, 0.12728, 0.121144, 0.12728, 0.248551, 0.331386, 0.248551, 0.331386, 0.248551, 0.331386, 0.248551, 0.331386, 0.248551, 0.331386, 0.248551, 0.331386, 0.248551, 0.331386, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, -0.314159, 0.788697, 0.909316, 0.788697, 0.909316, 0.788697, 0.909316, 0.788697, 0.909316, 0.788697, 0.909316, 0.788697, 0.909316, 0.788697, 0.530231, 0.506179])

names.append("LWristYaw")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.4, 8.64, 8.88, 9.12, 9.36, 9.6, 9.84, 10.08, 10.32, 10.56, 10.8, 11.04, 11.28, 11.52, 11.76, 12, 12.24, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([0.105804, 0.105804, 0.105804, 0.107338, 0.105804, 0.107338, 0.105804, 0.107338, 0.105804, 0.107338, 0.105804, 0.107338, 0.105804, 0.107338, -0.512313, -0.115008, -0.512313, -0.115008, -0.512313, -0.115008, -0.512313, -0.115008, -0.512313, -0.115008, -0.512313, -0.115008, -0.512313, -0.115008, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, 0.431096, -1.51511, -1.79636])

names.append("RAnklePitch")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([0.101286, 0.101286, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.101286, -0.34979, 0.145772, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, 0.091998, -0.34834, -0.14204, -0.118076])

names.append("RAnkleRoll")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([0.075208, 0.075208, 0.075208, 0.073674, 0.075208, 0.073674, 0.075208, 0.073674, 0.075208, 0.073674, 0.075208, 0.073674, 0.075208, 0.073674, 0.075208, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.118076, 0.116542, 0.0776441, 0.073674])

names.append("RElbowRoll")
times.append([0.96, 1.32, 1.72, 1.96, 2.2, 2.44, 2.68, 2.92, 3.16, 3.4, 3.64, 3.88, 4.12, 4.36, 4.84, 5.08, 5.32, 5.56, 5.8, 6.04, 6.28, 6.52, 6.76, 7, 7.24, 7.48, 7.72, 7.96, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([0.349794, 0.349794, 0.349794, 0.550747, 0.349794, 0.550747, 0.349794, 0.550747, 0.349794, 0.550747, 0.349794, 0.550747, 0.349794, 0.550747, 1.52169, 1.52782, 1.52169, 1.52782, 1.52169, 1.52782, 1.52169, 1.52782, 1.52169, 1.52782, 1.52169, 1.52782, 1.52169, 1.52782, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 0.401426, 1.33276, 1.54296, 1.33276, 1.54296, 1.33276, 1.54296, 1.33276, 1.54296, 1.33276, 1.54296, 1.33276, 1.54296, 1.33276, 0.170923, 0.0521979])

names.append("RElbowYaw")
times.append([0.96, 1.32, 1.72, 1.96, 2.2, 2.44, 2.68, 2.92, 3.16, 3.4, 3.64, 3.88, 4.12, 4.36, 4.84, 5.08, 5.32, 5.56, 5.8, 6.04, 6.28, 6.52, 6.76, 7, 7.24, 7.48, 7.72, 7.96, 8.44, 8.68, 8.92, 9.16, 9.4, 9.64, 9.88, 10.12, 10.36, 10.6, 10.84, 11.08, 11.32, 11.56, 11.8, 12.04, 12.28, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([1.06302, 1.06302, 1.06302, -0.380475, 1.06302, -0.380475, 1.06302, -0.380475, 1.06302, -0.380475, 1.06302, -0.380475, 1.06302, -0.380475, 0.145772, 0.236277, 0.145772, 0.236277, 0.145772, 0.236277, 0.145772, 0.236277, 0.145772, 0.236277, 0.145772, 0.236277, 0.145772, 0.236277, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, 0.0797858, 0.644027, -0.0384695, -0.0377698, -0.0384695, -0.0377698, -0.0384695, -0.0377698, -0.0384695, -0.0377698, -0.0384695, -0.0377698, -0.0384695, -0.0377698, -0.0384695, 1.59007, 1.82542])

names.append("RHand")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00479996, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0.00440001, 0, 0.00440001, 0, 0.00440001, 0, 0.00440001, 0, 0.00440001, 0, 0.00440001, 0, 0.00440001, 0.875526, 0.9996])

names.append("RHipPitch")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([0.0106959, 0.0106959, 0.0106959, -0.358999, 0.0106959, -0.358999, 0.0106959, -0.358999, 0.0106959, -0.358999, 0.0106959, -0.358999, 0.0106959, -0.358999, 0.052114, -0.318201, 0.0210405, -0.33448, 0.0123138, -0.33448, 0.0123138, -0.33448, 0.0123138, -0.33448, 0.0123138, -0.33448, 0.0123138, -0.33448, 0.0123138, -0.33448, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.26045, 0.109956, -0.28663, 0.129154, -0.31281, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.0541052, -0.328518, 0.397321, 0.481634])

names.append("RHipRoll")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([-0.061318, -0.061318, -0.061318, -0.0643861, -0.061318, -0.0643861, -0.061318, -0.0643861, -0.061318, -0.0643861, -0.061318, -0.0643861, -0.061318, -0.0643861, -0.0628521, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.112024, -0.115092, -0.0710375, -0.06592])

names.append("RHipYawPitch")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([-0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733, -0.1733])

names.append("RKneePitch")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.52, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.12, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 12.44, 12.68, 12.92, 13.16, 13.4, 13.64, 13.88, 14.12, 14.36, 14.6, 14.84, 15.08, 15.32, 15.56, 15.8, 16.24, 16.64])
keys.append([-0.0923279, -0.0923279, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.0923279, 0.77302, -0.091998, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.090548, 0.771402, -0.00243924, -0.0923279])

names.append("RShoulderPitch")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([-1.44345, -1.44345, -1.44345, -1.03084, -1.44345, -1.03084, -1.44345, -1.03084, -1.44345, -1.03084, -1.44345, -1.03084, -1.44345, -0.733274, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.438682, 0.226991, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 0.469958, 0.129154, 1.53849, 1.53857, 1.53849, 1.53857, 1.53849, 1.53857, 1.53849, 1.53857, 1.53849, 1.53857, 1.53849, 1.53857, 1.53849, 1.73967, 1.76875])

names.append("RShoulderRoll")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([-0.331386, -0.331386, -0.331386, -0.248551, -0.331386, -0.248551, -0.331386, -0.248551, -0.331386, -0.248551, -0.331386, -0.248551, -0.331386, -0.248551, -0.12728, -0.121144, -0.12728, -0.121144, -0.12728, -0.121144, -0.12728, -0.121144, -0.12728, -0.121144, -0.12728, -0.121144, -0.12728, -0.121144, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, 0.314159, -0.795964, -0.912095, -0.795964, -0.912095, -0.795964, -0.912095, -0.795964, -0.912095, -0.795964, -0.912095, -0.795964, -0.912095, -0.795964, -0.50207, -0.474047])

names.append("RWristYaw")
times.append([0.96, 1.32, 1.64, 1.88, 2.12, 2.36, 2.6, 2.84, 3.08, 3.32, 3.56, 3.8, 4.04, 4.28, 4.76, 5, 5.24, 5.48, 5.72, 5.96, 6.2, 6.44, 6.68, 6.92, 7.16, 7.4, 7.64, 7.88, 8.36, 8.6, 8.84, 9.08, 9.32, 9.56, 9.8, 10.04, 10.28, 10.52, 10.76, 11, 11.24, 11.48, 11.72, 11.96, 12.2, 13, 13.24, 13.48, 13.72, 13.96, 14.2, 14.44, 14.68, 14.92, 15.16, 15.4, 15.64, 15.88, 16.24, 16.64])
keys.append([0.115008, 0.115008, 0.115008, 0.512313, 0.115008, 0.512313, 0.115008, 0.512313, 0.115008, 0.512313, 0.115008, 0.512313, 0.115008, 0.512313, -0.107338, -0.105804, -0.107338, -0.105804, -0.107338, -0.105804, -0.107338, -0.105804, -0.107338, -0.105804, -0.107338, -0.105804, -0.107338, -0.105804, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, -0.431096, 1.50029, 1.7794])
