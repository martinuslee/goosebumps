import sys 
import re
import os
import math 

# --runMode: STAR 프로그램의 실행모드 (인덱스 생성은 “genomeGenerate”로 설정함)
# --genomeDir: 참조 유전체 데이터 파일의 인덱스를 생성하고 저장할 디렉토리
# --genomeFastaFiles: 참조 유전체 서열 데이터 파일 (FASTA 포맷)
# --sjdbOverhang  99 : reads가 101bp일때 씀, 안적어도 돌아감

star = "STAR"
s =" "  #   space bar 
indexMode = "--runMode genomeGenerate"
mapMode = "--runMode alignReads"
#outdir = "--genomeDir /disk11/3.Pipeline_test_ljh/star" #  output directory
outdir = "--genomeDir"
fasta = "--genomeFastaFiles"
th = "--runThreadN"
gtf = "--sjdbGTFfile"
intron = "(--alignIntronMax INTRONMAX)"
outtype = "--outSAMtype BAM SortedByCoordinate"
read = "--readFilesIn"
overhang = "--sjdbOverhang 35"

#STAR --runMode genomeGenerate --runThreadN 16 --genomeDir /disk1/bijh/ref/star_Coturnix_japonica --genomeFastaFiles Coturnix_japonica.Coturnix_japonica_2.0.dna.toplevel.fa

# time (STAR --runMode genomeGenerate --runThreadN 16 --genomeDir /disk1/bijh/ref/star_Anser_brachyrhynchus --genomeFastaFiles Anser_brachyrhynchus.ASM259213v1.dna.toplevel.fa > Anser_brachyrhynchus.txt ) >> Anas_platyrhynchos_platyrhynchos.txt
# time (STAR --runMode genomeGenerate --runThreadN 16 --genomeDir /disk1/bijh/ref/star_Anser_cygnoides --genomeFastaFiles Anser_cygnoides.GooseV1.0.dna.toplevel.fa > Anser_cygnoides.txt ) >> Anser_cygnoides.txt  
# time (STAR --runMode genomeGenerate --runThreadN 16 --genomeDir /disk1/bijh/ref/star_Apteryx_rowi --genomeFastaFiles Apteryx_rowi.aptRow1.dna.toplevel.fa > Apteryx_rowi.txt ) >> Apteryx_rowi.txt & 
# time (STAR --runMode genomeGenerate --runThreadN 16 --genomeDir /disk1/bijh/ref/star_Aquila_chrysaetos_chrysaetos --genomeFastaFiles Aquila_chrysaetos_chrysaetos.bAquChr1.2.dna.toplevel.fa > Aquila_chrysaetos_chrysaetos.txt ) >> Aquila_chrysaetos_chrysaetos.txt & 
# time (STAR --runMode genomeGenerate --runThreadN 16 --genomeDir /disk1/bijh/ref/star_Felis_catus --genomeFastaFiles Felis_catus.Felis_catus_9.0.dna.toplevel.fa > Felis_catus.txt ) >> Felis_catus.txt & 
# time (STAR --runMode genomeGenerate --runThreadN 16 --genomeDir /disk1/bijh/ref/star_Parus_major --genomeFastaFiles Parus_major.Parus_major1.1.dna.toplevel.fa > Parus_major.txt ) >> Parus_major.txt & 
# time (STAR --runMode genomeGenerate --runThreadN 16 --genomeDir /disk1/bijh/ref/star_Taeniopygia_guttata --genomeFastaFiles Taeniopygia_guttata.bTaeGut1_v1.p.dna.toplevel.fa > Taeniopygia_guttata.txt ) >> Taeniopygia_guttata.txt & 

def getIndexAm(path, thN, mode, fafile, gtffile):
    mkdir = path + "STAR_Index"
    try:
        os.makedirs(mkdir)
        cmd = star + s + indexMode + s + th + s + thN + s + outdir + s + mkdir + s + fasta + s + fafile + s + gtf + s + gtffile + s + overhang 
        print(cmd)
        os.system(cmd)  
    except FileExistsError:
        # dir already exists..
        os.system("rm -d " +mkdir)
        print("STAR Index Error occuered....\nPlease Try it again..\n")
    

'''
def getfileDir(dir, find):
    list = os.listdir(dir)
    for item in list:
        if item.find(find) > 0:
            item = dir + item
            return item


dir = "/disk11/3.Pipeline_test_ljh/"
file1 = getfileDir(dir, '_1')
file2 = getfileDir(dir, '_2')
fafile = getfileDir(dir, 'primary_assembly')
gtffile = getfileDir(dir, '.gtf')
'''
