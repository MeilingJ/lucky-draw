# -*- encoding: utf-8 -*-
import datetime

from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from common import logger
from common.db import orm
from common.db.orm import Base, get_session
from common.utils.date import get_time_now
from apps.tool.check_top1.form import CheckTop1AllMsg, convert_real2str, convert_str2real, CheckSqlsStrRecord
from apps.tool.check_top1.form import CheckSqlsRecord


class CheckTop1(Base):
    __tablename__ = 'tool_check_top1'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    db = Column(String(50))
    table_name = Column(String(50))
    cols_group = Column(String(300))
    cols_sort = Column(String(300))
    cols_filter = Column(String(300))
    col_key = Column(String(50))
    sql1_unstable_source_count = Column(String(1000))
    sql2_unstable_detail = Column(String(1000))
    sql3_unstable_target_count = Column(String(1000))
    created_time = Column(DateTime, default=datetime.datetime.utcnow)

    @staticmethod
    def save_record(item: CheckTop1AllMsg, db: Session):
        # 存储到数据库

        # 将item中所有value转str
        item_str = convert_real2str(item)

        data_record = CheckTop1(**item_str.dict(), created_time=get_time_now())

        orm.add(data_record, db)

        return data_record

    @staticmethod
    def get_latest_record(db: Session):
        try:
            data_record = db.query(CheckTop1).order_by(CheckTop1.id.desc()).filter().first()
            return data_record
        except NoResultFound:
            logger.error("The latest record id is: {}".format(data_record.id))
        except Exception as e:
            logger.error(e)

    @staticmethod
    def get_record(record_id: int, db: Session):
        try:
            data_record = db.query(CheckTop1).filter(CheckTop1.id == record_id).one()
            return data_record
        except NoResultFound:
            logger.error("The record {} is not found in db! ".format(data_record.id))
        except Exception as e:
            logger.error(e)

    def record_to_model(self) -> CheckSqlsRecord:
        # 将数据库记录转换成CheckSqlsRecord model类型
        # TODO 待优化

        # 将model转换成dict类型
        data_dict_real = self.to_dict()

        # 由于字典类型中有特殊类型datetime，将字典转换成value为str的字典
        data_dcit_str = jsonable_encoder(data_dict_real)

        # 将字典转换成model类型
        data_model_str = CheckSqlsStrRecord(**data_dcit_str)

        # 将model类型转换成含特殊类型值的model类型，特殊类型如list、dict
        data_model_real = convert_str2real(data_model_str)

        return data_model_real

    @staticmethod
    def get_records(page, size, db: Session):
        # 分页获取所有历史记录
        offset = (page - 1) * size
        try:
            data_records = db.query(CheckTop1).order_by(CheckTop1.id.desc()).offset(offset).limit(
                size).all()
            count = db.query(func.count(CheckTop1.id)).scalar()
            return data_records, count
        except Exception as e:
            logger.error(e)

    @staticmethod
    def operate_record(record_id: int, item: CheckSqlsRecord, db: Session):
        try:
            data_record = CheckTop1.get_record(record_id, db)

            data_record.db = item.db
            data_record.table_name = item.table_name
            data_record.cols_group = str(item.cols_group)
            data_record.cols_sort = str(item.cols_sort)
            data_record.cols_filter = str(item.cols_filter)
            data_record.col_key = item.col_key
            data_record.sql1_unstable_source_count = item.sql1_unstable_source_count
            data_record.sql2_unstable_detail = item.sql2_unstable_detail
            data_record.sql3_unstable_target_count = item.sql3_unstable_target_count

            db.commit()
            db.refresh(data_record)
            return data_record

        except NoResultFound:
            logger.error("The record {} is not found in db! ".format(record_id))

        except InvalidRequestError as e:
            logger.error(e)
            db.rollback()

if __name__ == "__main__":
    g = get_session()
    db = next(g)

    item = {"cols_sort": {"created_time": "desc", "db": "asc"}, "table_name": "tool_check_top1", "col_key": "sql1",
            "cols_group": ["db", "table_name"],
            "db": "htc-test", "cols_filter": ["db = 'htc-test'"], "sql2_unstable_detail": "sql2",
            "sql1_unstable_source_count": "sql1", "sql3_unstable_target_count": "sql3"}

    data_record = CheckTop1.get_record(1, db)

    data_model = data_record.record_to_model()
    data_model.table_name = "aaaa"
    print(data_model)
    CheckTop1.operate_record(1, data_model, db)

    # 如何将data record转换成对应的model类型？？？

    # 如何将model转换成record？
    # model类型的转字典类型item_model.dict()，然后在作为表类的参数得到record记录
