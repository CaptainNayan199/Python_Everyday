# reading from a file (txt, json, csv)
import os
import json
import csv
file_path = "output_45.txt"
file_path2 = "output_45.json"
file_path3 = "output_45.csv"
# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("The currently mentioned file was not found!")
# try:
#     with open(file_path2, "r") as file:
#         content = json.load(file)
#         print(content["age"])
#         for key,value in content.items():
#             print(f"{key} : {value}")
# except FileNotFoundError:
#     print("The currently mentioned file was not found!")
try:
    with open(file_path3, "r") as file:
        content = csv.reader(file)
        for line in content:
            # print(line)
            print(line[0], "\t\t", line[1], "\t\t", line[2], "\t\t", line[3], "\t\t", line[4])
        # print(content)
except FileNotFoundError:
    print("The currently mentioned file was not found!")