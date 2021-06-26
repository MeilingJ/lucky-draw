from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

'''
conn_v4和conn_v5的区别是什么？

conn_v5编写原则是session创建和操作事务的方法分离开来，然后在main方法中调用创建session和操作事物的方法。
'''

class SomeThing(object):

    def run_sql(self, session):
        '''
        这是操作事物的方法，定义在某类中
        :param session:
        :return:
        '''
        result = session.execute("show databases")
        return result


# utils方法
def create_session():
    conn_str = "mysql+pymysql://{user}:{pwd}@{host}:3306/{db_name}?charset=utf8mb4"

    connect_info = conn_str.format(user='htc',
                                   pwd='123456',
                                   host='10.16.2.5',
                                   db_name='test_td')

    engine = create_engine(connect_info, pool_recycle=1800)

    # 把当前的引擎绑定给这个会话, 即创建session工厂DBSession
    DBSession = sessionmaker(engine)
    # 根据session工厂DBSession创建session对象，实例话session，可对表中数据操作
    session = DBSession()
    return session


if __name__ == '__main__':

    session = create_session()
    try:
        result = SomeThing().run_sql(session)
        # 打印结果
        result = [row for row in result]
        print(result)

        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()