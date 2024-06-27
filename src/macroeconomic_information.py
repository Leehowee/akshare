#! /usr/bin/env python
# -*- coding: utf-8 -*-


"""
#***************************************************************************
# *
# * Copyright (c) 2024 SCUT All Rights Reserved
# *
# * Filename   :    cctv_news.py
# * Author     :    lizhihao(lizhihaohenry@gmail.com)
# * Date       :    2024/06/26 14:44:02
# * Dopyright (c) 2024 SCUT All Rights Reserved
# *
# * Filename   :    cctv_news.py
# * Author     :    lizhihao(lizhihaohenry@gmail.com)
# * Date       :    2024/06/26 14:44:02
# * Description:
# *
#***************************************************************************
"""

"""
macroeconomic information
获取宏观信息情报
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

# 获取当前工作目录
current_dir = os.getcwd()

def gen_cctv_news_by_day(minute_time):
	""" gen cctv news by day
	    获取天级别新闻联播信息
	"""
	day_set=set()
	for mt in minute_time:
		day_set.add(mt[:8])
	days = list(day_set)

	for day in days:
		# 相对路径
		relative_path = "../data/cctv_news/%s.txt" % day
		# 判断文件是否存在
		# 构建完整的文件路径
		file_path = os.path.join(current_dir, relative_path)
		if os.path.exists(file_path):
		    print("The file %s exists." % file_path)
		    continue
		else:
		    print("The file %s does not exist." % file_path)
		    news_cctv_df = ak.news_cctv(date=day)
		    news_cctv_df.to_csv(file_path, sep=',', index=True)

def gen_monitor_data():
	"""获取新闻个股数据
	"""
	# 获取需要爬取的股票list
	file_path = os.path.join(current_dir, "../conf/stocks_list.conf")
	# 参数为股票代码
	stocks = []
	with open(file_path) as rf:
		for line in rf:
			stocks.append(int(line.strip('\n')))
	for stock in stocks:
		save_path = os.path.join(current_dir, "../data/monitor/%s_news.txt" % str(stock))
		stock_df = ak.stock_news_em(stock)
		stock_df.to_csv(save_path, sep=',', index=True)


def gen_china_macro_index_data():
	"""获取中国宏观指数数据
	"""
	# LPR
	LPR_path = os.path.join(current_dir, "../data/macro_index/china_LPR.txt")
	LPR = ak.macro_china_lpr()
	print(LPR)
	LPR.to_csv(LPR_path, sep=',', index=True)

	# CPI monthly
	CPI_monthly_path = os.path.join(current_dir, "../data/macro_index/china_CPI_monthly.txt")
	CPI_monthly = ak.macro_china_cpi_monthly()
	CPI_monthly.to_csv(CPI_monthly_path, sep=',', index=True)

	# CPI yearly
	CPI_yearly_path = os.path.join(current_dir, "../data/macro_index/china_CPI_yearly.txt")
	CPI_yearly = ak.macro_china_cpi_yearly()
	CPI_yearly.to_csv(CPI_yearly_path, sep=',', index=True)

	# 贸易

	# 产业指标

	# 等等


