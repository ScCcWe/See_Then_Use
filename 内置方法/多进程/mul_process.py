"""
install: pip install tqdm
function：多进程使用模板
file: mul_process.py
author: ScCcWe
time: 2019-12-28
"""
import time
import os
import shutil
import os
from tqdm import tqdm                  # 显示进度条
from multiprocessing import cpu_count    # 查看cpu核心数
from multiprocessing import Pool         # 并行处理必备，进程池


def main_process():
    root_path = r'D:\测试用\shutil复制测试'
    dst_path_full = r'D:\测试用\shutil复制测试_进程池'

    tasks_list = os.listdir(root_path)  # 任务列表
    len_tasks_list = len(tasks_list)  # 任务列表长度

    num_cores = cpu_count()  # cpu核心数
    print(num_cores)

    if num_cores == 2:  # 双核，将所有数据集分成两个子数据集
        subset1 = tasks_list[:len_tasks_list // 2]
        subset2 = tasks_list[len_tasks_list // 2:]

        list_subsets = [subset1, subset2]

    elif num_cores == 4:  # 四核，将所有数据集分成四个子数据集
        subset1 = tasks_list[:len_tasks_list // 4]
        subset2 = tasks_list[len_tasks_list // 4: len_tasks_list // 2]
        subset3 = tasks_list[len_tasks_list // 2: (len_tasks_list * 3) // 4]
        subset4 = tasks_list[(len_tasks_list * 3) // 4:]

        list_subsets = [subset1, subset2, subset3, subset4]
        print(list_subsets)

    elif num_cores >= 8:  # 八核以上，将所有数据集分成八个子数据集
        num_cores = 8
        subset1 = tasks_list[:len_tasks_list // 8]
        subset2 = tasks_list[len_tasks_list // 8: len_tasks_list // 4]
        subset3 = tasks_list[len_tasks_list // 4: (len_tasks_list * 3) // 8]
        subset4 = tasks_list[(len_tasks_list * 3) // 8: len_tasks_list // 2]
        subset5 = tasks_list[len_tasks_list // 2: (len_tasks_list * 5) // 8]
        subset6 = tasks_list[(len_tasks_list * 5) //
                             8: (len_tasks_list * 6) // 8]
        subset7 = tasks_list[(len_tasks_list * 6) //
                             8: (len_tasks_list * 7) // 8]
        subset8 = tasks_list[(len_tasks_list * 7) // 8:]

        list_subsets = [subset1, subset2, subset3, subset4,
                        subset5, subset6, subset7, subset8]

    # 开辟进程池，num_cores为cpu核心数，也就是开启的进程数
    p = Pool(num_cores)

    # 对每个进程分配工作
    for i in range(num_cores):
        # 格式：p.apply_async(task, args=(...))
        # task：当前进程需要进行的任务/函数，只需要填写函数名
        # args：task函数中所需要传入的参数
        # 注意看 list_subsets[i] 就是传入不同的数据子集
        p.apply_async(
            single_worker,
            args=(
                list_subsets[i],
                root_path,
                dst_path_full))

    # 当进程完成时，关闭进程池
    p.close()
    p.join()


# 单线程需要完成的工作
def single_worker(list_subsets, root_path, dst_path_full):
    # for work_column in list_subsets:
    for work_column in tqdm(list_subsets):
        need_do_data_path = os.path.join(root_path, work_column)
        # print(need_do_data_path)
        for file_name in os.listdir(need_do_data_path):
            src_path = os.path.join(need_do_data_path, file_name)
            # print(src_path)
            # print("\n{0}  task:----{1}".format(self.number, file_name))
            mkdir_p(dst_path_full + '/' + work_column)
            shutil.copy(
                src_path,
                dst_path_full +
                '/' +
                work_column +
                '/' +
                file_name)


def mkdir_p(variable_path):
    if not os.path.exists(variable_path):
        os.makedirs(variable_path)


if __name__ == '__main__':
    start_time = time.time()
    main_process()
    print(time.time() - start_time)
