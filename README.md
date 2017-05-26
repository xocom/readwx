# readwx
爬取搜狗微信保存mysql<br>
创建人：紫气东来<br>
因为工作中用到抓取微信与内外部网站进行同步，所以编写了此程序。<br>
程序思路：用selenium模拟手机登陆，下载对应HTML，再用BeautifulSoup解析html，存放mysql<br>
程序构建在py3.x基础上，可以优化为爬虫程序。<br>


一：使用说明<br>
1:程序使用了selenium，所以必须先安装chrome浏览器对应插件。<br>
&nbsp;&nbsp;插件下载地址：https://sites.google.com/a/chromium.org/chromedriver/downloads<br>
&nbsp;&nbsp;下载对应版本的EXE文件后，拷贝到chrome浏览器的目录，比如：C:\Program Files (x86)\Google\Chrome\Application<br>
&nbsp;&nbsp;V56-V57版本的chrome可以直接用plugin下的chromedriver<br>
<br>
2:建立表结构之后，修改运行<a href="https://github.com/xocom/readwx/blob/master/test.py" target="_blank">test.py</a>，数据会抓取到对应表。<br>
<br>
演示效果：<br>
![image](https://github.com/xocom/readwx/blob/master/screenshots/show1.png)
<br><br>
二：数据库结构<br>
-- ----------------------------<br>
-- Table structure for zwxsougoupost<br>
-- ----------------------------<br>
<p>
DROP TABLE IF EXISTS `zwxsougoupost`;<br>
CREATE TABLE `zwxsougoupost` (<br>
  `id` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT,<br>
  `biz` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '文章对应的公众号biz',<br>
  `field_id` varchar(30) DEFAULT NULL COMMENT '微信定义的一个id',<br>
  `ztitle` varchar(255) DEFAULT '' COMMENT '文章标题',<br>
  `title_encode` text CHARACTER SET utf8 COMMENT '文章编码 ,<br>
  `zdesc` varchar(500) DEFAULT '' COMMENT '文章摘要',<br>
  `zhref` varchar(500) CHARACTER SET utf8 DEFAULT NULL COMMENT '文章地址',<br>
  `source_url` varchar(500) CHARACTER SET utf8 DEFAULT NULL COMMENT '阅读原文地址',<br>
  `zimg` varchar(500) CHARACTER SET utf8 DEFAULT NULL COMMENT '封面图片',<br>
  `is_multi` int(11) DEFAULT NULL COMMENT '是否多图文',<br>
  `is_top` int(11) DEFAULT NULL COMMENT '是否头条',<br>
  `ztime` date DEFAULT NULL,<br>
  `readNum` int(11) DEFAULT '1' COMMENT '文章阅读量',<br>
  `likeNum` int(11) DEFAULT '0' COMMENT '文章点赞量',<br>
  `zcontent` text CHARACTER SET utf8,<br>
  `isup` int(4) unsigned zerofill DEFAULT NULL,<br>
  PRIMARY KEY (`id`),<br>
  UNIQUE KEY `ztitle` (`ztitle`)<br>
) ENGINE=MyISAM AUTO_INCREMENT=207 DEFAULT CHARSET=gbk;<br>
</p>
三：如果帮助到了您，欢迎请老师喝杯水，谢谢。【功德随意】<br>

![image](https://github.com/xocom/readwx/blob/master/screenshots/pay.png)
<br>
任何问题可以咨询QQ:153560261 (紫气东来)<br>