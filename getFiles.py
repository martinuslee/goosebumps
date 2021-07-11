import os
import wget 
import math 
import time

##############################################    download files web paths    ##################################################

#release = input("Please Input Release Version (i.e. 102)$ ")
#species = input("Please Input Species (i.e. homo_sapiens)$ ")
#Species = species.capitalize() #Homo_sapiens
#refID = input("Please Input reference id (i.e. GRCh38)$ ")
#PATH = input("Please Input Download Path$ ")
dot = "."
slash ="/"
#p_a = "ftp://ftp.ensembl.org/pub/release-"+release+"/fasta/"+species+"/dna/"+Species+ dot + refID + dot + "dna.primary_assembly.fa.gz"
#ensembl = "ftp://ftp.ensembl.org/pub/release-"+release+"/gtf/"+species+ slash +Species+ dot + refID +dot + release + ".gtf.gz"
#GRCm39
# /disk1/bijh/10.Circadian_Transcriptome


#python3 pipeline.py -v 104 -s mus_musculus -i GRCm39 -p /disk1/bijh/10.Circadian_Transcriptome/ --tdir /program/Trimmomatic/ --th 32 --tver TruSeq3-PE.fa --mode genomeGenerate --T 4 --fout featureCount.txt

dic = { 1: 'GRCh38', 2:'GRCm39', 3:'GRCz11' } # 생물 종 선택 

def getRef(release, species, refID,PATH ):

    Species = species.capitalize() #Homo_sapiens
    
    if(refID == dic[1] or refID == dic[2] or refID == dic[3]):
        p_a = "ftp://ftp.ensembl.org/pub/release-"+release+"/fasta/"+species+"/dna/"+Species+ dot + refID + dot + "dna.primary_assembly.fa.gz"
    else:
        p_a = "ftp://ftp.ensembl.org/pub/release-"+release+"/fasta/"+species+"/dna/"+ Species + dot + refID + dot + "dna.toplevel.fa.gz"
        
    ensembl = "ftp://ftp.ensembl.org/pub/release-"+release+"/gtf/"+species+ slash + Species + dot + refID + dot + release + ".gtf.gz"
    link = [p_a,ensembl]
    input = link
    
    for i in input:
        print("start : " + i)
        download(i,PATH)
        unzipfiles(PATH)          
        print("completed : " + i)

###########################################     Downloading funuctoins      #################################################

def bar_custom(current, total, width=80):
    width=30
    avail_dots = width-2
    shaded_dots = int(math.floor(float(current) / total * avail_dots))
    percent_bar = '[' + '■'*shaded_dots + ' '*(avail_dots-shaded_dots) + ']'
    progress = "%d%% %s [%d / %d]" % (current / total * 100, percent_bar, current, total)
    return progress

def download(url, out_path):
    #print(out_path)
    wget.download(url, out=out_path, bar=bar_custom)

########################################### unzip fastA file (if this is .gz) ###########################################

def unzipfiles(dir):
    list = os.listdir(dir)
    for item in list:
        fa = '.fa.gz'
        gtf = '.gtf.gz'
        if item.find(fa) > 0 or item.find(gtf) > 0:
            cmd = "gzip -d " + dir + item
            #print(cmd)
            os.system(cmd)   
            
            
def isFiles(f, dir, name):
    list = os.listdir(dir)
    #name = '.fa.gz'
    for item in list: 
        if item.find(name) > 0:
            f.append(item)



def getFastqFiles(path_dir):
    from pprint import pprint

    #path_dir = '/disk1/bijh/10.Circadian_Transcriptome/data/'
    file_list = os.listdir(path_dir)
    file_list.sort()

    #print(file_list)

    result = []

    for i in range(0,len(file_list),2):
        result.append([file_list[i],file_list[i+1]])
    #pprint(result)
    return result

                
                
def getfileDir(dir, find):
    file_list = os.listdir(dir)
    file_list.sort()
    result  = list()
    for item in file_list:
        if find in item:
            item = dir + item
            result.append(item)
    return result


            

# 시간 체크용 변수 
t1 =0
t2= 0
result = 0           
def timeCheck(function, *args):
    #print(*args,'\n')
    t1 = time.time()
    function(*args)
    
    t2 = time.time()
    result = t2 -t1
    print("seconds : ", result,'\n')
    
    