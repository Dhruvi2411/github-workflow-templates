import os

f1 = open('newfile.txt', 'w+')
f1.write("Hello, I'm from the python file............")
f1.close()

file_path = os.getcwd()
print(file_path)

for folder, sub_folders, files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print("The subfolders are:")
    
    for i in sub_folders:
        print(f"Subfolder: {i}")
        
    print("\n")
    print("The files are:")
    for i in files:
        print(f"File: {i}")
    print("\n")
