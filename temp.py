from Bio import SeqIO
import sys 
import re
import os
import getopt
import wget 
import math 
import gzip
import getFiles
import fastqc
import getopt

##############################################     Input Variables to Download Files    ###########################################
checkFiles = input("--- Do you want to download ref files [Y/n]$ ")

#import countReads

##############################################     Download files using functions    ###########################################
class DownloadError(Exception):
    def __str__(self):
        return "FASTA File Download Error...!"
class QCError(Exception):
    def __str__(self):
        return "FASTQC Error...!"        

if(checkFiles == 'Y' or checkFiles == 'y'):

    print("Please Input options for Download Files, Trimmomatics, FastQC, STAR, and FeatureCount")
    
    #### for download files options
    release = input("Please Input Release Version (i.e. 102)$ ")
    species = input("Please Input Species (i.e. homo_sapiens)$ ")
    Species = species.capitalize() #Homo_sapiens
    refID = input("Please Input reference id (i.e. GRCh38)$ ")
    PATH = input("Please Input Download Path$ ")
    dot = "."
    slash ="/"
    p_a = "ftp://ftp.ensembl.org/pub/release-"+release+"/fasta/"+species+"/dna/"+Species+ dot + refID + dot + "dna.primary_assembly.fa.gz"
    ensembl = "ftp://ftp.ensembl.org/pub/release-"+release+"/gtf/"+species+ slash +Species+ dot + refID +dot + release + ".gtf.gz"

    link = [p_a,ensembl]
    print(input)
    input = link
    #### for trimmomatic options
    filename_forward = "/disk11/3.Pipeline_test_ljh/SRR390728_1.fastq.gz"
    filename_reverse = "/disk11/3.Pipeline_test_ljh/SRR390728_2.fastq.gz"

    # Compiler and path tool
    ja = " java -jar"
    tool = " /program/Trimmomatic/trimmomatic-0.39.jar"
    s = " "

    # Outputs paired end
    output_forward_paired = PATH + "output_forward_paired_SRR390728_1.fastq.gz"
    output_forward_unpaired = PATH + "output_forward_unpaired_SRR390728_1.fastq.gz"
    output_reverse_paired = PATH + "output_reverse_paired_SRR390728_2.fastq.gz"
    output_reverse_unpaired = PATH + "output_reverse_unpaired_SRR390728_2.fastq.gz"
    print("Start Trimmonatics :")
    print("--------------------")
    attribute = "PE -threads 12 -phred33 "
    #illuminaclip_adapters = "ILLUMINACLIP:/program/Trimmomatic/adapters/TruSeq3-PE.fa:2:30:10"
    illuminaclip_adapters = "ILLUMINACLIP:/program/Trimmomatic/adapters/TruSeq3-PE.fa:2:30:10"
    illuminaclip_Attribute = "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"
    
    
    ### LET's get started
    try:
        for i in input:
            print("start : " + i)
            getFiles.download(i,PATH)
            getFiles.unzipfiles(PATH)          
            print("completed : " + i)
            
        fastqc.getQC(PATH)
        print("Start Trimmonatics :")
        print("--------------------")


        cmd1 = s + ja + s + tool + s + attribute + s + filename_forward + s + filename_reverse + s + output_forward_paired + s + output_forward_unpaired
        cmd2 = s + output_reverse_paired + s + output_reverse_unpaired + s + illuminaclip_adapters + s + illuminaclip_Attribute

        cmd = cmd1 + cmd2

        os.system(cmd)
        
    except DownloadError as e:
        print(e) 
    except QCError as e:
        print(e)
        
    sys.exit()
    
else:
    pass
    
    
##############################################     FASTQC      #######################################################


checkQC = input("Do you want to build FastQC [Y/n]$ ")
if(checkQC == 'Y' or checkQC == 'y'):
    print("Please Input options for FastQC, Trimmomatics, STAR, and FeatureCount")
    PATH2 = input("Please Input the Path$ ")
    try:
        fastqc.getQC(PATH2)
    except:
        print("FastQC step has something wrong.....!")
else:
    pass
    
    

#import trimmomatic
os.system("pwd")

###################         Quality Check          ################################

## first step : indexing 

import starindexing
    
## second step : mapping 

import starmapping


## Change Log in v1.0.2
## 1. Add Computational Time estimation in each step
## 2. Correct Color map for Tree
## 3. Correct Loading library function

## Change Log in v1.0.3
## 1. Add Generating multiple figures for web visualization for each sample

## Change Log in v1.0.4
## 1. Data was newly added (Approximately 200 Samples)
## 2. VP1 Sequence Extraction
## 3. Algorithm Improved (x20 fast)