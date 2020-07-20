import subprocess

if __name__ == "__main__":
    #subprocess.call(["ls", "-lha"])
    #subprocess.run('ls', shell=True)
    #output = subprocess.check_output(["ls","-lha"],universal_newlines=True)
    process = subprocess.run('ls -l & uname', shell=True, check=False, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, universal_newlines=True)
    ret = process.returncode
    output = process.stdout
    err = process.stderr
    print(ret)
    print(output)
    print(err)
