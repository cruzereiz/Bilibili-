# -*- coding: UTF-8 -*-
import subprocess


# 可以合成
# COMMAND = f'ffmpeg -i 合并分割ori.mp4 -i 合并分割ori.mp3 -c:v copy -c:a aac -strict experimental 02下载、配置.mp4'
# subprocess.Popen(COMMAND,shell=True)


p1 = r'F:\bili\download\84分钟鏖战！Ame9万经济十神电狗对阵TB炸弹人！\sett'
p2 = r'F:\bili\download\84分钟鏖战！Ame9万经济十神电狗对阵TB炸弹人！\sett'
p3 = r'F:\bili\download\84分钟鏖战！Ame9万经济十神电狗对阵TB炸弹人！\set'

COMMAND = f'ffmpeg -i {p1}.mp4 -i {p2}.mp3 -c:v copy -c:a aac -strict experimental {p3}.mp4'
subprocess.Popen(COMMAND,shell=True)
