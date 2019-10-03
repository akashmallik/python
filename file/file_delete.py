import os

if os.path.exists("blank.txt"):
    os.remove("blank.txt")
else:
    print("The file does not exist")

if os.path.exists("temp"):
    os.rmdir("temp")
else:
    print("The directory does not exist")