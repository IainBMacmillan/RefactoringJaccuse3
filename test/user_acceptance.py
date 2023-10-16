from source.jaccuse_original_test import jaccuse_game
import sys


class MyWriter:

    def __init__(self, stdout, filename):
        self.stdout = stdout
        self.logfile = open(filename, 'w')

    def write(self, text):
        self.stdout.write(text)
        self.logfile.write(text)

    def close(self):
        self.stdout.close()
        self.logfile.close()

    def flush(self):
        ...


"""  use this to run tests to files
path = folder and filename
with open(path, 'w') as f:
    with contextlib.redirect_stdout(f):
        print('Hello, World')
"""

def main() -> None:
    writer = MyWriter(sys.stdout,'approval_results/user_test_3.txt')
    sys.stdout = writer

    jaccuse_game()


if __name__ == '__main__':
    main()
