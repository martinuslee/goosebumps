import os
import wget 
import math 

## import getFiles

os.system("pwd")


###########################################             fastqc               ###########################################

list = ["SRR390728_1.fastq.gz","SRR390728_2.fastq.gz"]
inputq = []

for i in list:
    mod = i.replace(i, "fastqc "+i)
    inputq.append(mod)
   
    
print(inputq[0], inputq[1])

for item in inputq:
    os.system(item)