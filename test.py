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
#补充下载图片
import urllib.request
import binascii
import os
import requests
import re
#补充多线程
import threading




# 模拟鼠标滑动
def myscroll(driver):
    driver.execute_script("""
        (function () {
            var y = document.body.scrollTop;
            var step = 100;
            window.scroll(0, y);


            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 50);
                }
                else {
                    window.scroll(0, y);
                    document.title += "scroll-done";
                }
            }


            setTimeout(f, 1000);
        })();
        """)


#Step1.根据浏览器请求，得到HTML文件，并保存
#模拟IOS6
def gethtml(zurl,str_fname):
    mobileEmulation = {'deviceName': 'Apple iPhone 6'}
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)


    driver.get(zurl)
    time.sleep(5)
    result = []


    # for i in range(0,300):  #依次把0到20保存在变量i中
    for i in range(0, 1):  # 依次把0到3保存在变量i中
        print('循环取数' + str(i))
        myscroll(driver)
        time.sleep(2)

    st=time.strftime("%Y%m%d",time.localtime())
    # print(driver.page_source, file=open('itg201703.html', 'w', encoding='utf-8'))
    print(driver.page_source, file=open(str_fname+"-"+st+".html", 'w', encoding='utf-8'))
    print("取数成功，请核对！")
    print(driver.title)
    driver.quit()

def read(str_fname,str_tname):
    print("开始读HTML")
    st = time.strftime("%Y%m%d", time.localtime())
    file = open(str_fname+"-"+st+".html",'r',encoding='utf-8')
    soup = BeautifulSoup(file,"html.parser")
    msgs = soup.find_all(class_='txt-box')
    # print(msgs)
    # sys.exit(0)

    msgs = soup.find_all(class_='tit')
    # print(msgs)

    # msgs num
    print('取得tit数：' + str(len(msgs)))

    if((len(msgs))==0):
        print("ERROR:未能取得数据，请检查URL地址KEY是否正确！")
        sys.exit()
    j=0
    for sp in msgs:
        j=j+1
        print('正在处理：'+str(j))
        if sp.find('a') is None:
            continue
        else:
            # print(sp.find('a'))
            #拼接出文章对应图片
            # print("href is:"+sp.find('a').get("href"))
            return  sp.find('a').get("href")

##插入
def insert(sql):
            conn = pymysql.connect("localhost", "root", "root", "test", port=3306, charset='utf8')
            cur = conn.cursor()
            print(sql)
            sta = cur.execute(sql)
            if sta == 1:
                print('Done sql')
            else:
                print('Failed sql.')
            conn.commit()
            cur.close()
            conn.close()

# Step2.读取HTML文件，并保存到MYSQL
def insert_to_mysql():
            print("开始读HTML")
            st = time.strftime("%Y%m%d", time.localtime())
            file = open("Zlist-" + st + ".html", 'r', encoding='utf-8')
            soup = BeautifulSoup(file, "html.parser")


            msgs = soup.find_all(class_='weui_media_box')
            # print(msgs)

            # msgs num
            print('取得节点新闻数：' + str(len(msgs)))

            if ((len(msgs)) == 0):
                print("ERROR:未能取得数据，请检查URL地址KEY是否正确！")
                sys.exit()

            content = ''
            sql = ''
            j = 0
            for sp in msgs:
                j = j + 1
                print('正在处理：' + str(j))
                if sp.find(class_='weui_media_bd') is None or sp.find(class_='weui_media_bd').find('h4') is None:
                    continue
                elif sp.find(class_='weui_media_bd').find('h4').string is None:
                    # print("error title is:"+sp.find(class_='weui_media_bd'))  #Can't convert 'Tag' object to str implicitly
                    continue
                else:
                    # 拼接出文章对应图片
                    zimg = sp.find('span').attrs['style'] + '?wx_fmt=jpeg'
                    zimg = zimg.replace('background-image:url(', '').replace(')', '')
                    # content = zimg+'\n'
                    # 得到标题，去除空格
                    ztitle = sp.find(class_='weui_media_bd').find('h4').string.strip()
                    ztitle = ztitle.replace('\'', '\"')
                    ztitle = ztitle.replace('?', '')
                    # content = ztitle+'\n'
                    # 得到文章超链接地址
                    zhref = "http://mp.weixin.qq.com"+sp.find(class_='weui_media_bd').find('h4').attrs['hrefs']
                    # content = zhref+'\n'
                    # 得到文章描述,分析有两个P标签，只取得第一个P标签下的内容；而且有的数据为空要进行判断
                    # zdesc=sp.find(class_='weui_media_bd').find('p').find(class_='weui_media_desc').string
                    zdesc = sp.find(class_='weui_media_bd').find_all('p')[0].string
                    if sp.find(class_='weui_media_bd').find_all('p')[0].string is None:
                        # print(sp.find(class_='weui_media_bd').find_all('p')[0].string)
                        zdesc = ''
                    else:
                        zdesc = sp.find(class_='weui_media_bd').find_all('p')[0].string
                        zdesc = zdesc.replace('\'', '\"')
                    # content = content+zdesc+'\n'

                    # 拼接出时间
                    ztime = sp.find(class_='weui_media_bd').find_all('p')[1].string
                    # content = content+ztime+'\n'

                    zbiz = ""
                    zfield_id = ""

                    #sql = 'replace into zwxsougoupost(biz,field_id,ztitle,zimg,zhref,zdesc,ztime) values(\'' + zbiz + '\',\'' + zfield_id + '\',\'' + ztitle + '\',\'' + zimg + '\',\'' + zhref + '\',\'' + zdesc + '\',\'' + ztime + '\')' + ';\n'
                    sql = 'insert into zwxsougoupost(biz,field_id,ztitle,zimg,zhref,zdesc,ztime) ' \
                          'select \'' + zbiz + '\',\'' + zfield_id + '\',\'' + ztitle + '\',\'' + zimg + '\',\'' + zhref + '\',\'' + zdesc + '\',\'' + ztime + '\' from dual ' \
                          + ' where not EXISTS (select ztitle from zwxsougoupost where ztitle = \'' + ztitle + '\')\n'
                    print("insert sql is:"+sql)


                    # 逐条写入：
                    insert(sql)
                    content = content + sql

            with open("zitgupdateSQL-" + st + ".html", 'w', encoding='utf-8') as f:
                f.write(content)

            print("读取HTML结束!")




# #Step1：模拟浏览器读取搜狗ITGCHINA微信公众号
zurl = "http://weixin.sogou.com/weixin?type=1&query=gwlianwu&ie=utf8&_sug_=n&_sug_type_="
print(zurl)
gethtml(zurl,"Z_SOUGOU_gwlianwu")

#Step2：得到文章列表HTML保存到 Zlist-20170411.html
str_url = read("Z_SOUGOU_gwlianwu","Zlist")
print(str_url)
gethtml(str_url,"Zlist")

# #Step3：读取信息写入mysql
insert_to_mysql()

