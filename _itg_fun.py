# coding = utf-8
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import parse
from selenium.common.exceptions import TimeoutException
# 引入ActionChains鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains
import time
import pymysql
import urllib.request
import sys
#补充下载图片   【特别注意，下载时不能用国贸内网，否则会提示：已经被上网策略[<font color=red id="strPlc"></font>]拒绝访问】
import urllib.request
import binascii
import os
import requests
import re
#补充多线程
import threading

def saveHandler(start, end, url, filename):
    headers = {'Range': 'bytes=%d-%d' % (start, end)}
    r = requests.get(url, headers=headers, stream=True)

    # 写入文件对应位置
    with open(filename, "r+b") as fp:
        fp.seek(start)
        var = fp.tell()
        fp.write(r.content)

#多线程下载
def threading_download_file(url, position, field_id, file_name, num_thread=5):
    r = requests.head(url)
    try:
        # file_name = "demo.rar"
        # field_id="ymtest"
        str_position = position + str(field_id) + '\\'
        if not os.path.isdir(str_position):
            os.makedirs(str_position)


        # file_name = url.split('/')[-1]
        file_size = int(
            r.headers['content-length'])  # Content-Length获得文件主体的大小，当http服务器使用Connection:keep-alive时，不支持Content-Length
    except:
        print("检查URL，或不支持对线程下载")
        return

    # 创建一个和要下载文件一样大小的文件
    str_position = str_position + file_name
    fp = open(str_position, 'wb')
    # fp = open(file_name, "wb")
    fp.truncate(file_size)
    fp.close()

    # 启动多线程写文件
    part = file_size // num_thread  # 如果不能整除，最后一块应该多几个字节
    for i in range(num_thread):
        start = part * i
        if i == num_thread - 1:  # 最后一块
            end = file_size
        else:
            end = start + part

        t = threading.Thread(target=saveHandler, kwargs={'start': start, 'end': end, 'url': url, 'filename': str_position})
        t.setDaemon(True)
        t.start()

    # 等待所有线程下载完成
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    print('%s 下载完成' % file_name)
