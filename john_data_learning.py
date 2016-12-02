# coding: utf-8
# __author__: u"John"
"""
这里用来浏览数据集, 根据需要可以将这些代码运行在jupyter notebook上
"""
from helpers import read_data_set
from meta_data import tables
import traceback


for table in tables:
    try:
        print read_data_set(table).head(3)
    except:
        print "\n" + "-" * 100
        print table
        traceback.print_exc()
        print "-" * 100 + "\n"
        continue

