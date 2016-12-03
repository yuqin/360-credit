# coding: utf-8
# __author__: u"John"
from helpers import *
from preprocess import *
# from model_research import *

file_name = "bank_detail_train.txt"
BankDetailETL().etl(file_name)
print read_data_set(file_name, True).head()
