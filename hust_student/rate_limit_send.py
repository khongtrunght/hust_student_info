import asyncio
import logging

import aiohttp
import attr

from hust_student.database import Base, engine, SessionLocal
from hust_student.models import Student, StudentEmail
from sqlalchemy.future import select

from hust_student.parse_model.class_parse import ClassParse
from hust_student.schemas import ClassResp

LOGGER_FORMAT = '%(asctime)s %(message)s'
logging.basicConfig(format=LOGGER_FORMAT, datefmt='[%H:%M:%S]')
log = logging.getLogger()
log.setLevel(logging.INFO)

db = SessionLocal()
Base.metadata.create_all(engine)

@attr.s
class Fetch:
    limit = attr.ib()  # batch
    rate = attr.ib(default=5, converter=int)  # speed

    async def make_request(self, url):

        EXCLUDE = {'semesters', 'trainings', 'staffAwards', 'relatives', 'allEmails'}
        obj_lst = []
        async with self.limit:
            async with aiohttp.ClientSession() as session:
                async with session.request(method='POST', url=url) as response:
                            mssv = url[-8:]
                            json = await response.json()
                            status = response.status
                            obj = json['data']
                            try :
                                stud = db.query(Student).filter(Student.id == obj['id']).first()
                                if not stud:
                                    test_obj = Student(**{k: v for k, v in obj.items() if k not in EXCLUDE})
                                    obj_lst.append(test_obj)
                                    # db.add(test_obj)
                                    for email in obj['allEmails']:
                                        e_obj = StudentEmail(id=obj['id'], email=email)
                                        obj_lst.append(e_obj)
                                        # db.add(e_obj)

                                # std = await db.execute(select(Student).filter(Student.studentId == obj['studentId']))
                                log.info(f"Mssv: {mssv}. Name: {obj['fullName']}. Status: {status}. Obj: ")
                            except Exception as e :
                                log.error(f"Mssv: {mssv}. Status: Fail {e}")
                            await asyncio.sleep(self.rate)
        return obj_lst

    async def make_request_new(self, url):

        async with self.limit:
            async with aiohttp.ClientSession() as session:
                async with session.request(method='GET', url=url) as response:
                    js = await response.json()
                    try :
                        ten_lop = js['data']['name']
                        log.info(f"Lop : {ten_lop} thanh cong")
                    except:
                        log.error(f"url {url} fail")
                        # return {'data': '',}
                    await asyncio.sleep(self.rate)
        return js






async def rate_limit_student(urls, rate, limit):
    limit = asyncio.Semaphore(limit)

    f = Fetch(
        rate=rate,
        limit=limit,
    )

    tasks = []

    for url in urls:
        tasks.append(f.make_request(url=url))

    results = await asyncio.gather(*tasks)

    list_to_commit = sum(results, [])
    db.add_all(list_to_commit)
    db.commit()


async def rate_limit_class(urls, rate, limit):
    limit = asyncio.Semaphore(limit)

    f = Fetch(
        rate=rate,
        limit=limit,
    )

    tasks = []

    for url in urls:
        tasks.append(f.make_request_new(url=url))

    class_parser = ClassParse(db)

    results = await asyncio.gather(*tasks)

    for json in results:
        if json:
            try:
                class_parser.parse_pydantic(ClassResp.parse_obj(json).data)
            except:
                log.error(f"json loi {json}")





