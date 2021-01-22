# :astonished:  Goosebumps paired-end RNA-Seq pipeline
RNA_Seq Python Pipeline 

:ballot_box_with_check: requirement : python3 Fastqc Trimmomatic Star featureCounts , and *.fastq files

Biopython, gzip, wget, getopt

  :heavy_check_mark: Notice : *.fastq files must be located in the same directory with option -p /Path/

-------------------------------

+ example command (SRR390728)
```
  python3 pipeline.py -v 102 -s coturnix_japonica -i Coturnix_japonica_2.0 -p /disk11/3.Pipeline_test_ljh/ --tdir /program/Trimmomatic/ --th 32 --tver TruSeq3-PE.fa --mode genomeGenerate --T 4 --fout featureCount.txt --fastq /disk11/3.Pipeline_test_ljh/SRR390728_1.fastq.gz /disk11/3.Pipeline_test_ljh/SRR390728_2.fastq.gz
```
+ To Download fastq files 
```
  -v Ensembl version
  -s Scientific Name
  -i Ref version 
  -p /PATH/ ( 
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

## getFiles.py

+ Download reference files on Ensembl DB through wget. 
+ Other functions definition. 

## fastqc.py 

+ To build fastq.html files for the read files's quality check. 

## trimmomatic.py

+ Trimming read files and get 4 outputfiles (forward_paired, forward_unpaired, reverse_paired, reverse_unpaired)
  + removing adapters... adapter options required

## starindexing.py

+ alignment step
  + indexing fa file (reference file)

## starmapping.py

+ mapping seq files to gtf file 
  + output data type is sorted bam
  
## FeatureCount.py
 
+ check expression rate
