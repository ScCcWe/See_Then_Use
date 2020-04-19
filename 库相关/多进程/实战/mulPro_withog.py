"""
function: 多进程 + 日志 合并97点
describe: 2 进程 cpu 可以节约1/2时间，4 进程 cpu 可以节约3/4时间，以此类推...
author: ScCcWe
data: 2020-1-2
"""
import time
import json
import shutil
import os
import logging
from tqdm import tqdm                    # 显示进度条
from multiprocessing import cpu_count    # 查看cpu核心数
from multiprocessing import Pool         # 并行处理必备，进程池


def main_process(
        father_path,
        root_path,
        root_path_meimao_bizi,
        root_path_tongkong,
        root_path_yankuang,
        root_path_zuiba):

    tasks_list = os.listdir(root_path)  # 任务列表

    len_tasks_list = len(tasks_list)  # 任务列表长度

    assert len_tasks_list >= 2, '选择的root_path路径为空！！！'
    
    num_cores = cpu_count()  # cpu核心数
    # print(num_cores)

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
        # print(list_subsets)

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
                father_path,
                root_path,
                root_path_meimao_bizi,
                root_path_tongkong,
                root_path_yankuang,
                root_path_zuiba))

    # 当进程完成时，关闭进程池
    p.close()
    p.join()


# 单线程需要完成的工作
def single_worker(
        list_subsets,
        father_path,
        root_path,
        root_path_meimao_bizi,
        root_path_tongkong,
        root_path_yankuang,
        root_path_zuiba):
    for json_file in tqdm(list_subsets):
        if json_file.endswith('.json'):

            # 避免None的错误
            if os.path.getsize(os.path.join(root_path, json_file)) == 0:
                log('debug', 'recv', '%s' %
                    (root_path + '\\' + json_file + '文件为空',))
                continue
            if os.path.getsize(
                os.path.join(
                    root_path_meimao_bizi,
                    json_file)) == 0:
                log('debug', 'recv', '%s' %
                    (root_path_meimao_bizi + '\\' + json_file + '文件为空',))
                continue
            if os.path.getsize(
                os.path.join(
                    root_path_tongkong,
                    json_file)) == 0:
                log('debug', 'recv', '%s' %
                    (root_path_tongkong + '\\' + json_file + '文件为空',))
                continue
            if os.path.getsize(
                os.path.join(
                    root_path_yankuang,
                    json_file)) == 0:
                log('debug', 'recv', '%s' %
                    (root_path_yankuang + '\\' + json_file + '文件为空',))
                continue
            if os.path.getsize(os.path.join(root_path_zuiba, json_file)) == 0:
                log('debug', 'recv', '%s' %
                    (root_path_zuiba + '\\' + json_file + '文件为空',))
                continue

            # 避免数量不对的问题
            # 轮廓路径1-17 (是真正的1-17，而不是1-16)
            if read_specified_json(root_path, json_file) is None:
                log('debug', 'recv', '%s' %
                    (root_path + '\\' + json_file + '文件的json格式有问题',))
                continue
            elif len(read_specified_json(root_path, json_file)) / 3 == 17:
                data_lunkuo = read_specified_json(root_path, json_file)
            else:
                log('debug', 'recv', '%s' %
                    (root_path + '\\' + json_file + 'json文件的数据数量有问题',))
                continue

            # 眉毛 18-25 39-46 + 鼻子 60-73
            if read_specified_json(root_path_meimao_bizi, json_file) is None:
                log('debug', 'recv', '%s' %
                    (root_path_meimao_bizi + '\\' + json_file + '文件的json格式有问题',))
                continue
            elif len(read_specified_json(root_path_meimao_bizi, json_file)) / 3 == 30:
                data_meimao_bizi = read_specified_json(
                    root_path_meimao_bizi, json_file)
                data_meimao_left = data_meimao_bizi[:24]
                data_meimao_right = data_meimao_bizi[24:48]
                data_bizi = data_meimao_bizi[48:]
            else:
                log('debug', 'recv', '%s' %
                    (root_path_meimao_bizi + '\\' + json_file + 'json文件的数据数量有问题',))
                continue

            # 瞳孔 32-38 53-59
            if read_specified_json(root_path_tongkong, json_file) is None:
                log('debug', 'recv', '%s' %
                    (root_path_tongkong + '\\' + json_file + '文件的json格式有问题',))
                continue
            elif len(read_specified_json(root_path_tongkong, json_file)) / 3 == 14:
                data_tongkong = read_specified_json(
                    root_path_tongkong, json_file)
                data_tongkong_left = data_tongkong[:21]
                data_tongkong_right = data_tongkong[21:]
            else:
                log('debug', 'recv', '%s' %
                    (root_path_tongkong + '\\' + json_file + 'json文件的数据数量有问题',))
                continue

            # 眼眶 26-31 47-52
            if read_specified_json(root_path_yankuang, json_file) is None:
                log('debug', 'recv', '%s' %
                    (root_path_yankuang + '\\' + json_file + '文件的json格式有问题',))
                continue
            elif len(read_specified_json(root_path_yankuang, json_file)) / 3 == 12:
                data_yankuang = read_specified_json(
                    root_path_yankuang, json_file)
                data_yankuang_left = data_yankuang[:18]
                data_yankuang_right = data_yankuang[18:]
            else:
                log('debug', 'recv', '%s' %
                    (root_path_yankuang + '\\' + json_file + 'json文件的数据数量有问题',))
                continue

            # 嘴巴 74-97
            if read_specified_json(root_path_zuiba, json_file) is None:
                log('debug', 'recv', '%s' %
                    (root_path_zuiba + '\\' + json_file + '文件的json格式有问题',))
                continue
            elif len(read_specified_json(root_path_zuiba, json_file)) / 3 == 24:
                data_zuiba = read_specified_json(root_path_zuiba, json_file)
            else:
                log('debug', 'recv', '%s' %
                    (root_path_zuiba + '\\' + json_file + 'json文件的数据数量有问题',))
                continue

            # 如果能到进行到这步，说明数据肯定是正确的！
            need_data = data_lunkuo + data_meimao_left + data_yankuang_left + data_tongkong_left + \
                data_meimao_right + data_yankuang_right + data_tongkong_right + data_bizi + data_zuiba
            with open(os.path.join(root_path, json_file), 'r', encoding='utf-8') as f:
                format_json = json.load(f)
                format_json['keypoint_annotations']['human1'] = need_data

                store_path = father_path + '/' + 'together_97'
                mkdir_p(store_path)
                with open(os.path.join(store_path, json_file), 'w', encoding='utf-8') as f:
                    f.write(
                        json.dumps(
                            format_json,
                            indent=4,
                            ensure_ascii=False))

            # 复制相应的图片到 json 文件路径
            if os.path.exists(
                os.path.join(
                    root_path,
                    json_file.split(
                        '.',
                        2)[0] +
                    '.jpg')):
                shutil.copy(
                    os.path.join(
                        root_path,
                        json_file.split(
                            '.',
                            2)[0] + '.jpg'),
                    os.path.join(
                        father_path,
                        'together_97'))
            else:
                shutil.copy(
                    os.path.join(
                        root_path,
                        json_file.split(
                            '.',
                            2)[0] + '.png'),
                    os.path.join(
                        father_path,
                        'together_97'))


