

class Parser:
    def __init__(self, db, schema):
        self.db = db
        self.schema = schema

    def parse(self, pydantic_obj):
        sql_obj = self.schema(**pydantic_obj)