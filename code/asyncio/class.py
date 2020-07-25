import asyncio

class Hello:
    async def say(self, what, when):
        await asyncio.sleep(when)
        print(what)

    async def tasks(self, loop):
        tasks = []
        tasks.append(loop.create_task(self.say('first hello', 2)))
        tasks.append(loop.create_task(self.say('second hello', 1)))
        await asyncio.wait(tasks)

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.tasks(loop))
        loop.close()

if __name__ == "__main__":
    h = Hello()
    h.run()
