import sys 
import re
import os
import wget 
import math 
import gzip


#SLIDINGWINDOW : 5'end부터 시작해서 average quality가 threshold 값 미만인지 스캐닝
#윈도우 사이즈 값 내의 퀄리티 이면서 threshold이하인 것들을 커팅해버리는 일명 슬라이딩 윈도우 트리밍을 하자
#여러 베이스들을 읽고 댕기기 때문에 한두개 퀄리티 낮은 것들이 뒤에가서 고퀄의 데이터를 제거하는데는 별 영향 없음

#TRAILING : threshold quality 이하일 read의 끝 서열들을 제거
#끝에서부터 저퀄의 base를 날림. (퀄리티 스코어 2정도 되는 special illumina low quality segment region 같은 부분)도 이 방법에 의해
#트리밍 될 수 있는데 sliding window나 maxinfo에서 하길 추천


#MINLEN : 어느 정도의 length 이하면 그 리드는 배제 dropped reads가 카운트 될 것

#### for trimmomatic options

#filename_forward = PATH + "SRR390728_1.fastq.gz"


#print(filename_forward, filename_reverse)


# Compiler and path tool

ja = " java -jar"

s = " "


def trimmomatic(path, tPATH, truseq, thread, fastq1, fastq2):
    try:
        mkdir = path+"Trimmomatic_Results"
        os.makedirs(mkdir)

        filename_forward = os.path.basename(fastq1)
        
        filename_reverse = os.path.basename(fastq2) 
        
        toolDir = tPATH + "trimmomatic-0.39.jar"
        # Outputs paired end
        output_forward_paired = path + "Trimmomatic_Results/output_forward_paired_" + filename_forward
        output_forward_unpaired = path + "Trimmomatic_Results/output_forward_unpaired_" + filename_reverse
        output_reverse_paired = path + "Trimmomatic_Results/output_reverse_paired_" + filename_forward
        output_reverse_unpaired = path + "Trimmomatic_Results/output_reverse_unpaired_" + filename_reverse

        attribute = "PE -threads " + thread+  " -phred33 "
        #illuminaclip_adapters = "ILLUMINACLIP:/program/Trimmomatic/adapters/TruSeq3-PE.fa:2:30:10"
        illuminaclip_adapters = "ILLUMINACLIP:" + tPATH + "adapters/"+truseq+":2:30:10"
        illuminaclip_Attribute = "LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"
    

        print("\n Start Trimmonatics :")
        print("--------------------")
        
        cmd1 = s + ja + s + toolDir + s + attribute + s + filename_forward + s + filename_reverse + s + output_forward_paired + s + output_forward_unpaired
        cmd2 = s + output_reverse_paired + s + output_reverse_unpaired + s + illuminaclip_adapters + s + illuminaclip_Attribute

    ### LET's get started
        cmd = cmd1 + cmd2
        print(cmd)
        os.system(cmd)
        print("\n Finished Trimmonatics :")
        print("-----------------------\n")

    except FileExistsError:
        # dir already exists..
        #os.system("rm -r " +mkdir)
        print("trim dir already exists..\n")
        pass
    