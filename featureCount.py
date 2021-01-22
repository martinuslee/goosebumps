import os 


fc = "featureCounts"
s =" "
p = "-p"    # paired -end
larget = "-T"    #thread
o = "-o"    # output file
a = "-a"    # annotation file
g = "-g gene_id"
smallt = "-t exon"
bam = "STAR_map/testSample_Aligned.sortedByCoord.out.bam"

def getFC(path, core, gtf , output):
    try: 
        mkdir = path + "FeatureCounts"
        os.makedirs(mkdir)
        #print(mkdir)
        cmd = fc + s + p + s + smallt + s + g + s + larget + s + core + s + a + s + gtf + s + o + s + mkdir + '/' +output + s + path + bam
        print(cmd)
        os.system(cmd)
    except FileExistsError:
        # dir already exists..
        #os.system("rm -d " + mkdir)
        print("featureCounts dir already exists..\n")
        pass
    


#featureCounts -T 4 -s 2 -a <gtf file> -o <output file> <inputfile *.bam>