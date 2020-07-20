import os

if __name__ == "__main__":
    filename = 'write-read.log'
    with open(filename, 'w') as f:
        f.write('Hello')
        print("World", file=f)

    with open(filename, 'r') as f:
        text = f.read(3)
        print(len(text))
        print(text)
        text_next = f.read()
        print(len(text_next))
        print(text_next)
        
