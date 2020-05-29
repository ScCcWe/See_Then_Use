import logging
import time


def log(level='info', title='log', message='logout'):
    # 创建一个logger
    logger = logging.getLogger('[{}]'.format(title))

    logger.setLevel(logging.DEBUG)

    # 创建一个handler，用于写入日志文件
    log_name = time.strftime('%Y-%m-%d', time.localtime(time.time()))  # 日志名
    fh = logging.FileHandler('{}.log'.format(log_name), encoding='utf-8')  # 文件日志

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


if __name__ == '__main__':
    log(level='debug', title='recv', message='json文件的数据数量有问题')
    log('warning', 'recv', '%s' % ('json文件的数据数量有问题',))
    log('error', 'recv', '%s' % ('json文件的数据数量有问题',))
    log('error', 'recv', '%s' % 'json文件的数据数量有问题',)
