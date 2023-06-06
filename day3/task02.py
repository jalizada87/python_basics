import os

current_dir = os.getcwd()
print(current_dir)

file_size = os.path.getsize(current_dir)
print(file_size)