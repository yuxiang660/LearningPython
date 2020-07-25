import asyncio
import subprocess

async def run_cmd(when):
    print(f'Start sleep {when}')
    cmd = f'sleep {when}'
    subprocess.run(cmd, shell=True, check=False, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f'End sleep {when}')

async def say(what, when):
    await asyncio.sleep(when)
    print(what)

async def tasks(loop):
    tasks = []
    tasks.append(loop.create_task(run_cmd(2)))
    tasks.append(loop.create_task(run_cmd(1)))
    await asyncio.wait(tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(tasks(loop))
loop.close()

# run_cmd(1)
# run_cmd(2)
