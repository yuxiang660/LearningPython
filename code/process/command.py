import subprocess
import time
import os
import logging
import logging.config

logging.config.fileConfig('config.ini')

class Command:
    def __init__(self, cmd, log_file):
        self._cmd = cmd
        self._log_file = log_file

    def run(self, timeout_s=None):
        logging.info(f"Start CMD: '{self._cmd}'")
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
                logging.error(e.__str__())
                f.write(f'Error: {e.__str__()}')
            else:
                elapsed = time.time() - start
                f.write("End command '{}' with {:.3f} seconds.".format(self._cmd, elapsed))
        logging.info(f'End CMD: {self._cmd}')
        return elapsed

    def print_cmd_log(self):
        logging.info(f'The log of CMD "{self._cmd}":')
        if os.path.exists(self._log_file):
            with open(self._log_file, 'r') as f:
                print(f.read())

if __name__ == "__main__":
    logfile = 'output/command.log'
    os.makedirs(os.path.dirname(logfile), exist_ok=True)
    cmd = Command('ls & sleep 1', 'output/command.log')
    time1 = cmd.run(3)
    print(f'The command runs {time1}s')
    cmd.print_cmd_log()
