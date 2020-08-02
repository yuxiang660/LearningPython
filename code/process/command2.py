import subprocess
import time
import os
import logging
import logging.config
import signal
import psutil

logging.config.fileConfig('config.ini')


class Command:
    def __init__(self, cmd, log_file):
        self._cmd = cmd
        self._log_file = log_file

        logging.info(f"Start CMD: '{self._cmd}'")
        self._start = time.time()
        with open(self._log_file, 'w') as f:
            self._proc = subprocess.Popen(self._cmd,
                                      shell=True,
                                      universal_newlines=True,
                                      stdout=f,
                                      stderr=f)

    def communicate(self, timeout_s=None):
        with open(self._log_file, 'a') as f:
            try:
               self._proc.communicate(None, timeout_s)
            except subprocess.TimeoutExpired as e:
                self.kill()
                #self._proc.kill()
                logging.error(e.__str__())
                f.write(f'Error: {e.__str__()}')
                return -1
            else:
                elapsed = time.time() - self._start
                f.write("End command '{}' with {:.3f} seconds.".format(self._cmd, elapsed))
        logging.info(f'End CMD: {self._cmd}')
        return elapsed

    def kill(self):
        process = psutil.Process(self._proc.pid)

        with open(self._log_file, 'a') as f:
            for child in process.children(recursive=True):
                kill_log = f">>> Kill command '{self._cmd}' child process '{child.pid}' - '{child.name()}' <<<"
                f.write(kill_log + '\n')
                logging.info(kill_log)
                child.kill()

            kill_log = f">>> Kill command '{self._cmd}' process '{process.pid}' - '{process.name()}' <<<"
            f.write(kill_log + '\n')
            logging.info(kill_log)
            process.kill()

if __name__ == "__main__":
    logfile = 'output/command2.log'
    os.makedirs(os.path.dirname(logfile), exist_ok=True)
    cmd = Command('echo "start!!" && sleep 10 && echo "end!!"', logfile)
    #cmd.communicate(2)
    try:
        time.sleep(1)
        raise Exception('spam', 'eggs')
    except:
        print('catch exception')
        cmd.kill()
