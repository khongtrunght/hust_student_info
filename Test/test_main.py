import asyncio

from hust_student.rate_limit_send import rate_limit_student


def test_run():

    URL_LIMIT = 100

    urls = [
        f'http://v1-dot-hust-edu.appspot.com/api/profile/student?sessionId=2B9D9020-9F8C-49F6-8DA4-7C8607593244-1631971109951_1631971109951&token=PLpt91USzRlluCq2duoZ-V2&studentId={n}'
        for n in range(20193300, 20193300+ URL_LIMIT)
    ]

    LIMIT = 30
    RATE = 1

    asyncio.run(
        rate_limit_student(
            urls= urls,
            rate = RATE,
            limit= LIMIT
        )
    )


test_run()