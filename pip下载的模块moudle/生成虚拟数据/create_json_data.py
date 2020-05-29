"""
install: pip install tqdm, faker
function：生成一个树状文件序列, 共：20x100 = 2000 个json文件
file: create_json_data.py
author: ScCcWe
time: 2019-12-28
"""
from faker import Faker
import os
import json
from tqdm import trange


def main():
    fake = Faker("zh-CN")
    
    json_data = fake.simple_profile()
    json_data.pop('birthdate')  # 因为日期无法json序列化，所以将这个字段删除
    
    root_path = 'D://测试用'
    
    fake_path = root_path + '/' + '测试用虚拟数据'
    
    for i in trange(1, 21):
        mkdir_p(fake_path + '/' + str(i))
        for j in range(1, 101):
            with open(fake_path + '/' + str(i) + '/' + str(j) + '.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(json_data, ensure_ascii=False, indent=4))


def mkdir_p(path):
    if not os.path.exists(path):
        os.makedirs(path)


if __name__ == '__main__':
    main()
