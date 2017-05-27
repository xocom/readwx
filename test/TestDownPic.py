
#补充下载图片
import urllib.request
import binascii
import os
import requests
import re
#补充多线程
import threading

#引用统一目录下的PY文件下函数
import sys

import _itg_fun #如果是同一个目录，就直接引用，只包含这句，就用：_itg_fun.threading_download_file()
from _itg_fun import threading_download_file #引用模块中的函数，引用后可以直接使用 threading_download_file()





if __name__ == "__main__":
    img_init_url = "http://www.itg.com.cn/Manager/images/systemlogo.gif"
    position = 'd:\\temp\\sougou\\'
    field_id="ymtest"
    file_name="systemlogo.gif"
    threading_download_file(img_init_url, position, str(field_id), file_name, num_thread=1)
