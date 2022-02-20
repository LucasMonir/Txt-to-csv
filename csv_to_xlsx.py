from inspect import getfile
from linecache import getline
import os
import openpyxl
import csv

path = os.getcwd()
input_format = "csv"
output_format = "xlsx"
header = ["*", "*", "*", "*"]
csv_list = []

def get_directory_files():
    files = os.listdir(path)
    return files

def read_lines(file):
    with open(file) as to_convert:
        reader = csv.reader(to_convert)
        for row in reader:
            if len(row) > 1 and row[0] != "*":
                csv_list.append(row)


def csv_to_xlsx(file):
    csv_list.append(header)
    read_lines(file)

    result = openpyxl.Workbook()
    sheet = result.active

    for row in csv_list:
        sheet.append(row)

    new_file = f'{path}/{file.split(".")[0]}.{output_format}'
    result.save(new_file)
    print("File saved: " + file.split(".")[0] + ".xlsx")


def get_file_extension(file):
    if len(file.split(".")) > 1:
        return file.split(".")[1]
    return ""


def convert_to_xlsx():
    for file in get_directory_files():
        file_extension = get_file_extension(file)
        if os.path.isfile(file) and input_format in file_extension:
            csv_to_xlsx(file)


def main():
    convert_to_xlsx()


main()
