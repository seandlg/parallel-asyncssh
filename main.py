import asyncio
from subprocess import CompletedProcess
import traceback
import asyncssh

async def executeCommand(cmd: str) -> CompletedProcess:
    try:
        async with asyncssh.connect(
            host="10.10.10.10",
            config=None,
            username="root",
            known_hosts=None,
            password="secret",
            request_pty=True,
        ) as conn:
            print(f"Asynchronous SSH connection established.. Executing command: {cmd}")
            ans = await conn.run(cmd, check=False)
            return ans
    except:
        print("Error trying to connect to server via SSH...")
        traceback.print_exc()
        return None

async def ls():
    tasks = []
    parallel_tasks = 20
    for i in range(parallel_tasks):
        tasks.append(asyncio.create_task(executeCommand(f"ls #{i}")))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(ls())