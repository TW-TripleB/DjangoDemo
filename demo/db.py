# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymysql

conn = pymysql.connect(host='localhost',user='root',passwd='12345678',db='lcc')

cursor = conn.cursor()