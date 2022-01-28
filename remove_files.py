#Author: Matthew Repecki
import os
import shutil
STUDENTS = {"JDMsofteng":"Mendes","Mercedess03":"Mercedes","DattCMohan":"Mohan","eam5863":"Morgan","DionteRules72":"Murphy-Ayers","sco5782":"Orlando","lukepicciano":"Picciano","lailaporter55":"Porter","christiansantiago213":"Santiago","hs9166":"Santos","nxsaunders":"Saunders","ds6953":"Silberman","PhilipSoto":"Soto","hz5816":"Zheng"}
def remove_files(file_directory,names,assignment_name,split):
    os.chdir(file_directory)
    files = os.listdir()
    #print(files)
    for i in range(len(files)):
        a = files[i].split("-")
        try:
            if(a[split] in names):
                name = str(a[split])
                if (name in STUDENTS):
                    path = assignment_name + "-" + str(a[split])
                    new_path = assignment_name + "-" + str(STUDENTS[name])
                    os.rename(path,new_path)
                    print("Renaming " + name + " to " + STUDENTS[name])
                print("include")
            else:
                #print("removing file")
                path = assignment_name + "-" + str(a[split])
                #print(path)
                #print("removed file" + path)
                shutil.rmtree(path)
        except:
            #print("invalid file" + str(a))
            #print("got an error")
            pass
    
def main():
    directory = input("Please enter directory: ")
    assignment = input("Please enter assignment name: ")
    names = ["JDMsofteng","Mercedess03","DattCMohan","eam5863","DionteRules72","sco5782","lukepicciano","lailaporter55","christiansantiago213","hs9166","ds6953","nxsaunders","PhilipSoto","Natnail101","hz5816"] #Enter Students github usernames seperated by commas, ex "mrr5298","matthew2848123",...
    names += ["Andrew6rant","MaraH980","alecjones0321","vuduchild14125","RuhangLiu","NoahMarini","mgm1785"] #Add Herrings Section Here to easily remove later
    #Still need - McMaster,Ryan [Moreland, Marcos, mdm8635]
    #Missing Herrings' Tryder
    split = 2#Where the names are located
    remove_files(directory,names,assignment,split)
    
main()
