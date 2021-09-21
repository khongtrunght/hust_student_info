import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.post('http://v1-dot-hust-edu.appspot.com/api/profile/student?sessionId=2B9D9020-9F8C-49F6-8DA4-7C8607593244-1631971109951_1631971109951&token=PLpt91USzRlluCq2duoZ-V2&studentId=20194465') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())