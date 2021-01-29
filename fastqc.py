import sys
import os
import math 
import getFiles
###########################################             fastqc               ###########################################


            
def getQC(files, dir):

    mkdir = dir + "FASTQC_Results"
    try: 
        os.makedirs(mkdir)
        name = '.fastq.gz'
        getFiles.isFiles(files, dir, name)
        #print(files)
        print("\n Start FASTQC : ")
        print("---------------------\n")
        os.system("fastqc -o "+ mkdir+ " " + files[0]+ " " +files[1])
        print("\nFinished FASTQC : ")
        print("---------------------\n")
            
    except FileExistsError:
        # dir already exists..
        os.system("rm -d " +mkdir)
        print("FASTQC cd dir already exists..\nPlease Try it again..\n")