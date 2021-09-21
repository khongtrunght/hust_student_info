import json

from hust_student.parse_model.class_parse import ClassParse
from hust_student.schemas import *
from hust_student import models
from hust_student.database import Base, engine, SessionLocal
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)

Base.metadata.create_all(engine)

with open('../resourse/test.json') as file:
    data = json.load(file)
    log.info(data['data']['name'])
    cr = ClassResp.parse_obj(data)
    class_parser = ClassParse(SessionLocal())
    class_parser.parse_pydantic(cr.data)

    # obj = ClassDB.parse_obj(cr.data)
    # EXCLUDE = {}
    # test_obj = models.Class(**obj.dict())
    # r_u = RootUnitDB.parse_obj(cr.data.rootUnit)
    # root_unit = models.RootUnit(**r_u.dict())
    # te = TeacherDB.parse_obj(cr.data.teacher)
    # # teacher = models.Teacher(**te.dict())
    # print(root_unit.abbrName)
