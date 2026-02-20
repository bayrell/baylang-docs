#!/usr/bin/env python3
import os

def list_files_recursively(directory):
    result = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            result.append(os.path.join(root, file))
    return result

def create_document(folder="en"):
    files = list_files_recursively(folder)
    
    output_file = "baylang_" + folder + ".md"
    print(output_file)
    with open(output_file, "w", encoding="utf-8") as outfile:
        for filename in files:
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as file:
                    outfile.write(f"# File: {filename}\n\n")
                    outfile.write(file.read())
                    outfile.write("\n\n")

create_document("en")
create_document("ru")