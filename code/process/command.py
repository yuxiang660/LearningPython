import subprocess
import time
import os

class Command:
    def __init__(self, cmd, log_file):
        self._cmd = cmd
        self._log_file = log_file
        self._elapsed = 0

    def run(self, timeout_s=None):
        print('Start CMD:', self._cmd)
        start = time.time()
        with open(self._log_file, 'w') as f:
            try:
                subprocess.run(self._cmd,
                               shell=True,
                               check=False,
                               universal_newlines=True,
                               timeout=timeout_s,
                               stdout=f,
                               stderr=f)
            except subprocess.TimeoutExpired as e:
                print(e)
                f.write('Error: Timeout!!!')
            else:
                self._elapsed = time.time() - start
                f.write('End with runtime: {:.3f} seconds.'.format(self._elapsed))
        print('End CMD:', self._cmd)

    def print_log(self):
        print(f'The log of CMD "{self._cmd}":')
        if os.path.exists(self._log_file):
            with open(self._log_file, 'r') as f:
                print(f.read())

if __name__ == "__main__":
    cmd = Command('ls & sleep 1', 'output.log')
    #cmd.run(1)
    cmd.print_log()
