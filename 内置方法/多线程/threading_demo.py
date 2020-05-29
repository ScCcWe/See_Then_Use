# -*- encoding: UTF-8 -*-
"""
install: None
function：多线程使用模板
file: mul_process.py
author: ScCcWe
time: 2019-12-28
"""
import shutil
import threading
import queue
import os
import time


class Worker(threading.Thread):

    def __init__(self, work_queue, number):
        super(Worker, self).__init__()
        self.work_queue = work_queue
        self.number = number

    def process(self, work_column):
        # 自定义的线程处理函数，用于run()中.
        need_do_data_path = os.path.join(root_path, work_column)
        print(need_do_data_path)
        for file_name in os.listdir(need_do_data_path):
            src_path = os.path.join(need_do_data_path, file_name)
            print(src_path)
            # print("\n{0}  task:----{1}".format(self.number, file_name))
            mkdir_p(dst_path_full + '/' + work_column)
            shutil.copy(src_path, dst_path_full + '/' + work_column + '/' + file_name)

    def run(self):
        # 重载threading类中的run()
        while True:
            try:
                work_column = self.work_queue.get()  # 从队列取出任务
                print(work_column)
                self.process(work_column)
            finally:
                self.work_queue.task_done()  # 通知queue前一个task已经完成


def main(work_list, work_threads):
    work_queue = queue.Queue()  # queue类中实现了锁
    for i in range(work_threads):  # 设置了 work_threads 个子进程
        worker = Worker(work_queue, i)  # 工作线程、工作队列、线程编号
        worker.daemon = True  # 守护进程
        worker.start()  # 启动线程开始
    for work_column in work_list:
        work_queue.put(work_column)  # 加入到队列中开始各个线程
    work_queue.join()  # 队列同步
    print(time.time() - start_time)


def mkdir_p(variable_path):
    if not os.path.exists(variable_path):
        os.makedirs(variable_path)


if __name__ == "__main__":
    start_time = time.time()
    config_threads = 5
    root_path = r'D:\测试用\shutil复制测试'
    dst_path = r'D:\测试用'
    dst_path_full = os.path.join(dst_path, 'shutil复制测试_速度_5_thread')
    config_work_list = os.listdir(root_path)
    main(work_list=config_work_list, work_threads=config_threads)
