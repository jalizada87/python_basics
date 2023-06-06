import os

current_dir = os.getcwd()
print(current_dir)

list_directory = os.listdir(current_dir)
print(' '.join(list_directory))


for i in list_directory:
    file_size = os.path.getsize(i)
    file_name = os.path.basename(i)
    print(f"name: {file_name}, size: {file_size} byte")