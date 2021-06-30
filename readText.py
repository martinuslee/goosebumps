# fastq file 리스트가 담긴 텍스트들을 읽어와서 파싱한다.

import sys
import os
from pprint import pprint
srrList = list()

path_dir = '/disk1/bijh/10.Circadian_Transcriptome/data/'
file_list = os.listdir(path_dir)
file_list.sort()

#print(file_list)

result = []

for i in range(0,len(file_list),2):
    result.append([file_list[i],file_list[i+1]])
pprint(result)




'''
SRR13649888
SRR13649889
SRR13649893
SRR13649895
SRR13649896
SRR13649897
SRR13649899
SRR13649901
SRR13649902
SRR13649903
SRR13649904
SRR13649908
SRR13649909
SRR13649910
SRR13649911
SRR13649894
SRR13649891
SRR13649906
SRR13649900
SRR13649898
SRR13649892
SRR13649907
SRR13649890
SRR13649905
'''