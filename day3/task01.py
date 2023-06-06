import os
from pathlib import Path

current_directory = os.getcwd()
print("Current directory:", current_directory)

home_directory = str(Path.home())

os.chdir(home_directory)


files = os.listdir()
for file in files:
    print(file)