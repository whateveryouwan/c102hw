import os
import shutil

from_dir='C:/Users/vanap/Downloads'
to_dir='C:/Users/vanap/Desktop/document_files'

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name, extension = os.path.splitext(file)
    print(f'Name: {name}, Extension: {extension}')
    if extension=='':
        continue
    elif extension.lower() in ['.pdf', '.docx', '.xlsx']:
        path1 = os.path.join(from_dir, file)
        path2 = os.path.join(to_dir, file)
        path3 = os.path.join(to_dir, f'{name}_converted{extension}')

        if os.path.exists(path2):
            print(f'moving {file} to {to_dir}')
            shutil.move(path1, to_dir)
        else:
            os.makedirs(to_dir, exist_ok=True)  
            shutil.move(path1, path3)
            