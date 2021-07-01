import sys
import os 


fc = "featureCounts"
s =" "
p = "-p"    # paired -end
larget = "-T"    #thread
o = "-o"    # output file
a = "-a"    # annotation file
g = "-g gene_id"
smallt = "-t exon"


def getFC(path, core, gtf , filename):
    bam = "STAR_map/" + filename + "Aligned.sortedByCoord.out.bam"
    output_file = filename + "_fc.txt"
    mkdir = path + "FeatureCounts"
    try: 
        if os.path.isdir(mkdir): # IF Theres not a STAT  MAP DIR
            print('caret')
            
            cmd = fc + s + p + s + smallt + s + g + s + larget + s + core + s + a + s + gtf + s + o + s + mkdir + '/' + output_file + s + path + bam
            #print(cmd)
            os.system(cmd + ' &')
        else:
            os.makedirs(mkdir)
            print('onion')
            cmd = fc + s + p + s + smallt + s + g + s + larget + s + core + s + a + s + gtf + s + o + s + mkdir + '/' + output_file + s + path + bam
            #print(cmd)
            os.system(cmd + ' &')
    except FileExistsError:
        # dir already exists..
        os.system("rm -d " + mkdir)
        print("(featureCounts) Error occuered..\nPlease Try it again..\n")
        sys.exit()
    


#featureCounts -T 4 -s 2 -a <gtf file> -o <output file> <inputfile *.bam>