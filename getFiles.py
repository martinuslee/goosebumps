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

#link = [p_a,ensembl]
#print(input)

dic = { 1: 'GRCh38', 2:'GRCm38', 3:'GRCz11' }

t1 =0
t2= 0
result = 0

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
                
                
                
def getfileDir(dir, find):
    list = os.listdir(dir)
    for item in list:
        if item.find(find) >= 0:
            item = dir + item
            return item
            
            
def timeCheck(function, *args):
    #print(*args,'\n')
    t1 = time.time()
    function(*args)
    
    t2 = time.time()
    result = t2 -t1
    print("seconds : ", result,'\n')
    
    