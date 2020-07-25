from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import subprocess

def spider(page):
    print(f'start spider {page}')
    time.sleep(page)
    print(f'crawl task{page} finish')
    return page

def run_cmd(when):
    print(f'Start sleep {when}')
    cmd = f'sleep {when}'
    subprocess.run(cmd, shell=True, check=False, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f'End sleep {when}')
    return when

with ThreadPoolExecutor(max_workers=5) as t:
    tasks = []
    for when in range(0, 5):
        tasks.append(t.submit(run_cmd, 5 - when))

    for future in as_completed(tasks):
        r_time = future.result()
        print(f">>finish sleep {r_time}")
        time.sleep(r_time)
        print(f">>sleep {r_time}")
