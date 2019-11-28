import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='47.103.15.202',
    port=3306,
    user='leec',
    passwd='gt12345',
    db='gt',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()

sql = """
CREATE TABLE USER1 (
id INT auto_increment PRIMARY KEY ,
name CHAR(10) NOT NULL UNIQUE,
age TINYINT NOT NULL
)ENGINE=innodb DEFAULT CHARSET=utf8;
"""

# 执行SQL语句
cursor.execute(sql)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
connect.close()

