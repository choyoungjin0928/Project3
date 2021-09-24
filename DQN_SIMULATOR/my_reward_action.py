#!/usr/bin/env python
# -*- coding: utf-8 -*-

def reward_in_game(data):
    reward = 0.0
    action = data[1]
    if 0 <= action <= 2:  # 뒤로 갈때 벌점 1점
        reward -= 1.0
    elif 3 <= action <= 5: # 앞으로 갈때 승점 0.5점
        reward += 0.5
    elif action == 6:     # 정지시 벌점 0.5점
        reward -= 0.5

    return float(reward)

def reward_end_game(data):
    reward = 1.0

    return float(reward)
