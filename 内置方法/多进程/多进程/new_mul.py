# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: new_mul.py
# author: ScCcWe
# time: 2020/4/27 9:27
import os
from multiprocessing import Pool, cpu_count
import functools


def divide_work_list(func):
    @functools.wraps(func)
    def divide_func(*args):
        tasks_list = func(*args)
        div_num = int(len(tasks_list) / cpu_count()) + 1
        return [tasks_list[i:i + div_num] for i in range(0, len(tasks_list), div_num)]
    return divide_func


@divide_work_list
def get_task_list(root_path):
    task_list = os.listdir(root_path)  # 任务列表
    assert len(task_list) >= 2, '选择的root_path路径为空！'
    return task_list


def main_process(root_path):
    list_divided = get_task_list(root_path)
    print(list_divided)
    with Pool(processes=cpu_count()) as p:
        for i in range(cpu_count()):
            p.apply_async(single_process_worker, args=(list_divided[i], ...))
        
        p.close()  # 阻止后续任务提交到进程池，当所有任务执行完成后，工作进程会退出
        p.join()  # 等待工作进程结束。调用 join() 前必须先调用 close() 或者 terminate()


# 单线程需要完成的工作
def single_process_worker():
    ...


if __name__ == '__main__':
    main_process(root_path=r'C:\Users\hwx827939\Desktop\pic')
