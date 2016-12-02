# coding: utf-8
# __author__: u"John"
"""
这里存放数据预处理的内容, 也就是ETL部分
数据清洗根据不同的数据源有多种pipeline (class为单位), 每个pipeline都有好几步 (function为单位),
"""
from abc import abstractmethod


class BaseETL(object):
    """
    抽象类
    每个继承BaseETL的类都需要Override [extract, transform, load] 这三个方法
    :return:
    """
    def __init__(self):
        self.data = None

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

    def etl(self):
        self.extract()
        self.transform()
        self.load()
