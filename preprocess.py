# coding: utf-8
# __author__: u"John"
"""
这里存放数据预处理的内容, 也就是ETL部分
数据清洗根据不同的数据源有多种pipeline (class为单位), 每个pipeline都有好几步 (function为单位),
"""
from abc import abstractmethod
from helpers import *


class BaseETL(object):
    """
    抽象类
    每个继承BaseETL的类都需要Override [extract, transform, load] 这三个方法
    :return:
    """
    def __init__(self):
        self.file_name = ""
        self.data = None
        self.cleaned = False
        return

    @abstractmethod
    def extract(self):
        """
        数据抽取层, 文件读操作
        :return:
        """
        pass

    @abstractmethod
    def transform(self):
        """
        数据转换层、筛选、差值、标准化等操作
        :return:
        """
        pass

    @abstractmethod
    def load(self):
        """
        数据输出层, 文件写操作
        :return:
        """
        pass

    def etl(self, file_name):
        self.file_name = file_name
        self.extract()
        self.transform()
        self.load()
        return


class BankDetailETL(BaseETL):
    """
    清洗bank_detail_train.txt和bank_detail_test.txt文件
    """
    def __init__(self):
        BaseETL.__init__(self)
        return

    def extract(self):
        self.data = read_data_set(self.file_name, self.cleaned)
        return

    def transform(self):
        """
        1. <时间戳>转换
        2. <交易类型>转换
        3. <工资收入标记>转换
        :return:
        """
        self.data[u"时间戳"] = self.data[u"时间戳"].apply(unixtime_to_datetime)
        self.data[u"交易类型"] = self.data[u"交易类型"].apply(get_column_meaning(u"交易类型"))
        self.data[u"工资收入标记"] = self.data[u"工资收入标记"].apply(get_column_meaning(u"工资收入标记"))
        return

    def load(self):
        save_data_set(self.data, self.file_name)
        return
