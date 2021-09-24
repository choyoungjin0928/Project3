#!/usr/bin/env python
# -*- coding: utf-8 -*-

import my_reward_action, time
import numpy as np
from env.xycarRL import *
from env.visual import *
    
if __name__ == '__main__':
    xycar = learning_xycar()
    xycar.set_map("competition_bs") # snake, square, competition

    hyper_param = {
        "sensor_num" : 5,
        "learning_rate" : 0.0025,
        "discount_factor" : 0.98,
        "batch_size" : 512,
        "min_history" : 512,
        "buffer_limit" : 1000000,
        "max_episode" : 99999999,
        "update_cycle" : 15,
        "hidden_size" : [1024, 1024],
        "min_score" : 0,                # 추가되었습니다. 
        "max_score" : 2000000           # 추가되었습니다.
    }

    xycar.set_hyperparam(hyper_param)

    state_select = {
        "car sensor" : True,
        "car yaw" : False,
        "car position" : False,
        "car steer" : True
    }

    xycar.state_setup(state_select)
    xycar.Experience_replay_init()
    xycar.ML_init("DDQN") # "DDQN" "Duel DQN"

    xycar.set_init_location_pose_random(True) 

    visual = visualize(port=8888)
    visual.chart_init()

    ALL_STEPS, ALL_REWARD = 0, 0
    episode = 0

    start_time = time.time()

    while (0 <= episode <= int(hyper_param["max_episode"])):
        episode += 1
        epsilon = max(0.01, 0.6 - 0.01*(float(episode)/100.0))
        xycar.set_E_greedy_func(epsilon)

        state = xycar.episode_init()

        reward, score = 0, 0.0

        while not xycar.get_episode_done():
            action = xycar.get_action(state)
            next_state = xycar.step(action)

            if xycar.get_episode_done() or score < hyper_param["min_score"] or score > hyper_param["max_score"]:
                for_reward = [xycar.get_round_count()]
                reward += my_reward.reward_end_game(for_reward)

                xycar.Experience_replay_memory_input(state, action, next_state, reward)
                break

            for_reward = [xycar.get_sensor_value(), action]
            reward = my_reward.reward_in_game(for_reward)
            
            xycar.Experience_replay_memory_input(state, action, next_state, reward)
            
            state = next_state
            score += reward

        ALL_STEPS += xycar.get_step_number()
        ALL_REWARD += score

        if xycar.get_max_score() < score:
            xycar.max_score_update(score)
            xycar.model_save(episode)
            xycar.making_video(episode, score)

        if xycar.get_memory_size() > hyper_param["min_history"]:
            loss = xycar.train()
            visual.loss_graph_update(episode, loss)

        visual.dead_position_update(xycar.get_xycar_position())
        visual.reward_update(episode, score)
        visual.learning_curve_update(episode, ALL_REWARD)

        if (xycar.get_memory_size() > hyper_param["min_history"]) and ((episode % hyper_param["update_cycle"]) == 0) and (episode != 0):
            xycar.mainQ2targetQ()

        if (episode % 10 == 0) and (episode != 0):
            print("episode :{}, time : {}, memory size : {}, epsilon : {:.1f}%".format(episode, time.time()-start_time, xycar.get_memory_size(), epsilon*100))
