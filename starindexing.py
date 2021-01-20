from Bio import SeqIO
import sys 
import re
import os
import wget 
import math 
import gzip


star = "STAR"
s =" "  #   space bar 
indexMode = "--runMode genomeGenerate"
mapMode = "--runMode alignReads"      
outdir = "--genomeDir /disk11/3.Pipeline_test_ljh/star" #  output directory
fasta = "--genomeFastaFiles"
th = "runThreadN 16"
gtf = "--sjdbGTFfile"
intron = "(--alignIntronMax INTRONMAX)"
outtype = "--outSAMtype BAM SortedByCoordinate"
read = "--readFilesIn"


def getfileDir(dir, find):
    list = os.listdir(dir)
    for item in list:
        if item.find(find) > 0:
            item = dir + item
            return item


dir = "/disk11/3.Pipeline_test_ljh/"
#file1 = "/disk11/3.Pipeline_test_ljh/output_forward_paired_SRR390728_1.fastq.gz";
#file2 = "/disk11/3.Pipeline_test_ljh/output_reverse_paired_SRR390728_2.fastq.gz";
file1 = getfileDir(dir, '_1')
file2 = getfileDir(dir, '_2')
fafile = getfileDir(dir, 'primary_assembly')
#fafile = "/disk11/3.Pipeline_test_ljh/Homo_sapiens.GRCh38.dna_rm.primary_assembly.fa"
#gtffile = "/disk11/3.Pipeline_test_ljh/Homo_sapiens.GRCh38.102.gtf.gz"
gtffile = getfileDir(dir, '.gtf')

class faError(Exception):
    def __str__(self):
        return "star indexing error : fa file has something wrong.....!"    

cmd = star + s + indexMode + s + outdir + s + fasta+ s + fafile

try:
    print(cmd)
    os.system(cmd)
    
except faError as e:
    print(e)
    