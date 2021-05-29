
from sqlalchemy.orm import sessionmaker
from p11_sqlalchemy.orm_create_allflow import Person, engine, session

p_data1 = Person(name='amity',
               age='19')

p_data2 = Person(name='lala',
               age='19')

p_data3 = Person(name='zz',
               age='20')

session.add(p_data1)
session.add(p_data2)
session.add(p_data3)
session.commit()
