#!/usr/bin/env python
#-*- coding: utf-8 -*-

#####################################################################################
# 해당 맵은 프로그래머스 2기 수강자인 허석님의 노력으로 제작된 맵을 바탕으로 제작되었습니다. #
# 혹여나 마주치면 감사하다고 인사드리도록 합시다.                                        #
#####################################################################################

MAP_NAME = "competition_bs" # 파일 이름과 같아야 함.
SCREEN_WIDTH =  1274 #1385 #1343.979 + 20.47968*2      # 트랙 너비 597
SCREEN_HEIGHT = 1264 #1385 #1343.979 + 20.47968*2     # 트랙 높이 592.5cm

INIT_POSE = [             # 초기 위치 및 자세 설정 - 랜덤위치 할시 0번 고정됨, 아니면 랜덤으로 실행 [x, y, yaw]
    [12.0, 6.92, 270.0],     # 해당 리스트에 [x, y, yaw] 추가할 수록 시작할 수 있는 시작위치가 늘어남
    [1.85, 6.92, 270.0],
    [5.21, 6.92, 270.0],
    [5.21, 6.92, 90.0],
    [8.62, 6.92, 270.0],
    [8.62, 6.92, 90.0],
]

# 추가할 장애물 OBS 리스트에 [x, y, 너비, 높이] 리스트를 추가하면 해당 위치에 장애물이 나타남.
WALL_SIZE = 22 # 20.47968 #9.6cm X, 10.5cm  ==>2.1333배
ROAD_WIDTH = 295 #320.63499 # 150.3cm X , 138.25cm
BOX = 207 #224 #223.9965 # 105cm X, 97cm
OBS_BOX_LENGTH = 96 # 45cm
OBS_BOX_WIDTH = 32 #15cm
OBS = [
   #############반드시 기본적으로 있어야 하는 벽##############
    [0, 0, WALL_SIZE, SCREEN_HEIGHT],                     #
    [0, 0, SCREEN_WIDTH, WALL_SIZE],                      #
    [0, SCREEN_HEIGHT-WALL_SIZE, SCREEN_WIDTH, WALL_SIZE],#
    [SCREEN_WIDTH-WALL_SIZE, 0, WALL_SIZE, SCREEN_HEIGHT],#
   ########################################################
    [WALL_SIZE * 1 + 1 * ROAD_WIDTH, WALL_SIZE, WALL_SIZE, BOX * 4],
    [WALL_SIZE * 2 + 2 * ROAD_WIDTH, WALL_SIZE + BOX * 2, WALL_SIZE, BOX * 4],
    [WALL_SIZE * 3 + 3 * ROAD_WIDTH, WALL_SIZE, WALL_SIZE, BOX * 4],
    ####################################################################
    [WALL_SIZE * 1 + 1 * ROAD_WIDTH - OBS_BOX_LENGTH, WALL_SIZE + BOX * 3, OBS_BOX_LENGTH, OBS_BOX_WIDTH], # 1번 장애물 (진입시 만나는 순서 기준)
    [WALL_SIZE * 2 + 1 * ROAD_WIDTH, WALL_SIZE + BOX * 4 - OBS_BOX_WIDTH, OBS_BOX_LENGTH, OBS_BOX_WIDTH], # 2번 장애물
    [WALL_SIZE * 2 + 2 * ROAD_WIDTH - 1 * OBS_BOX_LENGTH, WALL_SIZE + BOX * 2.5 - 0.5 * OBS_BOX_WIDTH, OBS_BOX_LENGTH, OBS_BOX_WIDTH], # 3번 장애물
    [WALL_SIZE * 3 + 2 * ROAD_WIDTH, WALL_SIZE + BOX * 5, OBS_BOX_LENGTH, OBS_BOX_WIDTH], # 4번 장애물
    [WALL_SIZE * 3 + 3 * ROAD_WIDTH - OBS_BOX_LENGTH, WALL_SIZE + BOX * 4 - OBS_BOX_WIDTH, OBS_BOX_LENGTH, OBS_BOX_WIDTH], # 5번 장애물
    [WALL_SIZE * 4 + 4 * ROAD_WIDTH - OBS_BOX_LENGTH, WALL_SIZE + BOX * 3 - OBS_BOX_WIDTH, OBS_BOX_LENGTH, OBS_BOX_WIDTH], # 6번 장애물

]

# 순간이동 설정
WARP = [
    #{"zone" : [WALL_SIZE * 4 + 3*ROAD_WIDTH, int(SCREEN_HEIGHT/10), 220, 22], "mov_pos" : [-1, -1, 90.0]},
    {"zone" : [0, 0, 1, 1],                      "mov_pos" : [-1, -1, 270.0]} 
  # zone 에 들어가 있는 리스트 대로 워프존이 만들어짐
]                                                              # mov_pos 에 들어가 있는 리스트 대로 차량 위치와 포즈가 설정됨

GOAL = [
    #[WALL_SIZE + 3*ROAD_WIDTH + G*3, int(SCREEN_HEIGHT/2), 220, 22],
    #[WALL_SIZE, int(SCREEN_HEIGHT/2), 220, 22]
]
