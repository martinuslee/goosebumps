import sys ,re ,os, math, time
import getopt
import wget 
import gzip
import getFiles, fastqc, trimmomatic, starindexing, starmapping, featureCount
import getopt
#import countReads

try: 
    options, args = getopt.getopt(sys.argv[1:], "v:s:i:p:j",
    ['fastq','tdir=', 'th=', 'tver=', 'LEADING=', 
    'TRAILING=','SLIDINGWINDOW=','MINLEN=','mode=','fout=','T='])
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

release = None
species = None
refID = None
PATH = None
p_a = None
ensembl =None

fastq1 = None
fastq2 = None
thread = None

truseq = None
tPATH = ''
mode = None
core = None
fout = None

check = False

for o, a in options:
    if o in ("-v"):
        release = a
        check = True
       # print(a)
    elif o in ("-s"):
        species = a
        Species = Species = species.capitalize() #Homo_sapiens
        #print(a)
    elif o in ("-i"):
        refID = a       
        #print(a)
    elif o in ("-p"):
        PATH = a
        #print(a)
    elif o == "--fastq":
        fastq1 = args[0]
        fastq2 = args[1]
        #print(fastq1, fastq2)
    elif o == "--tdir":
        tPATH = a
        #print(a)
    elif o == '--th':
        thread = a
        #print(a)
    elif o == '--tver':
        truseq = a
        #print(a)
    elif o == '--mode':
        mode = a
        #print(a)
    elif o in ("--T"):
        core = a
        #print(a)
    elif o == '--fout':
        fout = a
        #print(a)        
    else : 
        assert False, "unhandled option"
       
##############################################     Download files using functions    ##############################################

# python3 pipeline.py -v 102 -s danio_rerio -i GRCz11 -p /disk11/3.Pipeline_test_ljh/ --tdir /program/Trimmomatic/trimmomatic-0.39.jar --th 16 --tver TruSeq3-PE.fa --mode genomeGenerate --fastq SRR390728_1.fastq.gz SRR390728_2.fastq.gz
# python3 pipeline.py -v 102 -s coturnix_japonica -p /disk11/3.Pipeline_test_ljh/ --tdir /program/Trimmomatic/trimmomatic-0.39.jar --th 32 --tver TruSeq3-PE.fa --mode genomeGenerate --T 4 --fout featureCount.txt --fastq SRR390728_1.fastq.gz SRR390728_2.fastq.gz
# python3 ~/disk11/3.Pipeline_test_ljh/pipeline.py -p /disk11/3.Pipeline_test_ljh/ --tdir /program/Trimmomatic --th 32 --tver TruSeq3-PE.fa --mode genomeGenerate --fastq SRR390728_1.fastq.gz SRR390728_2.fastq.gz
# python3 pipeline.py -v 102 -s danio_rerio -i GRCz11 -p /disk11/3.Pipeline_test_ljh/ --tdir /program/Trimmomatic/trimmomatic-0.39.jar --th 16 --tver TruSeq3-PE.fa --mode genomeGenerate --fastq /disk11/3.Pipeline_test_ljh/SRR390728_1.fastq.gz /disk11/3.Pipeline_test_ljh/SRR390728_2.fastq.gz

# print(fastq1,fastq2)

startTime = time.time()
endTime = 0

if check:
    getFiles.timeCheck(getFiles.getRef,release, species, refID, PATH)
else:
    pass

##############################################       Trimmomatic        ##############################################
     
getFiles.timeCheck(trimmomatic.trimmomatic, PATH, tPATH, truseq, thread, fastq1, fastq2)

##############################################         FAST QC        ##############################################

getFiles.timeCheck(fastqc.getQC, args, PATH)

##############################################      STAR Indexing       ##############################################

#fafile = getFiles.getfileDir(PATH, 'primary_assembly')
fafile = getFiles.getfileDir(PATH, 'toplevel')
gtffile = getFiles.getfileDir(PATH, '.gtf')

getFiles.timeCheck(starindexing.getIndexAm, PATH, thread, mode, fafile, gtffile)

##############################################      STAR Mapping       ##############################################

mapDir = PATH+"Trimmomatic_Results/"
file1 = getFiles.getfileDir(mapDir, 'output_forward_paired_')
file2 = getFiles.getfileDir(mapDir, 'output_reverse_paired_')

getFiles.timeCheck(starmapping.getMapAm, PATH, thread, file1, file2)

##############################################      Feature Counts        ##############################################

getFiles.timeCheck(featureCount.getFC, PATH, core, gtffile, fout)

endTime = time.time()

print(" total : ", endTime - startTime)