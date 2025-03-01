# writing in a file like json, txt, csv
# some commands while writing in a file :
# r - for reading a file
# w - for writing a file(the file should exist)
# x - for writing a file(no need of existence of file, else we will get an error)
# a - to append in a file

txt_data = "I like momos"

file_path = "output_45.txt"



with open(file=file_path, mode="w") as file: #with is a block, and it automatically closes the file if we don't
    file.write(txt_data)
    print(f"Text file '{file_path}' was created!")