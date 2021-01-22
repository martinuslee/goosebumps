# RNA-Seq-pipeline
RNA_Seq Python Pipeline 

requirement : python3 fastqc trimmomatic star

Biopython, gzip, wget, getopt

-------------------------------

+ example command 
```
  python3 pipeline.py -v 102 -s coturnix_japonica -i Coturnix_japonica_2.0 -p /disk11/3.Pipeline_test_ljh/ --tdir /program/Trimmomatic/ --th 32 --tver TruSeq3-PE.fa --mode genomeGenerate --T 4 --fout featureCount.txt --fastq /disk11/3.Pipeline_test_ljh/SRR390728_1.fastq.gz /disk11/3.Pipeline_test_ljh/SRR390728_2.fastq.gz
```
+ To Download fastq files 
```
  -v Ensembl version
  -s Scientific Name
  -i Ref version 
  -p /PATH/ 
```
+ To launch Pipeline tools
```
  --tdir <TRIMMOMATIC TOOL PATH>
  --th Number of Thread 
  --tver Adapter Ver.
  --mode STAR Mode (default alignReads)
  --T Number of CPU Core for featureCounts
  --fout featureCounts outputfile.txt
  --fastq <file1> <file2>
```
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
