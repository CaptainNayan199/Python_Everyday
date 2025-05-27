# writing in a file like json, txt, csv
# some commands while writing in a file :
# r - for reading a file
# w - for writing a file(the file should exist)
# x - for writing a file(no need of existence of file, else we will get an error)
# a - to append in a file

import json
import csv
from operator import index

txt_data = "This file will be now created on user desktop"

file_path = "output_45.csv"

emp = ["Eugene", "Squidward", "Patrick" , "Spongebob"]

json_data = {

    "name" : "Nayan",
    "age" : 22,
    "Job": "Student",
    "isMarried" : False,
    "isHappy" : True,
    "Hobbies" : "Singing"
}

employees = [["Name", "Age", "Job", "Salary", "Address"],
             ["Nayan", 22, "Pilot", "150000", "Nepal"],
             ["Sita", 22, "Coder", "200000", "Charali"] ,
             ["Sitoshna", 22, "ML Engineer", "400000", "Birtamode"]]

#
# try:
#     with open(file=file_path, mode="w") as file: #with is a block, and it automatically closes the file if we don't
#         # for e in emp:
#         #     file.write(e+"\t")
#         for key,value in json_data.items():
#             file.write(f"{key} : {value}"+"\n")
#         print(f"Text file '{file_path}' was created!")
# except FileExistsError:
#     print("File is already there! And you cannot use 'x' mode to open an file that is already created!")
#
# finally:
#     print("Dudh Bhaat!")

with open(file_path, "w", newline="") as file:
    # json.dump(json_data, file, indent=4)
    writer = csv.writer(file)
    for emp in employees:
        writer.writerow(emp)
    print("csv file created")
