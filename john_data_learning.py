# coding: utf-8
# __author__: u"John"
"""
这里用来浏览数据集, 根据需要可以将这些代码运行在jupyter notebook上
"""
from helpers import read_data_set
from meta_data import TABLES


for table in TABLES:
    print read_data_set(table).describe()
