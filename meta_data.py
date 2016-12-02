# coding: utf-8
# __author__: u"John"
"""
这里存放的是元数据
header, 表头信息
relation, 字段关系
等信息
"""
from __future__ import unicode_literals


header = dict(
    bank_detail_train=["用户id", "时间戳", "交易类型", "交易金额", "工资收入标记"],
    bank_detail_test=["用户id", "时间戳", "交易类型", "交易金额", "工资收入标记"],
    bill_detail_train="",
    bill_detail_test="",
    browse_history_train="",
    browse_history_test="",
    loan_time_train="",
    loan_time_test="",
    overdue_train="",
    user_info_train="",
    usersID_test="",
)
