import multiprocessing

def worker(num):
    """worker function"""
    print('Worker', num)
    return

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