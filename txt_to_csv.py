import os;
import csv

path = os.getcwd();
input_format ='txt';
output_format='csv';
lines = [];
header = ['*', '*', '*', '*'];

def process_line(line):
    for line_split in line.split(';'):
        splitted = line_split.replace(',-', '').split(',') 
        if splitted != ['']:
            lines.append(splitted);

def read_file(file):
    with open(file) as to_convert:
        for line in to_convert.readlines():
            process_line(line.rstrip('\n'));

def get_directory_files():
    files = os.listdir(path) 
    return files;      

def get_file_extension(file):
    if len(file.split('.')) > 1:
        return file.split('.')[1]
    return '';

def write_file(file):
    with open(file, 'a', newline='\n') as csvfile:
        writer = csv.writer(csvfile);
        writer.writerow(header);
        writer.writerows(lines)

def convert_to_csv(files):
    for file in files:
        file_extension = get_file_extension(file)
        if os.path.isfile(file) and input_format in file_extension :
            read_file(file);
            new_file = f'{path}/{file.split(".")[0]}.{output_format}'
            write_file(new_file);

def main():
    convert_to_csv(get_directory_files());
    
main();
