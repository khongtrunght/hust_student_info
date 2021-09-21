from hust_student import schemas
from hust_student.models import RootUnit
from hust_student.schemas import RootUnitDB


class RootUnitParse:
    def __init__(self, db):
        self.db = db

    def parse_pydantic(self, r_unit: schemas.RootUnit):
        if r_unit:
            if not self.db.query(RootUnit).filter(RootUnit.id==r_unit.id).first():
                root_unit = RootUnitDB.parse_obj(r_unit)
                db_obj = RootUnit(**root_unit.dict())
                self.db.add(db_obj)
                self.db.commit()