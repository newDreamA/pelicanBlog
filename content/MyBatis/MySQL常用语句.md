Date:7/12/2016 2:50:40 PM 
Title:Mysql常见一些操作语句
##Mysql常见一些操作语句
#####1. 创建数据库的：
CREATE DATABASE IF NOT EXISTS auth DEFAULT CHARSET utf8 COLLATE utf8\_general_ci;
#####2. 自增类型定义:
auto\_increment
#####3. 时间日期的格式化：
DATE\_FORMAT(time,'%y-%m-%d %T')  
mySql的日期格式化示例： DATE_FORMAT(date, format)   

- select date_format(now(),'%y-%m-%d');
- format参数说明：
- %S, %s 两位数字形式的秒（ 00,01, ..., 59）
- %I, %i 两位数字形式的分（ 00,01, ..., 59）
- %H 两位数字形式的小时，24 小时（00,01, ..., 23）
- %h 两位数字形式的小时，12 小时（01,02, ..., 12）
- %k 数字形式的小时，24 小时（0,1, ..., 23）
- %l 数字形式的小时，12 小时（1, 2, ..., 12）
- %T 24 小时的时间形式（hh:mm:ss）
- %r 12 小时的时间形式（hh:mm:ss AM 或hh:mm:ss PM）
- %p AM或PM
- %W 一周中每一天的名称（Sunday, Monday, ..., Saturday）
- %a 一周中每一天名称的缩写（Sun, Mon, ..., Sat）
- %d 两位数字表示月中的天数（00, 01,..., 31）
- %e 数字形式表示月中的天数（1, 2， ..., 31）
- %D 英文后缀表示月中的天数（1st, 2nd, 3rd,...）
- %w 以数字形式表示周中的天数（ 0 = Sunday, 1=Monday, ..., 6=Saturday）
- %j 以三位数字表示年中的天数（ 001, 002, ..., 366）
- %U 周（0, 1, 52），其中Sunday 为周中的第一天
- %u 周（0, 1, 52），其中Monday 为周中的第一天
- %M 月名（January, February, ..., December）
- %b 缩写的月名（ January, February,...., December）
- %m 两位数字表示的月份（01, 02, ..., 12）
- %c 数字表示的月份（1, 2, ...., 12）
- %Y 四位数字表示的年份
- %y 两位数字表示的年份
- %% 直接值“%”
#####4.插入数据检查数据是否存在：
 当记录不存在的时插入，当记录存在时更新  
 在insert中使用 ON DUPLICATE KEY UPDATE 
#####5. 解决datetime类型的比较问题，
使用STR_TO_DATE函数，例如  add_time >=STR_TO_DATE('2016-06-28 13:22:12','%Y-%m-%d %H:%i:%s')
#####6. 删除原先主键，重新生成主键
ALTER TABLE table_name
ADD COLUMN id  INT(11) NOT NULL AUTO_INCREMENT AFTER name_field,
DROP PRIMARY KEY,
ADD PRIMARY KEY (id);
