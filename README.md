# RNA-Seq-pipeline
RNA_Seq Python Pipeline 

requirement : python3 fastqc trimmomatic star

Biopython, gzip, wget 

-------------------------------

+ example command 
'''
  python3 pipeline.py -v 102 -s coturnix_japonica -p /disk11/3.Pipeline_test_ljh/ --tdir /program/Trimmomatic/trimmomatic-0.39.jar --th 32 --tver TruSeq3-PE.fa --mode genomeGenerate --T 4 --fout featureCount.txt --fastq SRR390728_1.fastq.gz SRR390728_2.fastq.gz
'''

## pipeline.py 

+ this is the main script file.
+ you can use the functions below importing subscript files.

## getFiles.py

+ Download reference files on Ensembl DB through wget 
+ if the files already exists, you can pass this step through input 'n' 

## fastqc.py 

fastqc command build fastq.html files to check quality check for the read files.

## trimmomatic.py

## starindexing.py

## starmapping.py
