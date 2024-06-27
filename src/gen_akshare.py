#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""
#***************************************************************************
# *
# * Copyright (c) 2024 SCUT All Rights Reserved
# *
# * Filename   :    gen_akshare.py
# * Author     :    lizhihao(lizhihaohenry@gmail.com)
# * Date       :    2024/06/26 14:44:02
# * Dopyright (c) 2024 SCUT All Rights Reserved
# *
# * Filename   :    gen_akshare.py
# * Author     :    lizhihao(lizhihaohenry@gmail.com)
# * Date       :    2024/06/26 14:44:02
# * Description:
# *
#***************************************************************************
"""

"""
金融数据分析入口
"""
import os
import sys
import json
import datetime
import time
import requests
import argparse
import akshare as ak
import pandas as pd
from macroeconomic_information import *

class GenTask(object):
    """ 样本生成类 """
    def __init__(self, args):
        """ init """
        self.start_time = args.start
        self.end_time = args.end
        self.task_type = args.task_type
        # 生成区间十分钟 list
        self.gen_date_minute()
    
    
    def gen_date_minute(self):
        """ create spark object """
        self.date_minute = [] 
        start = datetime.datetime.strptime(self.start_time, "%Y%m%d%H%M") 
        end = datetime.datetime.strptime(self.end_time, "%Y%m%d%H%M")
        while start <= end: 
            minute_time = start.strftime("%Y%m%d%H%M") 
            self.date_minute.append(minute_time) 
            start += datetime.timedelta(minutes=10)
        return self.date_minute

    
    def gen_data(self):
        """ gen data """
        gen_cctv_news_by_day(self.date_minute)
        gen_monitor_data()
        gen_china_macro_index_data()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', help='start time',
                        type=str, default='202406240000')
    parser.add_argument('--end', help='end time',
                        type=str, default='202406240100')
    parser.add_argument('--task_type', help='task_type',
                        type=str, default='')
    parser.add_argument
    args = parser.parse_args()
    
    # 开始运行
    gen_data = GenTask(args)
    gen_data.gen_data()
