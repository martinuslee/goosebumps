from Bio import SeqIO
import sys 
import re
import os
import wget 
import math 
import gzip

filename_forward = "/disk11/SRR390728_1.fastq.gz"
filename_reverse = "/disk11/SRR390728_2.fastq.gz"
# Compiler and path tool
ja = " java -jar"
tool = " /program/Trimmomatic/trimmomatic-0.39.jar"
s = " "

# path for trimmomatic /program/Trimmomatic/trimmomatic-0.39.jar
# os.system(java -jar /program/Trimmomatic/trimmomatic-0.39.jar)


# Outputs paired end
output_forward_paired = "/disk11/output_forward_paired_SRR390728_1.fastq.gz"
output_forward_unpaired = "/disk11/output_forward_unpaired_SRR390728_1.fastq.gz"
output_reverse_paired = "/disk11/output_reverse_paired_SRR390728_2.fastq.gz"
output_reverse_unpaired = "/disk11/output_reverse_unpaired_SRR390728_2.fastq.gz"
print("Start Trimmonatics :")
print("--------------------")
attribute = "PE -threads 12 -phred33 "
#illuminaclip_adapters = "ILLUMINACLIP:/program/Trimmomatic/adapters/TruSeq3-PE.fa:2:30:10"
illuminaclip_adapters = "ILLUMINACLIP:/program/Trimmomatic/adapters/TruSeq3-PE.fa:2:30:10"
illuminaclip_Attribute = "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"
cmd1 = s + ja + s + tool + s + attribute + s + filename_forward + s + filename_reverse + s + output_forward_paired + s + output_forward_unpaired
cmd2 = s + output_reverse_paired + s + output_reverse_unpaired + s + illuminaclip_adapters + s + illuminaclip_Attribute
cmd = cmd1 + cmd2
os.system(cmd)

#SLIDINGWINDOW : 5'end부터 시작해서 average quality가 threshold 값 미만인지 스캐닝
#윈도우 사이즈 값 내의 퀄리티 이면서 threshold이하인 것들을 커팅해버리는 일명 슬라이딩 윈도우 트리밍을 하자
#여러 베이스들을 읽고 댕기기 때문에 한두개 퀄리티 낮은 것들이 뒤에가서 고퀄의 데이터를 제거하는데는 별 영향 없음

#TRAILING : threshold quality 이하일 read의 끝 서열들을 제거
#끝에서부터 저퀄의 base를 날림. (퀄리티 스코어 2정도 되는 special illumina low quality segment region 같은 부분)도 이 방법에 의해
#트리밍 될 수 있는데 sliding window나 maxinfo에서 하길 추천


#MINLEN : 어느 정도의 length 이하면 그 리드는 배제 dropped reads가 카운트 될 것
