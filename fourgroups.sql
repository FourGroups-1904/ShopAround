-- 创建数据库
create database shoparound;

-- 切换数据库
use shoparound;


-- 建表

-- 京东
create table jd(
jd_id int primary key auto_increment,
jd_station varchar(10) default '京东',
store_names varchar(30),
shop_names varchar(100),
sale_volumes varchar(10),
prices float(7,2),
shop_urls varchar(1000),
pic_urls varchar(1000)
);

-- 淘宝
create table taobao(
taobao_id int primary key auto_increment,
taobao_station varchar(10) default '淘宝',
store_names varchar(30),
shop_names varchar(100),
sale_volumes varchar(10),
prices float(7,2),
shop_urls varchar(1000),
pic_urls varchar(1000)
);

-- 天猫
create table tmall(
tmall_id int primary key auto_increment,
tmall_station varchar(10) default '天猫',
store_names varchar(30),
shop_names varchar(100),
sale_volumes varchar(10),
prices float(7,2),
shop_urls varchar(1000),
pic_urls varchar(1000)
);

-- 清空表数据
# truncate jd;
-- 删除库名
# drop database shoparound;