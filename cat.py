'''
This program prints stdin to the screen.
'''
import sys

CHUNK_SIZE = 65536

def cat(file, out):
    while True:
        data = file.read(CHUNK_SIZE)
        if not data:
            break
        out.write(data)

if __name__ == "__main__":
    out = sys.stdout.buffer
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "rb") as f:
                cat(f, out)
    else:
        cat(sys.stdin.buffer, out)
