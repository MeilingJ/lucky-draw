from sqlalchemy import create_engine
# 添加包pymysql

conn_str = "mysql+pymysql://{user}:{pwd}@{host}:3306/{db_name}?charset=utf8mb4"

connect_info = conn_str.format(user='root',
                              pwd='12345678',
                              host='127.0.0.1',
                              db_name='test')
print("connect_info is: ", connect_info)

engine = create_engine(connect_info, echo=True, max_overflow=5)

result = engine.execute("select * from stu;")
print(result.fetchall())

result = engine.query("select * from stu;")
print(result)