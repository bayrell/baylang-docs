#!/usr/bin/env python3
import os

def list_files_recursively(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            result.append(os.path.join(root, file))
    return result

def create_document(folder, file_name):
    
    output_file = file_name + ".rule"
    print(output_file)
    
    with open(output_file, "w", encoding="utf-8") as outfile:
        for item in folder:
            files = list_files_recursively(item)
            for name in files:
                if os.path.exists(name):
                    with open(name, "r", encoding="utf-8") as file:
                        outfile.write(file.read())
                        outfile.write("\n\n")

create_document(["en/baylang"], "baylang_syntax")
