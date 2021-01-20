# Rna-Seq-pipeline
RNA_Seq Python Pipeline 

requirement : python3 fastqc trimmomatic star

Biopython, gzip, wget 

-------------------------------

## pipeline.py 

+ this is the main script file.
+ you can use the functions below importing subscript files.

## getFiles.py

Download reference files on Ensembl DB through wget 
if the files already exists, you can pass this step through input 'n' 

pipeline.py
```c
checkFiles = input("Do you want to download ref files [Y/n]$ ");
if(checkFiles == 'Y'):
    import getFiles
else:
    pass
```

getfiles.py functions
input : release version, species, reference Id, output dir path
```c

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
```


## fastqc.py 

fastqc command build fastq.html files to check quality check for the read files.

## trimmomatic.py

## starindexing.py

## starmapping.py
