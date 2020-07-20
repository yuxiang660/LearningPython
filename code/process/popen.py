import subprocess
from subprocess import Popen

if __name__ == "__main__":
    #p = Popen(['ls', '-lha'])
    #p.wait()

    log_file = 'output.log'
    with open(log_file, 'w') as f:
        p = Popen(["ls","-lha"], stdout=f, stderr=subprocess.PIPE, universal_newlines=True)
        output, errors = p.communicate()
    
    print(output)
    print(errors)
