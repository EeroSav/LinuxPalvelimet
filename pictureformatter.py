import os
import re

picture_files = os.listdir("Pictures")
mddir = "."

print(picture_files)

for filename in os.listdir(mddir):
    if filename.endswith(".md"):
        md_files = os.path.join(mddir, filename)
        print(md_files)

    #Read the file
    with open(md_files, "r") as f:
        contents = f.read()

    #find all the pictures with regex
    pattern = r"!\[.*\]\((.*)\)"
    pictures = re.findall(pattern, contents)
    print(pictures)
