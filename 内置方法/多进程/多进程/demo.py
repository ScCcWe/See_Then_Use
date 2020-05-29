# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: new_mul.py
# author: ScCcWe
# time: 2020/4/27 9:27
import os
import sys
from multiprocessing import Pool, cpu_count
import functools
from colorama import Back, init

if 'win' in sys.platform:
    path_route_format = '\\'
else:
    path_route_format = '/'

do_file_path_list = []
init(autoreset=True)  # in windows


def divide_work_list(func):
    @functools.wraps(func)
    def divide_func(*args):
        tasks_list = func(*args)
        num = cpu_count() if len(tasks_list) > cpu_count() else 2
        # print(num)
        # print(len(tasks_list) / num)
        # print(len(tasks_list) % num)
        # 刚好可以平分的情况
        if len(tasks_list) % num == 0:
            div_num = int(len(tasks_list) / num)
            return [tasks_list[i:i + div_num] for i in range(0, len(tasks_list), div_num)], num
        
        # 无法平分的情况
        # 例如：9/4 = 2.25  div_num = 2  [] -> [ab][ab][ab][abc]
        else:
            div_num = int(len(tasks_list) / num)
            need_list = [tasks_list[i:i + div_num] for i in range(0, len(tasks_list[div_num * 2:]), div_num)]
            need_last_list = tasks_list[div_num * 3:]
            need_list.append(need_last_list)
            return need_list, num
    return divide_func


@divide_work_list
def get_task_list(root_path):
    task_list = get_all_list(root_path)
    assert len(task_list) >= 2, '选择的root_path路径为空！'
    return task_list


def get_all_list(par_path):
    for file_or_dir in os.listdir(par_path):
        par_path_new = par_path + path_route_format + file_or_dir
        if os.path.isdir(par_path_new):
            get_all_list(par_path_new)
        elif os.path.isfile(par_path_new):
            do_file_path_list.append(par_path_new)
    return do_file_path_list


def main_process(root_path):
    list_divided, cpu_num = get_task_list(root_path)
    print(Back.WHITE + "待处理的" + Back.GREEN + "任务队列" + Back.WHITE + "如下:")
    print(list_divided)
    with Pool(processes=cpu_num) as p:
        for i in range(cpu_num):
            p.apply_async(single_process_worker, args=(list_divided[i], ...))
        
        p.close()  # 阻止后续任务提交到进程池，当所有任务执行完成后，工作进程会退出
        p.join()  # 等待工作进程结束。调用 join() 前必须先调用 close() 或者 terminate()


# 单线程需要完成的工作
def single_process_worker():
    ...


if __name__ == '__main__':
    main_process(root_path=r'C:\Users\hwx827939\Desktop\pic')
