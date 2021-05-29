
from sqlalchemy.orm import sessionmaker
from p11_sqlaichemy.orm_create_v2 import Person, engine, session

# 所有数据，且结果集中是一个一个的对象, 一行数据为一个对象
ret = session.query(Person).all()
print("查询所有结果数据：", ret)
# 结果 [obj1, obj2, obj3]

#  指定字段查询，返回所有的数据，是一个列表，列表内是一个一个的元组
ret = session.query(Person.name, Person.age).all()
print("查询字段所有结果数据：", ret)
# 结果 [('yangge', '18'), ('qiangge', '19'), ('shark', '23')]


# 迭代查询结果
for name, age, in session.query(Person.name, Person.age):
    print("person name is {}, and age is {} ....".format(name, age))

# 返回的是对象
ret = session.query(Person).filter_by(name='zz').one()
print("查询one()结果数据：", ret.id, ret.name, ret.age, type(ret))

# 返回的是对象
ret = session.query(Person).filter_by(name='zz').scalar()
print("查询scalar()结果数据：", ret.id, ret.name, ret.age, type(ret))