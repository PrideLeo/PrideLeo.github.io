#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:31:38 2021

@author: lizihao
"""

from pyecharts.charts import WordCloud

src_filename = './data/人物出场次数.csv'
src_file = open(src_filename,'r')
line_list = src_file.readlines()
src_file.close()

#print (line_list)
del line_list[0]

word_freq = []

for line in line_list:
    line = line.strip()
    line_split = line.split(',')
    word_freq.append((line_split[0],line_split[1]))
    
#print (word_freq)

cloud = WordCloud()
cloud.add('',word_freq)

output_filename = './output/word_frequency.html'
cloud.render('output_filename')

print('已生成文件：' + output_filename)