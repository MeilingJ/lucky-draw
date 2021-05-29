from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

'''
hive://hive@10.16.100.1:10000/test_grl

conn_v3和conn_v4的区别是什么

'''


engine = create_engine("hive://hive@10.16.100.1:10000/test_grl", pool_recycle=1800)

# 把当前的引擎绑定给这个会话, 即创建session工厂DBSession
DBSession = sessionmaker(engine)
# 根据session工厂DBSession创建session对象，实例话session，可对表中数据操作
session = DBSession()

rows = session.execute("select count(1) from test_grl.source1").first()

print(rows)
print(type(rows))

# 打印执行结果
# rows = [row for row in rows]
print(rows)
print(rows[0])
print(int(rows[0]))
