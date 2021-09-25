#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np

def reward_cal(data1, data2):
    global idx
    global cos_list
    global sin_list
    
    idx = [270, 315, 0, 45, 90]  #sin, cos 계산을 위한 degrees 값
    #idx를 가져와서 cos 계산 후 radians로 변환한 리스트
    cos_list = [math.cos(idx[0]*np.pi/180), math.cos(idx[1]*np.pi/180), math.cos(idx[2]*np.pi/180), math.cos(idx[3]*np.pi/180), math.cos(idx[4]*np.pi/180)]
    #idx를 가져와서 sin 계산 후 radians로 변환한 리스트
    sin_list = [math.sin(idx[0]*np.pi/180), math.sin(idx[1]*np.pi/180), math.sin(idx[2]*np.pi/180), math.sin(idx[3]*np.pi/180), math.sin(idx[4]*np.pi/180)]
    
    avg_x = 0
    avg_y = 0
    
    sensor_value_tmp = data1
    steering_tmp = data2
    #print(sensor_value_tmp)
    sensor_value_cal = np.array(sensor_value_tmp) #라이다 값
    #print(sensor_value_cal)
    steering = np.array(steering_tmp) #차량의 조향 값
    
    for i in range(len(idx)):
        avg_x += sin_list[i] * float(sensor_value_cal[i])
        avg_y += cos_list[i] * float(sensor_value_cal[i])
        
    avg_x = avg_x/5 #x 성분 평균 - 반복문으로 합하고, 평균 구함.
    avg_y = avg_y/5 #y 성분 평균 - 반복문으로 합하고, 평균 구함.
    avg_distance = math.sqrt(avg_x*avg_x + avg_y*avg_y) #avg_x와 avg_y를 통해 평균 벡터 거리를 구함.
    
    result_sin_angle = math.asin(avg_x/avg_distance) * 180 / np.pi #arcsin으로 각도를 구한 후 degrees로 변환
    
    #result_sin_angle 값이 범위를 벗어난 경우에 값을 다시 세팅
    if result_sin_angle > 30:
        result_sin_angle = 30
    elif result_sin_angle < -30:
        result_sin_angle = -30
        
    reward = 1 - abs(steering - result_sin_angle) / 60 #앞에서 구해진 steering과 result_sin_angle을 가지고 reward 계산
    
    return float(reward)
    
#def reward_in_game(data):
#    reward = 0.5
    
#    sensor_value = data[1]
#    steering = data[4]
#    sensor_value.sort()
#    #print(sensor_value, steering)
    
#    reward += reward_cal(sensor_value, steering)

#    return float(reward)

last_action = 6

def reward_in_game(data):
    global last_action

    reward = 0.0
    action = data[1]
    dead_line = 5
    min_front = min(data[0][1:4])
    if (0 <= action <= 2) and (dead_line < min_front):
        reward += 0.2
    elif (0 <= action <= 2):  # 뒤로 갈때 벌점 1점
        reward -= 1.0
    elif 3 <= action <= 5: # 앞으로 갈때 승점 0.5점
        reward += 0.5
    elif action == 6:     # 정지시 벌점 0.5점
        reward -= 0.5

    if (last_action in [0, 1, 2]) and (action in [0, 1, 2]):
        reward -= 1.0
    elif (last_action in [3, 4, 5]) and (action in [3, 4, 5]):
        reward += 0.25
    elif (last_action in [0, 1, 2]) and (action in [3, 4, 5]):
        reward -= 1.0
    elif (last_action in [3, 4, 5]) and (action in [0, 1, 2]):
        reward -= 1.0
    elif (last_action in [3, 4, 5]) and (action == 6):
        reward -= 1.0
    elif (last_action in [0, 1, 2]) and (action == 6):
        reward -= 1.0
    elif (last_action == 6) and (action in [0, 1, 2]):
        reward -= 1.0
    elif (last_action == 6) and (action in [3, 4, 5]):
        reward -= 1.0

    last_action = action

    #min_score = -1.75
    #max_score = 1.0

    #return float((reward - min_score) * 1/(max_score - min_score)) + reward_cal(data[0], data[2][5])
    return reward + reward_cal(data[0], data[2][5])

def reward_end_game(data):
    reward = 1.0
    return float(reward)
