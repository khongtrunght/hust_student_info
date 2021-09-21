from hust_student import schemas
from hust_student.models import Teacher, TeacherEmail, TeacherPhoneNumber
from hust_student.schemas import TeacherDB


class TeacherParse:
    def __init__(self, db):
        self.db = db
        self.teacher_email_parser = TeacherEmailParse(self.db)
        self.teacher_phone_parser = TeacherPhoneParse(self.db)
    def parse_pydantic(self, teacher: schemas.Teacher):
        if teacher:
            if not self.db.query(Teacher).filter(Teacher.id == teacher.id).first():
                teacher_obj = TeacherDB.parse_obj(teacher)
                db_obj = Teacher(**teacher_obj.dict())
                self.db.add(db_obj)
                self.db.commit()
                for email in teacher.allEmails:
                    self.teacher_email_parser.parse_pydantic(teacher.id, email)
                for phone in teacher.otherPhoneNumbers:
                    self.teacher_phone_parser.parse_pydantic(teacher.id, phone)




class TeacherEmailParse:
    def __init__(self, db):
        self.db = db

    def parse_pydantic(self, id, email):
        tc_email_obj = TeacherEmail(id=id, email=email)
        self.db.add(tc_email_obj)
        self.db.commit()

class TeacherPhoneParse:
    def __init__(self, db):
        self.db = db

    def parse_pydantic(self, id, phone):
        tc_phone_obj = TeacherPhoneNumber(id=id, phoneNumber= phone )
        self.db.add(tc_phone_obj)
        self.db.commit()