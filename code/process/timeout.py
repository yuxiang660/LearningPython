import subprocess
import time

if __name__ == "__main__":
    log_file = 'output.log'
    with open(log_file, 'w') as f:
        try:
            start = time.time()
            subprocess.run('ls & sleep 2', shell=True, timeout=1, check=False, stdout=f,
                                     stderr=f, universal_newlines=True)
        except subprocess.TimeoutExpired as e:
            print(e)
            f.write("Error: Timeout!!!")
        elapsed = time.time() - start
        print(f'run time: {elapsed}')
