# !/usr/bin/env python
# -*- coding: utf-8 -*-
# file_name: code_analysis.py
# author: ScCcWe
# time: 2020/5/9 14:21
import os
import sys
import prettytable

count_comment = 0
count_blank = 0
count_code = 0
count_code_comment = 0


def deal_path_code(variable_path, **kwargs):
    with open(variable_path, 'r', encoding='utf-8') as f:
        code_lines = 0  # 代码行数
        comment_lines = 0  # 单行注释行数
        code_comment_lines = 0  # 代码+注释行数
        blank_lines = 0  # 空白行数  内容为'\n',strip()后为''
        is_comment = False
        start_comment_index = 0  # 记录以'''或"""开头的注释位置
        for index, line in enumerate(f, start=1):
            line = line.strip()  # 去除开头和结尾的空白符
            
            # 判断多行注释是否已经开始
            if not is_comment:
                if line.startswith("'''") or line.startswith('"""'):
                    is_comment = True
                    start_comment_index = index
                
                # 单行注释
                elif line.startswith('#'):
                    comment_lines += 1
                
                # 空白行
                elif line == '':
                    blank_lines += 1
                
                # 代码行
                else:
                    code_lines += 1
                    if '#' in line:
                        code_comment_lines += 1
            
            # 多行注释已经开始
            else:
                if line.endswith("'''") or line.endswith('"""'):
                    is_comment = False
                    comment_lines += index - start_comment_index + 1
                else:
                    pass
    if kwargs['format'] == 'three':
        # 注释；空行；代码
        return comment_lines, blank_lines, code_lines
    if kwargs['format'] == 'all':
        return comment_lines, blank_lines, code_lines, code_comment_lines
    

def start_pt():
    pt = prettytable.PrettyTable()
    pt.field_names = ['注释', '空行', '代码', '文件名']
    return pt


def entire_script(root_path):
    pt = start_pt()
    # print(type(pt))
    # print(pt)
    list_files(root_path, pt)
    pt.add_row([count_comment, count_blank, count_code, '合计'])
    print(pt)


def list_files(path, pt):
    global count_comment, count_blank, count_code, count_code_comment
    assert os.path.exists(path) is True, '输入的路径有问题！'
    for f in os.listdir(path):
        f_path = os.path.join(path, f)
        if os.path.isfile(f_path):
            if f.endswith('.py') or f.endswith('.qrc'):
                comment_lines, blank_lines, code_lines = deal_path_code(f_path, format='three')
                count_comment += comment_lines
                count_blank += blank_lines
                count_code += code_lines
                # count_4 += code_comment_lines
                pt.add_row([comment_lines, blank_lines, code_lines, os.path.basename(f_path)])
        elif os.path.isdir(f_path):
            list_files(f_path, pt)


if __name__ == '__main__':
    # if len(sys.argv) != 2:
    #     print("使用方式: python code_analyst.py [path]" + "\n"
    #           + "使用示例：python code_analyst.py D:\hj\pycode\gitlab_push\all-tools\朱昆-支付框选标注工具")
    # else:
    #     project_path = sys.argv[1]
    #     entire_script(project_path)
    path = r'D:\hj\pycode\gitlab_push\all-tools\朱昆-支付框选标注工具'
    entire_script(path)
