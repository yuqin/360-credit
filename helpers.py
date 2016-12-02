# coding: utf-8
# __author__: u"John"
"""
这里存放一些公用的函数, 例如生成树、读写文件之类的
"""
from os.path import join, splitext
from meta_data import header
import pandas
import os


def read_data_set(file_name):
    """
    读取项目数据集, 并返回DataFrame
    例子:
        如果要读取bank_detail_test.txt,
        file_name 传入 "bank_detail_test.txt" 即可
    :param file_name: str
    :return:
    """
    dir_name = splitext(file_name)[0].split("_")[-1]
    file_full_path = join(join(os.getcwd(), dir_name), file_name)
    df = pandas.read_table(file_full_path, sep=",")
    df.columns = header.get(splitext(file_name)[0])
    return df

