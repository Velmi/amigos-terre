import os
import shutil
import sys
import platform

def copy_file(source, destination, extension):
    extension = '.' + extension
    got_extension = os.path.splitext(source)
    if got_extension[1] == extension:
        print("Copying file to " + destination)
        shutil.copy2(source, destination)

def copy_files_extension(extension, source, destination):
    for path in os.listdir(source):
        copy_file(path, destination, extension)
    
    print("\nOK\n")

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Give extension")
        print("Press any key to exit...")
        input()
        exit()

    source_path = os.getcwd()
    extension = sys.argv[1]

    destination_path = os.getcwd()
    destination_path = os.path.join(destination_path, extension)

    if os.path.isdir(destination_path):
        print("Directory already exists")
        print("Press any key to exit...")
        input()
        exit()
    
    os.mkdir(destination_path, 0o777)

    print(platform.system())
    print("Destination path: " + destination_path)
    copy_files_extension(extension, os.getcwd(), destination_path)
    print("Press any key to exit...")
    input()
