# coding: utf-8
# __author__: u"John"
"""
这里用来浏览数据集, 根据需要可以将这些代码运行在jupyter notebook上
"""
from os.path import join, splitext
from meta_data import header
import pandas
import os


bank_detail_file_name = "bank_detail_test.txt"
dir_name = splitext(bank_detail_file_name)[0].split("_")[-1]
bank_detail_file = join(join(os.getcwd(), dir_name), bank_detail_file_name)
bank_detail_df = pandas.read_table(bank_detail_file, sep=",")
bank_detail_df.columns = header.get(splitext(bank_detail_file_name)[0])
print header.get(splitext(bank_detail_file_name)[0])
print bank_detail_df.head(3)
