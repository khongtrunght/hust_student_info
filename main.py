import asyncio

from hust_student.database import Base, engine, SessionLocal
import requests
from hust_student.rate_limit_send import rate_limit_student, rate_limit_class
from hust_student.models import Student, StudentEmail, Class

db = SessionLocal()

def crawl_student(start, end, rate, limit):
    urls = [
        f'http://v1-dot-hust-edu.appspot.com/api/profile/student?sessionId=2B9D9020-9F8C-49F6-8DA4-7C8607593244-1631971109951_1631971109951&token=PLpt91USzRlluCq2duoZ-V2&studentId={n}'
        for n in range(start, end)
    ]

    LIMIT = limit
    RATE = rate

    asyncio.run(
        rate_limit_student(
            urls=urls,
            rate=RATE,
            limit=LIMIT
        )
    )

def crawl_class(rate, limit):
    class_id = db.query(Student.classId).distinct()
    id_list = [a[0] for a in class_id.all()]
    # id_list = [5980566734241792, 6052251550351360]
    # id_list = id_list[:10]
    urls = [
        f"http://v1-dot-hust-edu.appspot.com/api/student-class?sessionId=2B9D9020-9F8C-49F6-8DA4-7C8607593244-1631971109951_1631971109951&token=PLpt91USzRlluCq2duoZ-V2&classId={n}"
        for n in id_list
    ]



    LIMIT = limit
    RATE = rate

    asyncio.run(
        rate_limit_class(
            urls=urls,
            rate=RATE,
            limit=LIMIT
        )
    )

# crawl(20210000,20219999, 0.5, 100)

# print(std.fullName)
# print(ema[-1].email)

crawl_class(rate=0.5, limit=50)