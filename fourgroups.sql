-- 创建数据库
create database shoparound;

-- 切换数据库
use shoparound;


-- 建表

-- 京东
create table jd(
jd_id int primary key auto_increment,
jd_station varchar(10) default '京东',
store_names varchar(200),
shop_names varchar(100),
prices float(8,2),
shop_urls varchar(1000),
pic_urls varchar(1000),
search_name varchar(20)
);

-- 一号店
create table yhd(
yhd_id int primary key auto_increment,
yhd_station varchar(10) default '一号店',
store_names varchar(200),
shop_names varchar(100),
prices float(8,2),
shop_urls varchar(1000),
pic_urls varchar(1000),
search_name varchar(20)
);

-- 考拉
create table kaolao(
kaolao_id int primary key auto_increment,
kaolao_station varchar(10) default '考拉',
store_names varchar(200),
shop_names varchar(100),
prices float(8,2),
shop_urls varchar(1000),
pic_urls varchar(1000),
search_name varchar(20)
);

select * from jd;
select * from kaolao;
select * from yhd;
-- 清空表数据
# truncate jd;
#drop database shoparound;