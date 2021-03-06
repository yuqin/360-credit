# coding: utf-8
# __author__: u"John"
"""
这里存放一些公用的函数, 例如生成树、读写文件之类的
"""
from os.path import join, splitext
from meta_data import HEADERS, ENCODING, COLUMNS
from datetime import datetime
import pandas
import time
import os


def read_data_set(file_name, cleaned=False):
    """
    读取项目数据集, 并返回DataFrame
    例子:
        如果要读取bank_detail_test.txt,
        file_name 传入 "bank_detail_test.txt" 即可
    :param file_name: str
    :param cleaned:
    :return:
    """
    df = pandas.read_table(get_file_path(file_name, cleaned), sep=",")
    df.columns = HEADERS.get(splitext(file_name)[0])
    return df


def unixtime_to_datetime(unix_time):
    """
    将数据集中unixtime的时间类型转换成python的datetime类型
    :param unix_time: int / long / str  "5894321388"
    :return: datetime
    """
    try:
        unix_time = int(unix_time)
        return datetime.fromtimestamp(unix_time).strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        return unix_time


def get_file_path(file_name, cleaned=False):
    """
    查找文件名所在的绝对路经
    :param file_name:
    :param cleaned:
    :return:
    """
    f_name, ext = splitext(file_name)
    dir_name = f_name.split("_")[-1]

    if cleaned:
        dir_name = "cleaned_{0}".format(dir_name)

    if not ext:
        ext = ".txt"

    return join(join(os.getcwd(), dir_name), f_name + ext)


def save_data_set(data, file_name, cleaned=True):
    """
    存放数据集
    如果是存放清洗后的数据集, 格式和清洗前保持一致:
        1. 无表头
        2. 逗号分隔符
    :param data: DataFrame
    :param file_name: str
    :param cleaned:
    :return:
    """
    file_name = get_file_path(file_name, cleaned)
    data.to_csv(file_name, HEADERS=False, encoding=ENCODING, index=False)
    return


def get_column_meaning(column_name):
    """
    传入字段名, 获取字段里所有值的含义
    通过一个闭包函数传递这种关系
    :param column_name:
    :return:
    """
    meaning = COLUMNS.get(column_name)

    def translate_meaning(original_column_value):
        translated_column_value = meaning.get(original_column_value)
        return translated_column_value

    return translate_meaning


def time_elapsed(function):
    """
    计算函数调用CPU时钟的decorator, 单位是秒
    例:
    @time_elapsed
    def foo():
        return [i for i in xrange(100000)]
    :param function:
    :return:
    """
    def wrapper(*args, **kwargs):
        start = time.clock()
        function(*args, **kwargs)
        end = time.clock()
        print "ELAPSE: function '{0}' elapse {1} seconds".format(function.__name__, end - start)
    return wrapper
