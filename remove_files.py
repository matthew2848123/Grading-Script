import os
import shutil
def remove_files(file_directory,names,assignment_name):
    os.chdir(file_directory)
    files = os.listdir()
    for i in range(len(files)):
        a = files[i].split("-")
        try:
            if(a[3] in names):
                print("include")
            else:
                path = assignment_name + "-" + str(a[3])
                print(path)
                shutil.rmtree(path)
        except:
            #print("invalid file" + str(a))
            pass
    
def main():
    directory = input("Please enter directory: ")
    assignment = input("Please enter assignment name: ")
    names = [] #Enter Students github usernames seperated by commas, ex "mrr5298","matthew2848123",...
    remove_files(directory,names,assignment)
main()
