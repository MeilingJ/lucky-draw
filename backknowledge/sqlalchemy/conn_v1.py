from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:12345678@127.0.0.1:3306/test?charset=utf8mb4",
    echo=True,
    max_overflow=5)

result = engine.execute("use test;")
result = engine.execute("select * from stu;")
print(result.fetchall())