def mkdir_p(variable_path):
    if not os.path.exists(variable_path):
        os.makedirs(variable_path)


def log(level='info', title='log', message='logout'):
    # 创建一个logger
    logger = logging.getLogger('[{}]'.format(title))

    logger.setLevel(logging.DEBUG)

    # 创建一个handler，用于写入日志文件
    log_name = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 日志名
    fh = logging.FileHandler('{}.log'.format(log_name))  # 文件日志

    # 定义handler的输出格式
    formatter = logging.Formatter(
        '%(asctime)+s  %(name)+s  %(levelname)+s  %(message)+s')
    fh.setFormatter(formatter)

    # 给 logger 添加 handler
    logger.addHandler(fh)

    # 写入日志
    if level == 'debug':
        logger.debug(message)
    elif level == 'warning':
        logger.warning(message)
    elif level == 'error':
        logger.error(message)
    else:
        logger.error(message)

    # 添加下面一句，在记录日志之后移除句柄.
    # 这句是必须要加的，如果不加，会重复写log
    logger.removeHandler(fh)


def read_specified_json(root_path, json_file):
    with open(os.path.join(root_path, json_file), 'r', encoding='utf-8') as f:
        data = json.load(f)

        # 避免字段没有的问题
        if 'keypoint_annotations' in data.keys():  # 判断是否存在 keypoint_annotations 字段
            if 'human1' in data['keypoint_annotations'].keys(
            ):  # 判断是否存在 hunman1 字段
                if data['keypoint_annotations']['human1'] != []:  # 判断是否为空
                    return data['keypoint_annotations']['human1']
                else:
                    log('debug', 'recv', '%s' %
                        (root_path + '\\' + json_file + '文件的human1字段没有数据!!!',))
                    return None
            else:
                log('debug', 'recv', '%s' %
                    (root_path + '\\' + json_file + '文件没有human1字段!!!',))
                return None
        else:
            log('debug', 'recv', '%s' %
                (root_path + '\\' + json_file + '文件没有keypoint_annotations字段!!!',))
            return None


if __name__ == '__main__':
    # 根路径
    father_path = ***
    # 各个部分路径
    root_path = ***
    root_path_meimao_bizi = ***
    root_path_tongkong = ***
    root_path_yankuang = ***
    root_path_zuiba = ***
    main_process(
        father_path,
        root_path,
        root_path_meimao_bizi,
        root_path_tongkong,
        root_path_yankuang,
        root_path_zuiba)
