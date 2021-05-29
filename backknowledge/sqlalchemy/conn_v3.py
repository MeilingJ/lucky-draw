from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

'''
python3 __main__.py hive hive://hive@10.16.100.1:10000/test_grl source 2 --locale zh_CN 
--meta /Users/andy/PycharmProjects/hypersfaker/tests/data/meta_hive.txt

'''
engine = create_engine(
    "hive://hive@10.16.100.1:10000/test_grl",
    echo=True,
    max_overflow=5)

result = engine.execute("select * from source1")
print(result)
# print("fetchone", result.fetchone()) # 获取第一条记录, result的游标指向第2条
# print("first", result.first()) # 获取第一条记录, This result object is closed, 跟上条语句的区别是执行该行后result游标指向末尾，所以无法再打印result的结果
print("fetchmany", result.fetchmany()) # 获取result的所有的结果,list类型，每条记录是元祖类型, 执行该行后result游标还是指向开头
# print("fetchall", result.fetchall()) # 获取result的所有的结果,list类型，每条记录是元祖类型, 跟上条语句的区别是执行该行后result游标指向末尾

#也可以循环获得
for i in result:
    print('===', i)

