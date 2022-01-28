import os
import sys
import subprocess
DIRECTORIES = []
def import_direc(filename):
    """
    Takes in directories from a file and adds them to a list, these directories are absolute paths to a students repo that you want to test
    """
    with open(filename, 'r') as f:
        for line in f:
            DIRECTORIES.append(line.strip())
def copy_tester(file_location):
    """
    Takes in a file location of a TESTING FILE, and will copy that file to the students repo given above
    """
    for directory in DIRECTORIES:
        subprocess.call(["cp", file_location, directory])

def call_tester():
    """
    Takes in a directory, and will run the tester on that directory
    """
    for directory in DIRECTORIES:
        f = open(directory+"/output.txt", "a+")
        subprocess.call(["python3", "test.py", directory],stdout=f)
        f.close()
#import_direc("/Users/matthewrepecki/Desktop/CA Stuff/files.txt") 
#copy_tester("/Users/matthewrepecki/Desktop/CA Stuff/test.py") 
#call_tester() 

def main():
    #a = input("Please enter the directory of where the path.txt file is (Please use absolute Paths if possible) ")
    a= "/Users/matthewrepecki/Desktop/CA Stuff/final-practical/path.txt"
    import_direc(a)
    #b = input("Please enter the directory of where the test.py file is (Please use absolute Paths if possible), also make sure the file is called test.py ")
    #b = "/Users/matthewrepecki/Desktop/CA Stuff/final-practical/test.py"
    #copy_tester(b)
    call_tester()
main()

