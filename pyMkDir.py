import os
userDirectory = input("Enter a directory: ")
for directory in userDirectory.split(" "):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print("Directory already exists: ", directory)
