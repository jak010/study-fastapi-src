import queue
import asyncio


class SessionQueue:

    def __init__(self):
        # self.queue = queue.Queue()
        self.queue = asyncio.Queue()

    async def add(self, session):
        print(f"ADD[SESSION]:{session}")
        await self.queue.put(session)

    async def get(self):
        s = await self.queue.get()
        print(f"GET[SESSION]:{s}")

        return s
