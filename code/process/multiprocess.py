import multiprocessing
import time

def worker(num):
    """worker function"""
    print('Worker', num)
    return

def timeout_worker():
    time.sleep(2)
    print('Timout worker')

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
    print('working')
    for job in jobs:
        job.join()
    print('ending')

    p2 = multiprocessing.Process(target=timeout_worker)
    p2.start()
    p2.join(1)
    print('p.is_alive()', p2.is_alive())
