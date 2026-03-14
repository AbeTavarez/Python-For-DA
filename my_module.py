# import math

# print(math.pow(2,2))

# print(math.pi)

import os
import sys
from math import pi, pow

# import pandas as pd

# ========== Math Module ============
print(pi)

result = pow(2, 2)
print("Result: ", result)

# ========== OS Module ============
print(os.name)  # os name

print(os.getcwd())  # current directory

# create a new directory or folder
# os.mkdir('./sample_dir')

# Delete a file
# os.remove('./test.txt')

# Delete a directory
# os.removedirs('sample_dir')

# Rename a file or directory
# os.rename('hello.py', 'hello_python.py')


print(os.listdir())  # list all files and directories

# Environment variables
print(os.environ["home"])


# =============== SYS Module ====================
print(sys.argv)
print(sys.executable)
print(sys.path)
print(sys.version)
print(sys.platform)
# print('\n', sys.modules)


# =============== __name__ ====================
def test(message):
    print(
        f"""{message}
          {__name__}""")
    

if __name__ == "__main__":
    test("Running from the main file")
