from Bio import SeqIO
import sys 
import re
import os
import wget 
import math 
import gzip
#import dircache #install

#import countReads
checkFiles = input("Do you want to download ref files [Y/n]$ ");
if(checkFiles == 'Y'):
    import getFiles
else:
    pass
#import fastqc
#import trimmomatic
os.system("pwd")

###################         Quality Check          ################################

## first step : indexing 

# --runMode: STAR 프로그램의 실행모드 (인덱스 생성은 “genomeGenerate”로 설정함)
# --genomeDir: 참조 유전체 데이터 파일의 인덱스를 생성하고 저장할 디렉토리
# --genomeFastaFiles: 참조 유전체 서열 데이터 파일 (FASTA 포맷)
# --sjdbOverhang  99 : reads가 101bp일때 씀, 안적어도 돌아감


import starindexing
    
## second step : mapping 

import starmapping
