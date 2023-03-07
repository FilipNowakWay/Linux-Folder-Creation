import subprocess
import os

amount_of_folders = int(input("Hello, how many folders do you want? "))
print("What format would you like, ex: ")
print("1: Project 1, Project 2          (One name of folder and just increases the number of folder)")
print("2: customName, CustomName2...    (Asks for name for every folder)")
folder_format = int(input())

if folder_format == 1:
    # Get folder name and location from user
    folder_name = input("What folder name would you like to use? ")
    folder_location = input("Where should the folders be created? ")

    # Change the current working directory to the specified location
    os.chdir(folder_location)

    # Check if folder name contains any invalid characters
    if any(c in folder_name for c in '/\\'):
        print("Invalid folder name")
        exit()

    # Create the folders
    for i in range(1, amount_of_folders + 1):
        subprocess.check_output(['mkdir', f'{folder_name} {i}'], cwd=folder_location)

else:
    folder_location = input("Where should the folders be created? ")

    # Change the current working directory to the specified location
    os.chdir(folder_location)

    # Get folder names from user
    folder_names = input("What would you like to name the folders? (add space for every name)").split()

    # Check if folder names contain any invalid characters
    if any(any(c in name for c in '/\\') for name in folder_names):
        print("Invalid folder name")
        exit()

    # Create the folders
    for name in folder_names:
        subprocess.check_output(['mkdir', name], cwd=folder_location)
