import os
import wget 
import math 
import getFiles
###########################################             fastqc               ###########################################


            
def getQC(files, dir):
    try: 
        mkdir = dir + "FASTQC_Results"
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
        #os.system("rm -r " +mkdir)
        print("FASTQC cd dir already exists..\n")
        pass