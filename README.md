# :astonished:  Goosebumps paired-end RNA-Seq pipeline
RNA_Seq Python Pipeline 
:copyright:ABCLab Jongheon Lee

:ballot_box_with_check: requirement : python3 Fastqc Trimmomatic Star featureCounts , and *.fastq files

Biopython, gzip, wget, getopt

  :heavy_check_mark: Notice : *.fastq files must be located in the same directory with option -p /Path/

-------------------------------

+ example command (SRR390728)
```
  python3 pipeline.py -v 104 -s mus_musculus -i GRCm39 -p /disk1/bijh/10.Circadian_Transcriptome/ --tdir /program/Trimmomatic/ --th 32 --tver TruSeq3-PE.fa --mode genomeGenerate --T 4 

```
+ To Download reference files 
```
  -v <Ensembl version>
  -s <Scientific Name>
  -i <Ref version >
  -p </PATH/> where fastq files located
```
+ To launch Pipeline tools
```
  --tdir <PATH> TRIMMOMATIC TOOL PATH
  --th <int> Number of Thread
  --tver <Adapter Ver.>
  --mode <STAR Mode> (default alignReads)
  --T <int> Number of CPU Core for featureCounts
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
