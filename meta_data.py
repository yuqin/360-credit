# coding: utf-8
# __author__: u"John"
"""
这里存放的是元数据
header, 表头信息
relation, 字段关系
tables, 数据集信息
等信息
"""
from __future__ import unicode_literals
from os.path import join
from os import listdir, getcwd


header = dict(
    bank_detail_train=["用户id", "时间戳", "交易类型", "交易金额", "工资收入标记"],
    bank_detail_test=["用户id", "时间戳", "交易类型", "交易金额", "工资收入标记"],
    bill_detail_train=[
        "用户id", "账单时间戳", "银行id", "上期账单金额", "上期还款金额", "信用卡额度", "本期账单余额", "本期账单最低还款额",
        "消费笔数", "本期账单金额", "调整金额", "循环利息", "可用金额", "预借现金额度", "还款状态"
    ],
    bill_detail_test=[
        "用户id", "账单时间戳", "银行id", "上期账单金额", "上期还款金额", "信用卡额度", "本期账单余额", "本期账单最低还款额",
        "消费笔数", "本期账单金额", "调整金额", "循环利息", "可用金额", "预借现金额度", "还款状态"
    ],
    browse_history_train=["用户id", "时间戳", "浏览行为数据", "浏览子行为编号"],
    browse_history_test=["用户id", "时间戳", "浏览行为数据", "浏览子行为编号"],
    loan_time_train=["用户id", "放款时间"],
    loan_time_test=["用户id", "放款时间"],
    overdue_train=["用户id", "样本标签"],
    user_info_train=["用户id", "性别", "职业", "教育程度", "婚姻状态", "户口类型"],
    user_info_test=["用户id", "性别", "职业", "教育程度", "婚姻状态", "户口类型"],
    usersID_test=["用户id"],
)


tables = filter(lambda x: ".txt" in x, listdir(join(getcwd(), "train")) + listdir(join(getcwd(), "test")))
