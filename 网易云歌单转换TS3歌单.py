# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
# File       : 网易云歌单转换TS3歌单.py
# Time       : 2023年1月13日 0013 \(^o^)/ 15:23:40 摆烂！
# Author     : kirito
# email      : 1342874081@qq.com
# Blog       : mywifeasuna.top
# Description:
"""
import os
import platform
import sys
import time
import pynvml
import psutil as psutil
import uuid
import wmi

from selenium import webdriver
from selenium.webdriver.common.by import By


def info():
    print("============================")
    print(" || 网易云歌单转换TS3歌单 || ")
    print(" || 作者：kirito          || ")
    print(" || 博客：mywifeasuna.top || ")
    print("============================")
    print("\n")
    print("注意：如果歌单为私人歌单，需要登陆才能获取")
    print("开坑：")
    print("     登陆 x")
    print("     翻页 x")
    print("     VIP  可做(请直接询问律师")
    print("\n")
    print("--------------------")


class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a', encoding="utf8")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


def log():
    log_path = './logs/'
    log_file_name = log_path + 'log-' + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + '.log'
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    os.path.join(log_path, f'{log_file_name}')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    # 使用Logger类 经典做法可直接copy 注意编码问题
    # sys.stdout = Logger(f'{log_file_name}', sys.stdout)
    sys.stderr = Logger(f'{log_file_name}', sys.stderr)
    # 获取电脑信息写入 log
    with open(f'{log_file_name}', 'a', encoding="utf8") as f:
        # System
        macaddr = uuid.UUID(int=uuid.getnode()).hex[-12:]
        macaddr = ':'.join([macaddr[e:e + 2] for e in range(0, 11, 2)])
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + str(platform.uname()) + "\n"
                + time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime()) + " | " + "platform: " + platform.platform() + "\n"
                + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + "version: " + platform.version() + "\n"
                + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + "architecture: " + str(
            platform.architecture()) + "\n"
                + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + "machine: " + platform.machine() + "\n"
                + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + "node: " + platform.node() + "\n"
                + time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime()) + " | " + "processor: " + platform.processor() + "\n"
                + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + "macaddr: " + macaddr + "\n"
                + time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime()) + " | " + "python_version: " + platform.python_version() + "\n"
                + "==================================================\n")

        # CPU
        cpu_info = wmi.WMI().Win32_Processor()
        for cpu in cpu_info:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + "CPU_NAME: " + cpu.Name + "\n"
                    + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + "CPU_LoadPercentage: " + str(
                cpu.LoadPercentage) + "%\n"
                    + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + "CPU_NumberOfCores: " + str(
                cpu.NumberOfCores) + "\n")

        # GPU
        # pynvml.nvmlInit()
        # device_count = pynvml.nvmlDeviceGetCount()
        # total_memory = 0
        # total_free = 0
        # total_used = 0
        # gpu_num = device_count
        #
        # for i in range(device_count):
        #     handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        #     info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        #     gpu_name = pynvml.nvmlDeviceGetName(handle).decode('utf-8')
        #     total_memory += (info.total // 1048576) / 1024
        #     total_free += (info.free // 1048576) / 1024
        #     total_used += (info.used // 1048576) / 1024
        #     f.write("GPU_NAME: " + gpu_name + "\n"
        #             + "GPU_NUM: " + str(gpu_num) + "\n"
        #             + "GPU_TOTAL_MEMORY: " + str(total_memory) + "\n"
        #             + "GPU_TOTAL_MEMORY: " + str("%.2f%%" % (total_used / total_memory)) + "\n")

        # Memory
        free = str(round(psutil.virtual_memory().free / (1024.0 * 1024.0 * 1024.0), 2)) + 'GB'
        total = str(round(psutil.virtual_memory().total / (1024.0 * 1024.0 * 1024.0), 2)) + 'GB'
        memory_use_percent = str(psutil.virtual_memory().percent) + ' %'
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + "Memory_Free: " + free + "\n"
                + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " | " + "Memory_Total: " + total + "\n"
                + time.strftime("%Y-%m-%d %H:%M:%S",
                                time.localtime()) + " | " + "Memory_Use_Percent: " + memory_use_percent + "\n\n")

        # 回到原位置
        os.chdir(f'{default_path}')


def files():
    # 创建并检查文件夹
    os.chdir('./.')
    path = os.getcwd()
    path = os.path.join(path, 'data')
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)
    return path


def get_list_id():
    play_list_id = input("请输入歌单ID 按回车键确认：")
    time.sleep(1)
    print('正在检测歌单ID...')
    return play_list_id


def get_ts3ablist(play_list_id):
    option = webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    option.add_argument('headless')

    web = webdriver.Chrome(executable_path="chromedriver", options=option)
    web.get(f'https://music.163.com/#/playlist?id={play_list_id}')
    time.sleep(1)
    iframe = web.find_element(By.XPATH, '//*[@id="g_iframe"]')
    web.switch_to.frame(iframe)
    time.sleep(1)
    music_num = web.find_element(By.XPATH, '//*[@id="playlist-track-count"]').text
    music_url_list = web.find_elements(By.XPATH, '//td[2]/div/div/div/span/a')
    music_name_list = web.find_elements(By.XPATH, '//td[2]/div/div/div/span/a/b')
    with open(f'data/{play_list_id}.ts3ablist', mode='w', encoding="utf8", newline='') as file:
        file.close()
    print('正在疯狂爬取，请稍等...')
    f = open(f"data/{play_list_id}.ts3ablist", mode="w", encoding="utf8", newline="")
    print("version:3", file=f)
    print('meat:{"count":' + music_num + f',"title":"{play_list_id}''"}'"\n", file=f)
    for music_url in music_url_list:
        print("rsj:{\"type\":\"media\",\"resid\":\"http://music.163.com/song/media/outer/url?id="
              + music_url.get_attribute('href')[30:]
              + ".mp3\",\"title\":\"", end="", file=f)
        for music_name in music_name_list:
            print(music_name.get_attribute('title') + "\"}", file=f)
            del music_name_list[0]
            break
    f.close()
    return web


def del_log(path):
    if not os.path.isdir(path):
        return
    for file in os.listdir(path):
        if os.path.isfile(path + "/" + file):
            last_time = int(os.stat(path + "/" + file).st_mtime)
            now_time = int(time.time()) - 1800
            if last_time <= now_time:
                os.remove(path + "/" + file)


if __name__ == '__main__':
    try:
        info()
        default_path = os.getcwd()
        log()
        get_path = files()
        while True:
            try:
                list_id = get_list_id()
                get_web = get_ts3ablist(list_id)
            except Exception:
                print("此歌单不存在或为私人歌单，需要登陆才可查看。稍等1秒请重新输入一个公共歌单ID\n")
            else:
                break
        time.sleep(1)
        print("\n任务完成！文件输出在data目录下 请手动关闭程序。")
        get_web.close()
        sys.exit(0)
    except KeyboardInterrupt:
        del_log('./logs')
        print("\n手动关闭程序，正常退出！")
        sys.exit(0)
