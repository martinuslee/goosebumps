import sys 
import re
import os
import wget 
import math 
import gzip


filename_forward = "/disk11/3.Pipeline_test_ljh/SRR390728_1.fastq.gz"
#fastq_forward = open(filename_forward, 'r')

# FASTQ file where you want to trim all the reads

print("Let's get started to check read object...!")

with gzip.open(filename_forward, "rt") as handle:
    records = list(SeqIO.parse(handle, "fastq"))
    print(records[0])  # first record

'''

count = 0
with gzip.open(filename_forward, "rt") as handle:
    for record in SeqIO.parse(handle, "fastq"):
#        if(record.id == "SRR390728.1886807"):
#            print(record.seq)   
        count += 1
print("fastq forward %i reads" % count) # count reads



# Load data reverse
filename_reverse = "/disk11/3.Pipeline_test_ljh/SRR390728_2.fastq.gz"
# FASTQ file where you want to trim all the reads
count = 0
with gzip.open(filename_reverse, "rt") as handle:
    for record in SeqIO.parse(handle, "fastq"):
        count += 1
print("fastq reverse %i reads" % count) # count reads

'''