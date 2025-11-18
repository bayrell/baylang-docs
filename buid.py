import os

files = [
    "index.md",
    "baylang/about.md",
    "baylang/install.md",
    "baylang/map.md",
    "baylang/model.md",
    "baylang/project.md",
    "baylang/string.md",
    "baylang/syntax.md",
    "baylang/template.md",
    "baylang/vector.md",
    "cloud-os/about.md",
    "cloud-os/install-desktop.md",
    "cloud-os/install-server.md",
    "cloud-os/templates.md",
    "constructor/about.md",
    "framework/about.md",
]

output_file = "baylang.md"
with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in files:
        if os.path.exists("ru/" + filename):
            with open("ru/" + filename, "r", encoding="utf-8") as file:
                outfile.write(f"# Содержимое файла: {filename}\n\n") 
                outfile.write(file.read())
                outfile.write("\n\n")
