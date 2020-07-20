import os
import os.path
import glob

if __name__ == "__main__":
    pyfiles = [name for name in os.listdir('.')]
    print(pyfiles)
    pyfilenames = glob.glob('./**/*.py', recursive=True)
    print(pyfilenames)
