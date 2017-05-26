# readwx
爬取搜狗微信保存mysql
创建人：杨闽

一：说明
因为工作中用到抓取微信与内外部网站进行同步，所以编写了此程序。
可以优化为爬虫程序。
建立表结构之后，修改运行test.py，数据会抓取到对应表。


二：数据库结构
-- ----------------------------
-- Table structure for zwxsougoupost
-- ----------------------------
DROP TABLE IF EXISTS `zwxsougoupost`;
CREATE TABLE `zwxsougoupost` (
  `id` int(11) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `biz` varchar(255) CHARACTER SET utf8 DEFAULT NULL COMMENT '文章对应的公众号biz',
  `field_id` varchar(30) DEFAULT NULL COMMENT '微信定义的一个id',
  `ztitle` varchar(255) DEFAULT '' COMMENT '文章标题',
  `title_encode` text CHARACTER SET utf8 COMMENT '文章编码 ,
  `zdesc` varchar(500) DEFAULT '' COMMENT '文章摘要',
  `zhref` varchar(500) CHARACTER SET utf8 DEFAULT NULL COMMENT '文章地址',
  `source_url` varchar(500) CHARACTER SET utf8 DEFAULT NULL COMMENT '阅读原文地址',
  `zimg` varchar(500) CHARACTER SET utf8 DEFAULT NULL COMMENT '封面图片',
  `is_multi` int(11) DEFAULT NULL COMMENT '是否多图文',
  `is_top` int(11) DEFAULT NULL COMMENT '是否头条',
  `ztime` date DEFAULT NULL,
  `readNum` int(11) DEFAULT '1' COMMENT '文章阅读量',
  `likeNum` int(11) DEFAULT '0' COMMENT '文章点赞量',
  `zcontent` text CHARACTER SET utf8,
  `isup` int(4) unsigned zerofill DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ztitle` (`ztitle`)
) ENGINE=MyISAM AUTO_INCREMENT=207 DEFAULT CHARSET=gbk;
