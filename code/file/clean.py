import os

def clean(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("The file does not exist")

if __name__ == "__main__":
    filenames = ['write-read.log']
    for filename in filenames:
        clean(filename)
