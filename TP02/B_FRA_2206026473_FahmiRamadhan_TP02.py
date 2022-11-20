"""
Tugas Pemrograman 2 (Simulasi perintah grep)

Format eksekusi program:
python grep.py [options (-w / -i)] [string pattern yang dicari] [nama file / direktori]
"""

import sys
import os

def scan_file(file):
    """Mendapatkan lokasi file serta memindai file baris per baris untuk mendapatkan
    teks dalam baris tersebut dan nomor barisnya."""
    path = os.path.join(os.getcwd(), file)
    location = os.path.relpath(path, root_directory)
    with open(file, "r") as text_file:
        line_number = 0
        for line in text_file:
            line_number += 1
            print_line(location, line_number, line.strip())

def print_line(location, line_number, line):
    """Mencetak lokasi, nomor baris, dan teks dalam baris sesuai dengan ketentuan dari
    command line argumnents yang dimasukkan"""
    if "*" in string_pattern: # Menggunakan wildcard
        left_substring, right_substring = string_pattern.split("*")
        if option == "-w": # Whole word
            if " " + left_substring.strip() in " " + line:
                if right_substring.strip() + " " in line[line.find(left_substring) + len(left_substring):] + " ":
                    print(f"{location:<40}line {line_number:<3} {line[:40]}")
        elif option == "-i": # Case insensitive
            if left_substring.lower() in line.lower():
                if right_substring.lower() in line[line.lower().find(left_substring.lower()) + len(left_substring):].lower():
                    print(f"{location:<40}line {line_number:<3} {line[:40]}")
        else: # Tidak memasukkan option
            if left_substring in line:
                if right_substring in line[line.find(left_substring) + len(left_substring):]:
                    print(f"{location:<40}line {line_number:<3} {line[:40]}")
    else: # Tidak menggunakan wildcard
        if option == "-w": # Whole word
            if " " + string_pattern.strip() + " " in " " + line + " ":
                print(f"{location:<40}line {line_number:<3} {line[:40]}")
        elif option == "-i": # Case insensitive
            if string_pattern.lower() in line.lower():
                print(f"{location:<40}line {line_number:<3} {line[:40]}")
        else: # Tidak memasukkan option
            if string_pattern in line:
                print(f"{location:<40}line {line_number:<3} {line[:40]}")

try:
    print()
    # Mengolah command line arguments yang dimasukkan
    program_arguments = sys.argv[1:]
    if len(program_arguments) == 3: # memasukkan argumen option
        option = program_arguments[0]
        string_pattern = program_arguments[1]
        file_or_dir_rel_path = program_arguments[2]
    elif len(program_arguments) == 2: # tidak memasukkan argumen option
        option = ""
        string_pattern = program_arguments[0]
        file_or_dir_rel_path = program_arguments[1]

    # Memunculkan error jika ketentuan program tidak terpenuhi
    assert len(program_arguments) == 3 or len(program_arguments) == 2
    assert option == "-w" or option == "-i" or option == ""
    assert string_pattern.count("*") <= 1
    root_directory = os.getcwd()
    file_or_dir_abs_path = os.path.join(root_directory, file_or_dir_rel_path)
    if os.path.exists(file_or_dir_abs_path) is False:
        raise FileNotFoundError

    # Mengecek path yang dimasukkan untuk mulai memindai file
    if os.path.isfile(file_or_dir_abs_path): # Path menuju suatu file
        scan_file(file_or_dir_abs_path)
    else: # Path menuju suatu direktori
        for files in os.walk(file_or_dir_abs_path):
            os.chdir(files[0])
            for file in files[2]:
                scan_file(file)

# Mengatasi error
except AssertionError:
    print("Argumen program tidak benar.")
except FileNotFoundError:
    print(f"Path {file_or_dir_rel_path} tidak ditemukan.")
finally:
    print()
