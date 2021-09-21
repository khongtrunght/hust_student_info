from hust_student import schemas
from hust_student.models import RootUnit, Teacher, Class
from hust_student.parse_model.root_unit_parse import RootUnitParse
from hust_student.parse_model.teacher_parse import TeacherParse
from hust_student.schemas import RootUnitDB, TeacherDB, ClassDB


class ClassParse:
    def __init__(self, db):
        self.db = db
        self.root_unit_parser = RootUnitParse(self.db)
        self.teacher_parser = TeacherParse(self.db)


    def parse_pydantic(self, lop: schemas.Class):
        if lop:
            if not self.db.query(Class).filter(Class.id==lop.id).first():
                self.root_unit_parser.parse_pydantic(lop.rootUnit)
                self.teacher_parser.parse_pydantic(lop.teacher)
                class_obj = ClassDB.parse_obj(lop)
                db_obj = Class(**class_obj.dict())
                self.db.add(db_obj)
                self.db.commit()




