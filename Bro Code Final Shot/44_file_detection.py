# basic file detection

import os
file_path = "file_handling.txt"

if os.path.exists(file_path):
    print(f"Yes there is file in the locations {file_path}")
    if os.path.isfile(file_path):
        print("yes its a file")
    else:
        print("Its a directory")
else:
    print(f"{file_path} doesn't exists!")
