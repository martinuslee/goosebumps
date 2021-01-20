import os
import wget 
import math 

##############################################    download files web paths    ##################################################

release = input("Please Input Release Version (i.e. 102)$ ")
species = input("Please Input Species (i.e. homo_sapiens)$ ")
Species = species.capitalize() #Homo_sapiens
refID = input("Please Input reference id (i.e. GRCh38)$ ")
PATH = input("Please Input Download Path$ ")
dot = "."
slash ="/"
p_a = "ftp://ftp.ensembl.org/pub/release-"+release+"/fasta/"+species+"/dna/"+Species+ dot + refID + dot + "dna.primary_assembly.fa.gz"
ensembl = "ftp://ftp.ensembl.org/pub/release-"+release+"/gtf/"+species+ slash +Species+ dot + refID +dot + release + ".gtf.gz"

link = [p_a,ensembl]
print(input)

###########################################     Downloading funuctoins      #################################################

def bar_custom(current, total, width=80):
    width=30
    avail_dots = width-2
    shaded_dots = int(math.floor(float(current) / total * avail_dots))
    percent_bar = '[' + '■'*shaded_dots + ' '*(avail_dots-shaded_dots) + ']'
    progress = "%d%% %s [%d / %d]" % (current / total * 100, percent_bar, current, total)
    return progress

def download(url, out_path):
    wget.download(url, out=out_path, bar=bar_custom)

################### unzip fastA file (if this is .gz) #########################

def unzipfiles(dir):
    list = os.listdir(dir)
    for item in list:
        fa = '.fa.gz'
        if item.find(fa) > 0:
            cmd = "gzip -d " + dir + item
            print(cmd)
            os.system(cmd)   
            
##############################################     Download files using functions    ###########################################

## if input is human files ##

input = link
try:
    for i in input:
        download(i,PATH)
        unzipfiles(PATH)          
        
        #print("completed : " + i)
except:
    print("FASTA File Download Error...!")    