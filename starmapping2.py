import sys 
import re
import os
import math 
import getFiles

## second step : mapping 

# runMode: STAR 프로그램의 실행모드 (맵핑은 “alignReads”로 설정함) // %% 인덱스 생성은 genomeGenerate %%
# --runThreadN: 맵핑에 사용할 thread 개수
# --outFilterMultimapNmax: 결과물 (BAM 포맷의 맵핑된 데이터)에 기록 가능한 각 read 별 최대 맵핑 허용치 (허용치를 초과할 경우 맵핑 되지 않는 것으로 판단함)
# --alignIntronMin: 맵핑 허용 최소 인트론 길이 (본 내용에서는 알려진 인간 유전자의 인트론 길이 분포로부터 0.01% 구간을 설정함)
# --alignIntronMax: 맵핑 허용 최대 인트론 길이 (본 내용에서는 알려진 인간 유전자의 인트론 길이 분포로부터 99.9% 구간을 설정함)
# --genomeDir: 맵핑에 사용할 참조 유전체 인덱스가 저장된 디렉토리
# --readFilesIn: 품질 관리된 입력 데이터 파일 (입력 데이터의 타입이 paired-end 인 경우는 공백으로 첫번째 read 와 두번째 read 파일을 구분하여 입력)
# --outSAMtype: 출력 데이터 파일의 종류 (SAM: SAM 파일, BAM Unsorted: 포지션으로 정돈되지않은 BAM 파일, BAM SortedByCoordinate: 포지션으로 정돈된 BAM 파일)
# --outFileNamePrefix: 맵핑된 결과물을 생성하고 저장할 파일 이름의 접두사를 지정
 
# --alignIntronMax INTRONMAX : exon-exon-junction(EEJ)에 걸친 reads까지 매핑되면 시간 낭비니까 인트론 최대값 이상으로 떨어져 있는 split reads에는 얼라인이 안되게 해줌
 

# STAR --runMode alignReads --runThreadN 2 --outFilterMultimapNmax 10 --
#alignIntronMin 61 --alignIntronMax 265006 --genomeDir /인덱스_파일_디렉토리/
#--readFilesIn data1_1.trimmed.fastq data1_2.trimmed.fastq --readFilesCommand zcat --outSAMtype
#BAM SortedByCoordinate --outFileNamePrefix [output filename]

star = "STAR"
s =" "  #   space bar 
indexMode = "--runMode genomeGenerate"
mapMode = "--runMode alignReads"      
outdir = "--genomeDir"
th = "--runThreadN"
intron = "--alignIntronMax INTRONMAX"
outtype = "--outSAMtype BAM SortedByCoordinate"
read = "--readFilesIn"
zcat = "--readFilesCommand zcat"
#outputFile = "--outFileNamePrefix /disk11/3.Pipeline_test_ljh/STAR_map/testSample"
outputFile = "--outFileNamePrefix"
junction = "--limitSjdbInsertNsj"

# STAR --genomeDir /disk1/bijh/ref/star_Anas_platyrhynchos_platyrhynchos/ --genomeLoad NoSharedMemory --runThreadN 48 --readFilesIn ${sp}.R1.fq ${sp}.R2.fq --outFileNamePrefix ${sp}.STAR
# 
def getMapAm(path, outPath, file1, file2, outFileName):

    
    cmd = star + s + th + s + "16" + s + outdir + s + path + s + read + s + file1 + s + file2 + s + zcat + s + outtype + s + outputFile + s + outPath + outFileName 
    print('time ' + cmd + + ' '+' &')
    #os.system(cmd + ' &')
    print("running___%s"%(outFileName))

path = '/disk1/bijh/ref/'
targetDir = path + '' #star_ 로 시작하는 디렉토리 안의 디렉토리
outDir = ''
file1, file2 = 'fastq_1', 'fastq_2'
outFileName = ''

        
#getMapAm(path , '/disk1/bijh/ref/mapping_Anas_platyrhynchos_platyrhynchos/', '/disk3/bipsw/SRR1758114_1.fastq.gz', '/disk3/bipsw/SRR1758114_2.fastq.gz', 'SRR1758114')
getFiles.getFastqFiles('/disk3/bipsw/')