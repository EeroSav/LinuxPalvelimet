import os
import re

picture_files = os.listdir("Pictures")
mddir = "."

for filename in os.listdir(mddir):
    if filename.endswith(".py"):
        break

    if filename.endswith(".md"):
        md_files = os.path.join(mddir, filename)
        pic1 = filename[:-3]
    

    #Read the file
    with open(md_files, "r") as f:
        contents = f.read()

    #find all the pictures with regex
    pattern = r"!\[.*\]\((.*)\)"
    pictures = re.findall(pattern, contents)

    # Loop through picures and rename them
    for picture in pictures:
        picname = pic1 + "_" + str(pictures.index(picture)+1)
        old_name = picture
        new_name = "Pictures/" + f"{picname}.png"
        if (old_name != new_name):
            print("in file: " + filename + ", old name: " + old_name)
            print("new name: " + new_name)

            os.rename(old_name, new_name)
            contents = contents.replace(picture, new_name)
            
