from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://htc:123456@10.16.2.5:3306/test_td?charset=utf8mb4",
    echo=True,
    max_overflow=5)

result = engine.execute("use test_td;")
result = engine.execute("select * from config;")
print(result.fetchall())

