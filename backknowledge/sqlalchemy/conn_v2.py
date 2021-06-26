from sqlalchemy import create_engine
# 添加包pymysql

conn_str = "mysql+pymysql://{user}:{pwd}@{host}:3306/{db_name}?charset=utf8mb4"

connect_info = conn_str.format(user='htc',
                              pwd='123456',
                              host='10.16.2.5',
                              db_name='test_td')
print("connect_info is: ", connect_info)

engine = create_engine(connect_info, echo=True, max_overflow=5)

result = engine.execute("select * from config;")
print(result.fetchall())

# result = engine.query("select * from config;")
# print(result)